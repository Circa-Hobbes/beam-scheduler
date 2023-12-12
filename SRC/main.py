import pandas as pd
import beamscheduler_gui as gui
from nicegui import ui, events
import io
import tempfile
import df_processing as pr
import asyncio

# Global variable to store the processed DataFrame
processed_beam_schedule_df = None


def main():
    gui.start_popup()
    gui.ui_header()
    gui.main_row(lambda e: excel_handler(e, main_container))
    main_container = gui.download_button()
    ui.run()


# Handle and utilise the excel spreadsheet for processing.
def excel_handler(e: events.UploadEventArguments, container):
    global processed_beam_schedule_df
    ui.notify(
        f"{e.name} successfully uploaded! Please await processing.", type="positive"
    )
    # Schedule the processing of the content asynchronously
    asyncio.create_task(process_content(e, container))


async def process_content(e: events.UploadEventArguments, container):
    global processed_beam_schedule_df
    excel_file = e.content
    initial_flexural_df = pd.read_excel(excel_file, sheet_name=0)
    initial_shear_df = pd.read_excel(excel_file, sheet_name=1)
    processed_beam_schedule_df = await asyncio.to_thread(
        pr.process_dataframes, initial_flexural_df, initial_shear_df
    )
    with container:
        ui.notify(
            "Processing complete. Please download the completed beam schedule.",
            type="positive",
        )
        add_down_button()


def add_down_button():
    with ui.grid(columns=3).classes("w-full no-wrap mt-5"):
        with ui.row().classes("pt-8 pb-6 pr-6 pl-10 justify-start items-start"):
            pass
        with ui.row().classes("pt-6 pb-6 pr-6 pl-6 justify-center items-center"):
            ui.button(
                "download beam schedule",
                on_click=download_handler,
                color="#075985",
            ).classes("text-lg font-bold self-center rounded-full").on(
                "click", lambda: ui.notify("Downloading...")
            )
        with ui.row().classes("pt-8 pb-6 pr-6 pl-10 justify-start items-start"):
            pass


# Create the relevant functions to export the excel file
def export_file(beam_schedule_df):
    # Use BytesIO as an in-memory buffer
    output = io.BytesIO()

    # Create an Excel writer object with the BytesIO object
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        # Write the entire DataFrame to the first sheet
        beam_schedule_df.to_excel(writer, sheet_name="Beam Reinforcement Schedule")

        # Group by the 'Storey' column
        grouped = beam_schedule_df.groupby("Storey", sort=False)

        # Iterate through the groups and write to separate sheets
        for name, group in grouped:
            sheet_name = f"{name}"
            group.to_excel(writer, sheet_name=sheet_name)

    # Return the Excel file content from the in-memory buffer
    return output.getvalue()


def download_handler():
    global processed_beam_schedule_df
    if processed_beam_schedule_df is not None:
        # Call export_file to get the in-memory Excel file
        excel_content = export_file(processed_beam_schedule_df)

        # Write the content to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
            tmp.write(excel_content)
            tmp_path = tmp.name  # Store the file path

        # Initiate the download using the file path
        ui.download(tmp_path, "beam_schedule.xlsx")
    else:
        ui.notify(
            "No data available for download or uploaded file does not adhere to considerations. Please try again.",
            type="negative",
        )


if __name__ in {"__main__", "__mp_main__"}:
    main()
