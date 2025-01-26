import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Define headers to avoid request blocking
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Send a GET request to the URL with headers
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()  # This will raise an HTTPError if the status code isn't 200
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract and print the title of the webpage
        title = soup.title.string if soup.title else 'No title found'
        print("Title: ", title)
        
        # Example: Scraping all the <a> tags from the page
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))
        
        # Example: Scraping text from <p> tags
        print("\nParagraphs:")
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            print(paragraph.get_text())
            
        # Example: Scraping heading
        print("\nHeadings:")
        headings = soup.find_all('h1')
        for heading in headings:
            print(heading.get_text())
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage:
url = input("Enter the URL of the website you want to scrape: ")
scrape_website(url)
