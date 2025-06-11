from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from src import utils

console = Console()

def main():
    console.print(Panel(
        "Welcome to git assistant!\n"
        "• Describe your Git operations in natural language and we will handle it\n"
        "• Type 'examples' to see available operations\n"
        "• Type 'quit' to exit", 
        title="Git Assistant", 
        style="bold blue"
    ))

    while True:
        description = Prompt.ask("\nWhat would you like to do?")
        description = description.strip().lower()
        
        if description == 'quit':
            decision = Prompt.ask("Are you sure you want to quit?", choices=["y", "n"])
            if decision == 'y':
                console.print("Goodbye!", style="blue")
                break
            else:
                continue
        elif description == 'examples':
            try:
                tasks = utils.get_examples()
                console.print(Panel("\n".join(f"• {task}" for task in tasks),
                                  title="Example Git Operations",
                                  style="blue"))
            except Exception as e:
                utils.handle_error(e)
            continue
        else:
            console.print(f"Analyzing: {description}", style="blue")
            commands = utils.get_git_commands()
            console.print(Panel('\n'.join(f"• {command}" for command in commands), title="Commands", style="blue"))
            decision = Prompt.ask("Are you sure you want to execute these commands?", choices=["y", "n"])
            if decision == 'y':
                utils.execute_command(commands)
            continue

if __name__ == '__main__':
    main()