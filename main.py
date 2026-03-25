import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    parser = argparse.ArgumentParser(description="AI-Agent")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")
    
    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    generate_content(client, messages, args)


def generate_content(client, messages, args):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages,
    )

    meta_data = response.usage_metadata 

    if meta_data == None:
        raise RuntimeError("Error: Failed API Request")
    
    if args.verbose:
        print(f'User prompt: {args.user_prompt}')
        print(f'Prompt tokens: {meta_data.prompt_token_count}')
        print(f'Response tokens: {meta_data.candidates_token_count}')

    print(f'Response: {response.text}')


if __name__ == "__main__":
    main()
