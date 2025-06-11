import json
import boto3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize AWS Bedrock client with environment variables
bedrock = boto3.client(
    'bedrock-runtime',
    region_name=os.getenv('AWS_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

def get_commands(message):
    prompt = f"""
        You are a Git expert. Convert the following natural language description into a sequence of Git commands.
        Return ONLY the Git commands, one per line, without any explanation or markdown formatting.
        Description: {message}
    """
    
    try:
        response = bedrock.invoke_model(
            modelId=os.getenv('MODEL_ID'),
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 500,
                "temperature": 0.1,
                "top_p": 0.9,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            })
        )
        
        response_body = json.loads(response['body'].read())
        content = response_body['content'][0]['text']
        commands = [cmd.strip() for cmd in content.strip().split('\n')
                   if cmd.strip() and cmd.strip().startswith('git')]
        
        if not commands:
            raise ValueError("No valid Git commands were generated")
            
        return commands
        
    except Exception as e:
        raise RuntimeError(f"Failed to generate Git commands: {str(e)}")