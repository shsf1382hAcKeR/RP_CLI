import inquirer
from inquirer.errors import ValidationError
from rp_cli.utils.config import update_config
from rp_cli.utils.clear_screen import clear
from rp_cli.utils.display_message import display_message
from rp_cli.utils.read_current_value import read_current_value

def handle_details_update():
    def validate_details(answers, value):
        if not value:
            raise ValidationError("Details cannot be empty.", reason="Details cannot be empty.")
        return True

    display_message("🔑 The details field represents what you are currently doing.\n\n🔙 Ctrl+Shift+C: Cancel edit")
    current_details = read_current_value('details')
    questions = [
        inquirer.Text(
            'details', 
            message="Update details",
            default=current_details,
            validate=validate_details
        )
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        clear()
        return display_message("👤 Operation cancelled by the user! \n\n🔙 Returning to the previous prompt...", style="error")

    new_details = answers['details']
    update_config(details=new_details)
    clear()
    return display_message("Details updated successfully 🙌🎉")