# scraper.py
import urllib.request
import re

def scrape_website(url):
    try:
        # Open the URL and read the content
        response = urllib.request.urlopen(url)
        html_content = response.read().decode('utf-8')
        
        # Remove HTML tags and clean the text
        clean_text = re.sub('<[^<]+?>', ' ', html_content)
        clean_text = re.sub('\s+', ' ', clean_text)
        
        # Remove special characters and extra whitespace
        clean_text = ' '.join(clean_text.split())
        
        # Extract meaningful content (first 5000 characters for demonstration)
        return clean_text[:5000]
        
    except Exception as e:
        print(f"Error scraping website: {str(e)}")
        return ""
