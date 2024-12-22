#!/usr/bin/env python3

from openai import OpenAI
import argparse
import sys
import os

def create_llm_client():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is not set. "
            "Please set it in your .env file or export it in your shell."
        )
    
    client = OpenAI(api_key=api_key)
    return client

def query_llm(prompt, client=None, model="gpt-4o"):
    if client is None:
        client = create_llm_client()
    
    try:
        print(f"Using model: {model}", file=sys.stderr)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error querying LLM: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Query an LLM with a prompt')
    parser.add_argument('--prompt', type=str, help='The prompt to send to the LLM', required=True)
    parser.add_argument('--model', type=str, default="gpt-4o",
                       help='The model to use (default: gpt-4o)')
    args = parser.parse_args()

    client = create_llm_client()
    response = query_llm(args.prompt, client, model=args.model)
    if response:
        print(response)
    else:
        print("Failed to get response from LLM")

if __name__ == "__main__":
    main()
