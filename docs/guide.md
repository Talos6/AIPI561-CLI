# User Guide

## Overview
Git Assistant is a command-line tool that converts natural language descriptions into Git commands and executes them.

## Usage

### Starting the Application
```bash
python cli.py
```

### Basic Operations
1. **Describe what you want to do** in plain English
   - Example: "commit all my changes with message 'fix bug'"
   - Example: "create a new branch called feature-login"
   - Example: "show me the status of my files"

2. **Review the generated commands** - The tool will show you exactly what Git commands it plans to run

3. **Confirm execution** - Type 'y' to execute or 'n' to cancel

4. **View results** - See the output of your Git commands in real-time

### Example Session
```
What would you like to do? > commit all changes with message "update documentation"

Commands:
• git add .
• git commit -m "update documentation"

Are you sure you want to execute these commands? [y/n]: y

Executing: git add .
Executing: git commit -m "update documentation"
[main 1a2b3c4] update documentation
 2 files changed, 15 insertions(+), 3 deletions(-)
```

### Exiting
Type `quit` to exit the application.

## Tips
- Be specific in your descriptions for better command generation
- Always review the generated commands before executing
- The tool stops execution immediately if any command fails 