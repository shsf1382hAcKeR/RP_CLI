import typer
import inquirer
from rp_cli.theme import custom_theme
from rp_cli.ascii_arts.config_art import config
from rp_cli.utils.clear_screen import clear
from rp_cli.utils.display_message import display_message

def handle_update_config():
    typer.echo(config(custom_message="💡 You can also manually update the config file located at $HOME/.config/linux-discord-rich-presencerc.\n\n🔙 Ctrl+Shift+C: Go back"))
    questions = [
        inquirer.List('field',
                      message="Choose a field to update (use arrow keys ⬆ ⬇)",
                      choices=['application_id', 'state', 'details', 'start_timestamp', 'large_image', 'small_image'],
                      ),
    ]
    answers = inquirer.prompt(questions, theme=custom_theme())
    if answers is None:
        clear()
        return display_message("👤 Operation cancelled by the user! \n\n🔙 Returning to the previous prompt...", style="error")
    
    field = answers['field']
    if field in ['application_id', 'state', 'details', 'start_timestamp']:
        handler_module = f"rp_cli.handlers.{field}_handler"
        handler_function = f"handle_{field}_update"
        module = __import__(handler_module, fromlist=[handler_function])
        function = getattr(module, handler_function, clear())
        return function()
    elif field in ['large_image', 'small_image']:
        handler_module = f"rp_cli.handlers.{field}_handler"
        handler_function = f"handle_{field}_update"
        module = __import__(handler_module, fromlist=[handler_function])
        function = getattr(module, handler_function, clear())
        return function()
