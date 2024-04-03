import inquirer
from rp_cli.config import update_config

def handle_application_id_update():
    questions = [
        inquirer.Text('application_id', message="Enter new application ID")
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        return

    new_application_id = answers['application_id']
    update_config(application_id=new_application_id)
    return "Application ID updated successfully."