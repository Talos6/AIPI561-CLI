# Git Assistant CLI

A command-line tool that converts natural language descriptions into Git commands using AWS Bedrock AI.

## Quick Start

1. **Setup environment**:
   ```bash
   cp env.sample .env
   # Edit .env with your AWS credentials
   pip install -r requirements.txt
   ```

2. **Run the assistant**:
   ```bash
   python cli.py
   ```

3. **Use natural language**:
   ```
   What would you like to do? > commit all my changes with message "fix login bug"
   ```

## Documentation

- **[User Guide](docs/guide.md)** - How to use the Git Assistant
- **[Technical Overview](docs/overview.md)** - Architecture, components, and implementation details

## Requirements

- Python 3.7+
- AWS Account with Bedrock access
- Git installed on your system

## Features

- 🗣️ Natural language to Git commands
- ✅ Command preview before execution  
- 🛡️ Safe execution with confirmations
- 🎨 Rich terminal interface
- ⚡ Real-time command output

