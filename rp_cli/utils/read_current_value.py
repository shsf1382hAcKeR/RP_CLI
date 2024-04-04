import os
import re
from rp_cli.utils.clear_screen import clear
from rp_cli.utils.display_message import display_message

CONFIG_PATH = os.path.expanduser('~/.config/config.json')

def read_current_value(field, subfield_of=None, intg=False):
    """
    Reads the current configuration file and returns the value of the specified field.

    Parameters:
    - field: The name of the field to read the value from.
    - subfield_of (optional): The name of the parent field if the field is a subfield.
    - intg (optional): A boolean indicating whether the value is an integer. Defaults to False.

    Returns:
    - The value of the specified field if found, otherwise None.

    Raises:
    - FileNotFoundError: If the configuration file does not exist at the specified path.

    Example:
    - read_current_value("application_id")
    - read_current_value("application_id", intg=True)
    - read_current_value("key", subfield_of="small_image")

    Note:
    - This function supports reading fields that are either strings or integers, depending on the 'intg' parameter.
    - It also supports reading nested fields by specifying the parent field with the 'subfield_of' parameter.
    """
    if not os.path.exists(CONFIG_PATH):
        clear()
        return display_message("💻 Operation cancelled by the system! \n\n⁉ Config file not found at $HOME/.config/linux-discord-rich-presencerc!\n\n🔙 Returning to the previous prompt...", style="error")

    with open(CONFIG_PATH, 'r') as file:
        script = file.read()

    # Construct the pattern based on whether the value is an integer and whether it's a subfield
    if subfield_of:
        pattern = re.compile(rf'"{subfield_of}":\s*{{\s*.*?"{field}":\s*("[^"]*"|\d+).*?}}', re.DOTALL) if not intg else re.compile(rf'"{subfield_of}":\s*{{\s*.*?"{field}":\s*(\d+).*?}}', re.DOTALL)
    else:
        pattern = re.compile(rf'"{field}":\s*("[^"]*"|\d+)', re.DOTALL) if not intg else re.compile(rf'"{field}":\s*(\d+)', re.DOTALL)

    match = pattern.search(script)
    if match:
        # Extract the value without quotes for string values
        value = match.group(1)
        # If intg is True, convert the value to an integer
        return int(value) if intg else value.strip('"')
    return None