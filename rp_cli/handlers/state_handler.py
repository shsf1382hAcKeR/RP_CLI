import inquirer
from rp_cli.config import update_config

def handle_state_update():
    questions = [
        inquirer.Text('state', message="Enter new state")
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        return

    new_state = answers['state']
    update_config(state=new_state)
    return "State updated successfully."
