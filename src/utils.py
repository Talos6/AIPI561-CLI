"""
Utility functions for the CLI tool.
"""

from rich.console import Console
from rich.panel import Panel

console = Console()

def get_git_commands():
    return [
        "ls"
    ]

def get_examples():
    return [
        "commit changes",
        "create and switch to new branch",
        "show file change status",
        "view commit history"
    ]

def handle_error(error):
    """Handle and display errors in a user-friendly way.
    
    Args:
        error: The exception to handle
    """
    error_type = type(error).__name__
    error_message = str(error)
    
    console.print(Panel(f"{error_type}: {error_message}",
                       title="Error",
                       style="red"))