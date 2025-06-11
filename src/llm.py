import json
import boto3

# Initialize AWS Bedrock client
bedrock = boto3.client('bedrock-runtime')

def get_git_commands(message):
    prompt = f"""
        You are a Git expert. Convert the following natural language description into a sequence of Git commands.
        Return ONLY the Git commands, one per line, without any explanation or markdown formatting.
        Description: {message}
    """
    
    try:
        response = bedrock.invoke_model(
            modelId='anthropic.claude-v2', 
            body=json.dumps({
                "prompt": prompt,
                "max_tokens_to_sample": 500,
                "temperature": 0.1,
                "top_p": 0.9,
            })
        )
        
        response_body = json.loads(response['body'].read())
        commands = [cmd.strip() for cmd in response_body['completion'].strip().split('\n')
                   if cmd.strip() and cmd.strip().startswith('git')]
        
        if not commands:
            raise ValueError("No valid Git commands were generated")
            
        return commands
        
    except Exception as e:
        raise RuntimeError(f"Failed to generate Git commands: {str(e)}")