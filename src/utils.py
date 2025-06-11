import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

def get_git_commands():
    return [
        "python --version",
        "git --version",
        "git status"
    ]

def get_examples():
    return [
        "commit changes",
        "create and switch to new branch",
        "show file change status",
        "view commit history"
    ]

def execute_command(commands):
    for command in commands:
        console.print(f"Executing: {command}", style="dim")
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            if result.stdout:
                console.print(result.stdout.strip(), style="green")
        else:
            error_msg = result.stderr.strip() if result.stderr else f"Command failed with exit code {result.returncode}"
            console.print(f"Failed on command: {command}\n{error_msg}", style="red")
            return

def handle_error(error):
    error_type = type(error).__name__
    error_message = str(error)
    
    console.print(Panel(f"{error_type}: {error_message}",
                       title="Error",
                       style="red"))