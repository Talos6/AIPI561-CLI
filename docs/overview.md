# Overview

## Architecture

```
┌─────────────┐    ┌─────────────┐     ┌─────────────┐
│    CLI      │───▶│     LLM     │───▶│   Utils     │
│   (cli.py)  │    │  (llm.py)   │     │ (utils.py)  │
└─────────────┘    └─────────────┘     └─────────────┘
      │                   │                   │
      ▼                   ▼                   ▼
   User I/O          AWS Bedrock        Command Exec
```

## Components

### 1. CLI Module (`cli.py`)
- **Purpose**: User interface and main application
- **Key Functions**:
  - Application entry point
  - Interactive

### 2. LLM Module (`llm.py`)
- **Purpose**: NLP command generator via AWS Bedrock
- **Key Functions**:
  - Converts natural language to Git commands
  - AWS Bedrock integration with Claude

### 3. Utils Module (`utils.py`)
- **Purpose**: System utilities
- **Key Functions**:
  - Command execution
  - Error handling

## Data Flow

1. **User Input** → CLI captures natural language description
2. **LLM Processing** → Description sent to AWS Bedrock Claude model
3. **Command Generation** → LLM returns structured Git commands
4. **User Confirmation** → Commands displayed for approval
5. **Sequential Execution** → Commands executed one by one
6. **Real-time Output** → Results displayed immediately
7. **Error Handling** → Execution stops on first failure

## Error Handling

### Exception Types
- **LLM Errors**: AWS connection, authentication, or model failures
- **Command Errors**: Git command failures with exit codes
- **System Errors**: Timeout, permission, or subprocess failures

### Error Strategy
- **Immediate Stop**: Execution halts on first command failure
- **Graceful Display**: Errors shown in styled red panels

## Environment Setup

### Required Variables
```bash
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
MODEL_ID=anthropic.claude-3-5-sonnet-20240620-v1:0
```

### Dependencies
- `rich`: Terminal UI and styling
- `boto3`: AWS SDK for Bedrock integration  
- `python-dotenv`: Environment variable management

## Test Coverage
| File | Test File | Coverage |
|------|-----------|----------|
| **cli.py** | Manual |  All scenarios, error cases |
| **llm.py** | Indirect |  Via CLI testing |
| **utils.py** | Indirect | Via CLI testing |

## Lessons Learned

- **CLI**: Interactive console with automatic sub process
- **Prompt Engineering**: Prompt to restrict model response
- **Scalability**: Extensible to be console assistant

## Future Improvements
- **Dry Run**: Test mode that shows commands without execution
- **Caching**: Caching for duplicated or similar question
- **Plugin Architecture**: Deploy and wrap as tool that can be accessible easily
