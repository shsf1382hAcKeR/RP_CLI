import typer
import inquirer
from .theme import custom_theme
from .ascii_arts.intro_art import intro
from .handlers.update_config_handler import handle_update_config
from rp_cli.utils.display_message import display_message
from rp_cli.utils.clear_screen import clear

app = typer.Typer()

@app.command()
def cli():
    clear()
    while True:        
        typer.echo(intro())
        questions = [
            inquirer.List('action',
                          message="Choose an option (use arrow keys ⬆ ⬇)",
                          choices=['Update Configuration', 'Exit'],
                          ),
        ]
        answers = inquirer.prompt(questions, theme=custom_theme())
        if answers is None:
            return

        if answers['action'] == 'Update Configuration':
            clear()
            message = handle_update_config()
            if message:
                typer.echo(message)
        elif answers['action'] == 'Exit':
            display_message("Bye! 🚀👋", style="info")
            return

if __name__ == "__main__":
    app()