from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def display_message(message, style="info"):
    """
    Displays a message with a rectangular border.

    :param message: The message to display.
    :param style: The style of the message, can be "info" or "error".
    """
    if style == "error":
        color = "red"
    else:
        color = "green"

    text = Text(message, style=color)
    panel = Panel(text, expand=False, border_style=color)
    console.print(panel)