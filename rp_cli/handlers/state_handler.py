import inquirer
from inquirer.errors import ValidationError
from rp_cli.utils.config import update_config
from rp_cli.utils.clear_screen import clear
from rp_cli.utils.display_message import display_message
from rp_cli.utils.read_current_value import read_current_value

def handle_state_update():
    def validate_state(answers, value):
        if not value:
            raise ValidationError("State cannot be empty.", reason="State cannot be empty.")
        return True

    display_message("🔑 The state field represents your current party status or what you are doing/working on.\n\n🔙 Ctrl+Shift+C: Cancel edit")
    current_state = read_current_value('state')
    questions = [
        inquirer.Text(
            'state', 
            message="Update state",
            default=current_state,
            validate=validate_state
        )
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        clear()
        return display_message("👤 Operation cancelled by the user! \n\n🔙 Returning to the previous prompt...", style="error")

    new_state = answers['state']
    update_config(state=new_state)
    clear()
    return display_message("State updated successfully 🙌🎉")