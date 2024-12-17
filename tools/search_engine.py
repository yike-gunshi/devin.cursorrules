#!/usr/bin/env /workspace/tmp_windsurf/py310/bin/python3

import argparse
import sys
from duckduckgo_search import DDGS

def search(query, max_results=5):
    """
    Search using DuckDuckGo and return results with URLs and text snippets.
    
    Args:
        query (str): Search query
        max_results (int): Maximum number of results to return
    """
    try:
        print(f"DEBUG: Searching for query: {query}", file=sys.stderr)
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
            
        if not results:
            print("DEBUG: No results found", file=sys.stderr)
            return
        
        print(f"DEBUG: Found {len(results)} results", file=sys.stderr)
        
        for i, r in enumerate(results, 1):
            print(f"\n=== Result {i} ===")
            print(f"URL: {r.get('href', 'N/A')}")
            print(f"Title: {r.get('title', 'N/A')}")
            print(f"Snippet: {r.get('body', 'N/A')}")
            
    except Exception as e:
        print(f"ERROR: An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Search using DuckDuckGo API")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--max-results", type=int, default=5,
                      help="Maximum number of results (default: 5)")
    
    args = parser.parse_args()
    search(args.query, args.max_results)

if __name__ == "__main__":
    main() 