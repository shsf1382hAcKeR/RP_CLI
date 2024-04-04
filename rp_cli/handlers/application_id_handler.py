import inquirer
from inquirer.errors import ValidationError
from rp_cli.utils.config import update_config
from rp_cli.utils.clear_screen import clear
from rp_cli.utils.display_message import display_message
from rp_cli.utils.read_current_value import read_current_value

def handle_application_id_update():
    def validate_application_id(answers, value):
        if not value.isdigit():
            raise ValidationError("Application ID must be a number.", reason="Application ID must be a number.")
        return True

    display_message("🔑 This ID is crucial for Discord to access application details and assets.\n\n💡 Create a new application in 'Discord's Developer Portal' at https://discord.com/developers \n\n🔙 Ctrl+Shift+C: Cancel edit")
    current_state = read_current_value("application_id", intg=True)
    questions = [
        inquirer.Text(
            'application_id', 
            message="Update application ID",
            default=current_state,
            validate=validate_application_id
        )
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        clear()
        return display_message("👤 Operation cancelled by the user! \n\n🔙 Returning to the previous prompt...", style="error")

    new_application_id = answers['application_id']
    update_config(application_id=new_application_id, intg=True)
    clear()
    return display_message("Application ID updated successfully 🙌🎉")
