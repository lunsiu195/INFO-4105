# searchapp/crawler.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .models import CrawledPage

def crawl_page(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract relevant information from the page
        # In this example, we'll just print the titles of the articles
        titles = soup.find_all('h2', {'class': 'mp-h2'})
        for title in titles:
            print(title.text.strip())
            
        # Find and follow links to other pages
        links = soup.find_all('a', href=True)
        for link in links:
            absolute_url = urljoin(url, link['href'])
            crawl_page(absolute_url)
            
    except Exception as e:
        print(f"Error crawling {url}: {e}")
