import os
import sys
import requests
import argparse

def signin(api_base_url, username, password):
    """Sign in to Memos using gRPC-web"""
    endpoint = f"{api_base_url}/memos.api.v1.AuthService/SignIn"
    
    headers = {
        "Content-Type": "application/grpc-web+proto",
        "Accept": "*/*",
        "x-grpc-web": "1"
    }
    
    # Create binary payload as seen in the curl request
    # \u0000\u0000\u0000\u0000\u001a\n\u0005pablo\u0012\u000f2023Espana67945\u0018\u0001
    payload = b'\x00\x00\x00\x00\x1a\n\x05' + username.encode() + b'\x12\x0f' + password.encode() + b'\x18\x01'
    
    try:
        print(f"Signing in as {username}...")
        response = requests.post(
            endpoint,
            headers=headers,
            data=payload
        )
        print(f"Sign-in response: {response.status_code}")
        
        # Get token from cookie
        cookies = response.cookies
        token = cookies.get('memos.access-token')
        if token:
            return token
            
        return None
    except Exception as e:
        print(f"Sign in failed: {e}")
        return None

def create_memo(api_base_url, api_key, content, tags=None, visibility="PRIVATE"):
    """Create a memo using gRPC-web"""
    endpoint = f"{api_base_url}/memos.api.v1.MemoService/CreateMemo"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/grpc-web+proto",
        "Accept": "*/*",
        "x-grpc-web": "1"
    }

    # Start with user provided tags
    tags = tags or []
    
    # Get default tags from environment variable and append them
    default_tags = os.getenv("MEMOS_DEFAULT_TAG")
    if default_tags:
        # Split by comma and strip whitespace, then append all non-empty tags
        default_tag_list = [tag.strip() for tag in default_tags.split(',')]
        tags.extend([tag for tag in default_tag_list if tag])
    
    # Format tags with hashtags
    hashtags = ' '.join([f'#{tag}' for tag in tags])
    content = f"{content}\n{hashtags}" if tags else content

    # Create binary payload matching exact format from curl
    content_bytes = content.encode()
    content_length = len(content_bytes)
    
    payload = (
        b'\x00\x00\x00\x00' +           # Fixed header
        bytes([content_length + 2]) +    # Total length (content + 2 extra bytes)
        b'\n' +                         # Field separator
        bytes([content_length]) +       # Content length
        content_bytes +                 # The actual content
        b'\x10\x01'                    # Visibility flag (PRIVATE)
    )

    try:
        print(f"Creating memo: {content}")
        # print(f"Payload hex: {payload.hex()}")  # Debug output
        response = requests.post(
            endpoint,
            headers=headers,
            data=payload
        )
        
        if response.status_code == 200:
            print(f"Memo created successfully")
            return True
        else:
            print(f"Failed to create memo: {response.status_code}")
            if response.text:
                print(f"Error details: {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a memo in Memos')
    parser.add_argument('content', help='Content of the memo')
    parser.add_argument('-t', '--tags', help='Comma-separated list of tags (e.g. tag1,tag2,tag3)')
    parser.add_argument('--visibility', choices=['PRIVATE', 'PUBLIC'], default='PRIVATE',
                      help='Visibility of the memo (default: PRIVATE)')
    
    args = parser.parse_args()

    # Get environment variables
    API_BASE_URL = os.getenv("MEMOS_API_URL")
    TOKEN = os.getenv("MEMOS_ACCESS_TOKEN")

    if not API_BASE_URL or not TOKEN:
        print("Please set MEMOS_API_URL and MEMOS_ACCESS_TOKEN environment variables")
        sys.exit(1)

    # Parse tags
    tags = []
    if args.tags:
        tags = [tag.strip() for tag in args.tags.split(',')]

    # Create the memo
    create_memo(API_BASE_URL, TOKEN, args.content, tags, args.visibility)
