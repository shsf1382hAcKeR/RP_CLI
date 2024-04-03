import inquirer
from rp_cli.config import update_config

def handle_small_image_update():
    questions = [
        inquirer.List('subfield',
                      message="Choose a subfield to update",
                      choices=['key', 'text'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        return

    subfield = answers['subfield']
    if subfield == 'key':
        questions = [
            inquirer.Text('key', message="Enter new key for small image")
        ]
        answers = inquirer.prompt(questions)
        if answers is None:
            return
        new_key = answers['key']
        update_config(key=new_key, subfield_of="small_image")
    elif subfield == 'text':
        questions = [
            inquirer.Text('text', message="Enter new text for small image")
        ]
        answers = inquirer.prompt(questions)
        if answers is None:
            return
        new_text = answers['text']
        update_config(text=new_text, subfield_of="small_image")

    return "Small image updated successfully."