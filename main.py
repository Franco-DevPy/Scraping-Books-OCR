#IMPORT
import requests
from bs4 import BeautifulSoup
from scraping.categories import *



url = 'https://books.toscrape.com/'


def main(url):
    
    response = requests.get(url)
    html_response = response.text
    soup = BeautifulSoup(html_response, "html.parser")
    # Get all book categories
    urls_all_category = find_category(soup)
    print(urls_all_category)
    # Get all book categories
    all_book_for_category(urls_all_category)   
    




#permite que un archivo funcione tanto como un script 
# ejecutable como un módulo importable sin conflictos.
if __name__ == "__main__":
    main(url)
