import inquirer
from inquirer.errors import ValidationError
from rp_cli.theme import custom_theme
from rp_cli.utils.config import update_config
from rp_cli.utils.clear_screen import clear
from rp_cli.utils.display_message import display_message
import time

from rp_cli.utils.read_current_value import read_current_value

def handle_start_timestamp_update():
    def validate_timestamp(answers, value):
        if not value.isdigit():
            raise ValidationError("Timestamp must be a number.", reason="Timestamp must be a number.")
        if int(value) > int(time.time()):
            raise ValidationError("Timestamp cannot be in the future.", reason="Timestamp cannot be in the future.")
        return True

    display_message("🔑 The start timestamp field represents the start time of your activity.\n\n🔙 Ctrl+Shift+C: Cancel edit")
    questions = [
        inquirer.List('action',
                      message="Choose an action",
                      choices=['Set Current Time', 'Set your own Unix timestamp'],
                      ),
    ]
    answers = inquirer.prompt(questions, theme=custom_theme())
    if answers is None:
        clear()
        return display_message("👤 Operation cancelled by the user! \n\n🔙 Returning to the previous prompt...", style="error")

    if answers['action'] == 'Set Current Time':
        new_start_timestamp = int(time.time())
        update_config(start_timestamp=new_start_timestamp, intg=True)
        clear()
        return display_message("Start timestamp set to current time successfully 🙌🎉")
    elif answers['action'] == 'Set your own Unix timestamp':
        current_key = read_current_value('start_timestamp')
        display_message(
            "💡 A Unix timestamp is the number of seconds that have elapsed since January 1, 1970 (UTC).\n\n"
            "💡 You can obtain the current Unix timestamp by using online tools or programming languages.\n\n"
            "💡 For example, in Python, you can use `import time; print(int(time.time()))` to get the current timestamp."
        )
        questions = [
            inquirer.Text('start_timestamp', message="Enter your Unix timestamp", default=current_key, validate=validate_timestamp)
        ]
        answers = inquirer.prompt(questions)
        if answers is None:
            clear()
            return display_message("👤 Operation cancelled by the user! \n\n🔙 Returning to the previous prompt...", style="error")
        new_start_timestamp = int(answers['start_timestamp'])
        update_config(start_timestamp=new_start_timestamp, intg=True)
        clear()
        return display_message("Start timestamp updated successfully 🙌🎉")