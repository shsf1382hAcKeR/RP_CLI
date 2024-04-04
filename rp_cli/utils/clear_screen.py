import os

def clear():
    """
    Clears the terminal screen using cls or clean commands.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
