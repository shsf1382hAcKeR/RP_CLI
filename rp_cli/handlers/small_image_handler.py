import inquirer
from inquirer.errors import ValidationError
from rp_cli.theme import custom_theme
from rp_cli.utils.config import update_config
from rp_cli.utils.clear_screen import clear
from rp_cli.utils.display_message import display_message
from rp_cli.utils.read_current_value import read_current_value

def handle_small_image_update():
    def validate_input(answers, value):
        if not value:
            raise ValidationError("Input cannot be empty.", reason="Input cannot be empty.")
        return True

    display_message("🔑 The small image field consists of a key and text. Choose which to update.\n\n🔙 Ctrl+Shift+C: Cancel edit")
    questions = [
        inquirer.List('subfield',
                      message="Choose a subfield to update",
                      choices=['key', 'text'],
                      ),
    ]
    answers = inquirer.prompt(questions, theme=custom_theme())
    if answers is None:
        clear()
        return display_message("👤 Operation cancelled by the user! \n\n🔙 Returning to the previous prompt...", style="error")

    subfield = answers['subfield']
    if subfield == 'key':
        current_key = read_current_value('key',subfield_of="small_image")
        questions = [
            inquirer.Text('key', message="Enter new key for small image", default=current_key, validate=validate_input)
        ]
        answers = inquirer.prompt(questions)
        if answers is None:
            clear()
            return display_message("👤 Operation cancelled by the user! \n\n🔙 Returning to the previous prompt...", style="error")
        new_key = answers['key']
        update_config(key=new_key, subfield_of="small_image")
    elif subfield == 'text':
        current_text = read_current_value('text',subfield_of="small_image")
        questions = [
            inquirer.Text('text', message="Enter new text for small image", default=current_text, validate=validate_input)
        ]
        answers = inquirer.prompt(questions)
        if answers is None:
            clear()
            return display_message("👤 Operation cancelled by the user! \n\n🔙 Returning to the previous prompt...", style="error")
        new_text = answers['text']
        update_config(text=new_text, subfield_of="small_image")

    clear()
    return display_message("Small image updated successfully 🙌🎉")