import os
import re

CONFIG_PATH = os.path.expanduser('~/.config/linux-discord-rich-presencerc')

def update_config(**kwargs):
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Config file not found at {CONFIG_PATH}")

    # Read the entire script
    with open(CONFIG_PATH, 'r') as file:
        script = file.read()

    # Update the fields
    for key, value in kwargs.items():
        if key == 'subfield_of':
            continue # Skip processing 'subfield_of' as an update target

        if 'subfield_of' in kwargs:
            # Handle nested fields
            parent_field = kwargs['subfield_of']
            # Create a regex pattern to match the nested field within the parent field
            # This pattern captures the value of the nested field we want to update
            pattern = re.compile(rf'"{parent_field}":\s*{{\s*.*?"{key}":\s*"([^"]*)".*?}}', re.DOTALL)
            # Replace the nested field value with the new value, ensuring other subfields are preserved
            updated_field = f'"{key}": "{value}"'
            script = pattern.sub(lambda match: match.group().replace(f'"{key}": "{match.group(1)}"', updated_field), script)
        else:
            # Create a regex pattern to match the field name and its value
            pattern = re.compile(rf'"{key}":\s*"[^"]*"')
            # Replace the field value with the new value
            updated_field = f'"{key}": "{value}"'
            script = pattern.sub(updated_field, script)

    # Write the updated script back to the file
    with open(CONFIG_PATH, 'w') as file:
        file.write(script)