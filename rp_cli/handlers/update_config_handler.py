import typer
import inquirer
from rp_cli.theme import custom_theme
from rp_cli.ascii_arts.config_art import config

def handle_update_config():
    typer.echo(config())
    questions = [
        inquirer.List('field',
                      message="Choose a field to update",
                      choices=['application_id', 'state', 'details', 'start_timestamp', 'large_image', 'small_image'],
                      ),
    ]
    answers = inquirer.prompt(questions, theme=custom_theme())
    if answers is None:
        return

    field = answers['field']
    if field in ['application_id', 'state', 'details', 'start_timestamp']:
        handler_module = f"rp_cli.handlers.{field}_handler"
        handler_function = f"handle_{field}_update"
        module = __import__(handler_module, fromlist=[handler_function])
        function = getattr(module, handler_function)
        return function()
    elif field in ['large_image', 'small_image']:
        handler_module = f"rp_cli.handlers.{field}_handler"
        handler_function = f"handle_{field}_update"
        module = __import__(handler_module, fromlist=[handler_function])
        function = getattr(module, handler_function)
        return function()
