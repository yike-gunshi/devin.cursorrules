#!/usr/bin/env python3

import google.generativeai as genai
import argparse
import sys
import os

def create_llm_client():
    api_key = 'AIzaSyB31Okz3O878obIYvKM1ssKkFATI1r9-eo'
    genai.configure(api_key=api_key)
    return genai

def query_llm(prompt, client=None, model="gemini-pro"):
    if client is None:
        client = create_llm_client()
    
    try:
        print(f"Using model: {model}", file=sys.stderr)
        model = client.GenerativeModel(model)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error querying LLM: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Query an LLM with a prompt')
    parser.add_argument('--prompt', type=str, help='The prompt to send to the LLM', required=True)
    parser.add_argument('--model', type=str, default="gemini-pro",
                       help='The model to use (default: gemini-pro)')
    args = parser.parse_args()

    client = create_llm_client()
    response = query_llm(args.prompt, client, model=args.model)
    if response:
        print(response)
    else:
        print("Failed to get response from LLM")

if __name__ == "__main__":
    main()
