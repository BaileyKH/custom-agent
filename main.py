import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="AI-Agent")
parser.add_argument("user_prompt", type=str, help="User Prompt")
args = parser.parse_args()

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = args.user_prompt,
)



def main():
    meta_data = response.usage_metadata 
    if meta_data == None:
        raise RuntimeError("Error: Failed API Request")
    
    print(f'Prompt tokens: {meta_data.prompt_token_count}\nResponse tokens: {meta_data.candidates_token_count}')
    print(response.text)


if __name__ == "__main__":
    main()
