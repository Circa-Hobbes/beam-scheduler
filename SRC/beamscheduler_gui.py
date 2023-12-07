from nicegui import app, ui


# Turn on dark mode for the website.
ui.dark_mode().enable()


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
            ui.label("6. The script adheres to ACI 318-19 for beam design.")
        ui.button("Understood", on_click=dialog.close).classes(
            "self-center text-lg mt-4"
        )


# Call the start popup function to greet the user with what is required to run the script.
start_popup()

ui.run()
