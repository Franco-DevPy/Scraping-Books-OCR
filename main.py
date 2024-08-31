#IMPORT
import requests
from bs4 import BeautifulSoup
from scraping.categories import *



url = 'https://books.toscrape.com/'


def main(url):
    
    response = requests.get(url)
    html_response = response.text
    soup = BeautifulSoup(html_response, "html.parser")
    
    
    urls_all_category = find_category(soup)
    all_book_for_category(urls_all_category)   
    

    print('ETL COMPLETED')


if __name__ == "__main__":
    main(url)
