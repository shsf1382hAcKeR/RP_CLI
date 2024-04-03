import inquirer
from rp_cli.config import update_config

def handle_details_update():
    questions = [
        inquirer.Text('details', message="Enter new details")
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        return

    new_details = answers['details']
    update_config(details=new_details)
    return "Details updated successfully."
