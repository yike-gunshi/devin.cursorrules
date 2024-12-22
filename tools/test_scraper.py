from web_scraper import scrape_urls

def test_scraper():
    # Test URLs - using some stable websites
    test_urls = [
        "https://example.com",
        "https://httpbin.org/html",
        "https://playwright.dev"
    ]
    
    try:
        # Test with multiple URLs
        results = scrape_urls(test_urls, max_concurrent=2)
        print("\nScraping Results:")
        for url, content in results.items():
            print(f"\nURL: {url}")
            print(f"Content length: {len(content)} characters")
            print(f"First 200 characters: {content[:200]}...")
            
        return True
    except Exception as e:
        print(f"Error during scraping: {str(e)}")
        return False

if __name__ == "__main__":
    print("Starting web scraper test...")
    success = test_scraper()
    print(f"\nTest {'succeeded' if success else 'failed'}")
