import os
import re
from rp_cli.utils.clear_screen import clear
from rp_cli.utils.display_message import display_message

CONFIG_PATH = os.path.expanduser('~/.config/config.json')

def update_config(**kwargs):
    """
    Updates the configuration file located at `~/.config/linux-discord-rich-presencerc` with new values.

    This function reads the existing configuration file, updates specified fields with new values,
    and writes the updated content back to the file. It supports updating both top-level fields and
    nested fields within a parent field. If a field does not exist, it will be created.

    Parameters:
    - **kwargs: A dictionary of field names and their new values. The keys are the field names, and
                the values are the new values to be set.
    - intg (optional): A boolean indicating whether the values are integers. Defaults to False.

    Raises:
    - FileNotFoundError: If the configuration file does not exist at the specified path.

    Example:
    - update_config(state="online")
    - update_config(application_id=123456789, intg=True)

    Note:
    - This function supports updating fields that are either strings or integers, depending on the 'intg' parameter.
    - The 'subfield_of' keyword is used to specify a parent field for nested updates.
    - Nested fields are updated by preserving the structure of the parent field and replacing only the
      specified nested field's value.
    """
    if not os.path.exists(CONFIG_PATH):
        clear()
        return display_message("💻 Operation cancelled by the system! \n\n⁉ Config file not found at $HOME/.config/linux-discord-rich-presencerc!\n\n🔙 Returning to the previous prompt...", style="error")

    # Read the entire script
    with open(CONFIG_PATH, 'r') as file:
        script = file.read()

    # Update the fields
    for key, value in kwargs.items():
        if key == 'subfield_of' or key == 'intg':
            continue # Skip processing 'subfield_of' or 'intg' as an update target

        # Check if the field exists
        pattern = re.compile(rf'"{key}":\s*("[^"]*"|\d+)')
        match = pattern.search(script)

        if 'subfield_of' in kwargs:
            # Handle nested fields
            parent_field = kwargs['subfield_of']
            # Determine the pattern based on whether the value is an integer
            pattern = re.compile(rf'"{parent_field}":\s*{{\s*.*?"{key}":\s*("[^"]*"|\d+).*?}}', re.DOTALL)
            # Replace the nested field value with the new value, ensuring other subfields are preserved
            updated_field = f'"{key}": "{value}"' if not kwargs.get('intg', False) else f'"{key}": {value}'
            script = pattern.sub(lambda match: match.group().replace(f'"{key}": {match.group(1)}', updated_field), script)
        elif match:
            # If the field exists, update its value
            updated_field = f'"{key}": "{value}"' if not kwargs.get('intg', False) else f'"{key}": {value}'
            script = pattern.sub(updated_field, script)
        else:
            # If the field does not exist, insert it into the first object of the array
            # Find the position right after the opening brace of the first object
            insert_position = script.find('{') + 1
            # Insert the new field
            script = script[:insert_position] + f'\n    "{key}": "{value}",' + script[insert_position:]

    # Write the updated script back to the file
    with open(CONFIG_PATH, 'w') as file:
        file.write(script)