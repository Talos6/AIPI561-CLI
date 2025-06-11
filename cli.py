from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from src import utils, llm

console = Console()

def main():
    console.print(Panel(
        "Welcome to git assistant!\n"
        "• Describe your Git operations in natural language and I will handle it\n"
        "• Type 'quit' to exit", 
        title="Git Assistant", 
        style="bold blue"
    ))

    while True:
        description = Prompt.ask("\nWhat would you like to do?")
        description = description.strip()
        
        if description.lower() == 'quit':
            console.print("Goodbye!", style="blue")
            break
        else:
            console.print(f"Analyzing: {description}", style="blue")
            try:
                commands = llm.get_commands(description)
                console.print(Panel('\n'.join(f"• {command}" for command in commands), title="Commands", style="blue"))
                decision = Prompt.ask("Are you sure you want to execute these commands?", choices=["y", "n"])
                if decision == 'y':
                    utils.execute_command(commands)
            except Exception as e:
                utils.handle_error(e)
            continue

if __name__ == '__main__':
    main()