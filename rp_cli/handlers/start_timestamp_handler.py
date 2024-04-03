import inquirer
from rp_cli.config import update_config

def handle_start_timestamp_update():
    questions = [
        inquirer.Text('start_timestamp', message="Enter new start timestamp")
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        return

    new_start_timestamp = answers['start_timestamp']
    update_config(start_timestamp=new_start_timestamp)
    return "Start timestamp updated successfully."
