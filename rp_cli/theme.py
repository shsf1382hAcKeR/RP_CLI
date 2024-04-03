import inquirer

def custom_theme():
    return inquirer.themes.load_theme_from_dict({
        "Question": {
            "mark_color": "yellow",
            "brackets_color": "\033[36m",
        },
        "List": {
            "selection_cursor": "✔",
        }
    })
