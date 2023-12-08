from nicegui import app, ui


# Turn on dark mode for the website.
ui.dark_mode().enable()

# Call the Eva Icons for icon usage.
ui.add_head_html(
    '<link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet">'
)


# Create function which describes limitations and requirements of beam scheduler.
def start_popup():
    """This function aims to clarify what the beam scheduler does and what it requires
    to run properly."""
    with ui.dialog() as dialog, ui.card().classes("w-fit"):
        app.on_connect(dialog)
        ui.label("Beam Scheduler v0.1").classes("self-center font-bold text-4xl -my-2")
        ui.label("Made by Adnan Almulla @ Killa Design").classes("self-center text-2xl")
        ui.label(
            "To utilise this script appropriately, please consider and abide by the following:"
        ).classes("text-lg text-red-500 flex-nowrap")
        with ui.row().classes("text-lg w-full"):
            ui.label(
                "1. When exporting design results from ETABS, flexure and shear must be exported in the same spreadsheet."
            )
            ui.label(
                "2. All facade and superimposed beam elements must not be included in the exported spreadsheet."
            )
            ui.label(
                "3. Beam section definitions in ETABS must follow a naming convention such as ''B400X600-C45/55'', where 400 is width and 600 is depth."
            )
            ui.label(
                "4. The engineer must account for the fact that flexural design first prioritises an increase of rebar diameter up to 32mm, then proceeds to add an additional layer."
            )
            ui.label(
                "5. The engineer must account for the fact that shear design first prioritises an increase of spacing down to 100mm, then proceeds to increase the rebar diameter."
            )
            ui.label("6. This script adheres to ACI 318-19 for beam design.")
        ui.button("Understood", on_click=dialog.close).classes(
            "self-center text-lg mt-4"
        )


# Create a copy function of start_popup to enable the question button to have a dialog popup
async def question_popup():
    """This function mimics start-popup, except it does not come up on start and only comes up when the question
    button is clicked"""
    with ui.dialog() as dialog, ui.card().classes("w-fit"):
        ui.label("Beam Scheduler v0.1").classes("self-center font-bold text-4xl -my-2")
        ui.label("Made by Adnan Almulla @ Killa Design").classes("self-center text-2xl")
        ui.label(
            "To utilise this script appropriately, please consider and abide by the following:"
        ).classes("text-lg text-red-500 flex-nowrap")
        with ui.row().classes("text-lg w-full"):
            ui.label(
                "1. When exporting design results from ETABS, flexure and shear must be exported in the same spreadsheet."
            )
            ui.label(
                "2. All facade and superimposed beam elements must not be included in the exported spreadsheet."
            )
            ui.label(
                "3. Beam section definitions in ETABS must follow a naming convention such as ''B400X600-C45/55'', where 400 is width and 600 is depth."
            )
            ui.label(
                "4. The engineer must account for the fact that flexural design first prioritises an increase of rebar diameter up to 32mm, then proceeds to add an additional layer."
            )
            ui.label(
                "5. The engineer must account for the fact that shear design first prioritises an increase of spacing down to 100mm, then proceeds to increase the rebar diameter."
            )
            ui.label("6. This script adheres to ACI 318-19 for beam design.")
        ui.button("Understood", on_click=dialog.close).classes(
            "self-center text-lg mt-4"
        )
    await dialog


# Create upper row containing script name, KLD logo, github logo, and question mark for popup.
def ui_header():
    """This function holds the upper row which carries the title and logos."""
    with ui.grid(columns=3).classes("w-full no-wrap"):
        with ui.row().classes("pt-4 pb-6 pr-6 pl-10 justify-start items-start"):
            ui.button(
                icon="question_mark", on_click=question_popup, color="#075985"
            ).classes("rounded-full w-16 h-16 ml-4")
        with ui.row().classes(
            "bg-sky-900 pt-6 pb-6 pr-6 pl-6 rounded-full justify-center items-center"
        ):
            ui.label(
                "Beam Scheduler v0.1 - Made by Adnan Almulla @ Killa Design"
            ).classes("text-2xl font-bold pr-1")
            ui.image("assets/kld logo outlined.png").classes("w-14 h-14")
        with ui.row().classes("pt-4 pb-6 pr-10 pl-6 justify-end items-end"):
            ui.element("i").classes("eva eva-github").classes("text-7xl")


# Call the start popup function to greet the user with what is required to run the script.
start_popup()

ui_header()

ui.run()
