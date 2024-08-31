import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from scraping.singlebook import get_info_book
import csv
import os



def find_category(soup):
        url = "https://books.toscrape.com/"
        nmb = 0
        urls_absolutes = []
        aside = soup.find('aside')
        aside_category = aside.find('div', class_="side_categories")
        links = aside_category.find_all('a')
        categories_url =  [category['href'] for category in links[1:]]
        for category_url in  categories_url:
            url_absolut = urljoin(url, category_url)
            urls_absolutes.append(url_absolut)
            nmb += 1

        return urls_absolutes 





def all_book_for_category(urls_all_category):
        os.makedirs("scraping/data/csv", exist_ok=True)
        categories = urls_all_category
        for category_url in categories:
            urls_books_single = []
            while category_url:
                url = category_url
                response = requests.get(url)
                html_response = response.text
                soup = BeautifulSoup(html_response, "html.parser") 
                title_category = soup.find('div', class_="page-header")
                title_book_h = title_category.find('h1').text.strip()
                row = soup.find('ol', class_='row')
                title_h = row.find_all("h3")
                for title in title_h:
                    title_href = title.find('a').get('href')
                    final_url = urljoin(url, title_href )
                    urls_books_single.append(final_url)
                
                next_button = soup.find('li', class_="next")
                if next_button is not None:
                    href_button = next_button.find('a').get('href')
                    category_url = urljoin(url, href_button)
                else:
                    category_url = None       
            with open(f"scraping/data/csv/{title_book_h}.csv", "w", newline="", encoding="utf-8") as fichier_csv:
                writer = csv.writer(fichier_csv, delimiter=',')
                writer.writerow(["Title", "Category", "Rating", "Stock", "Description", "UPC", "Product Type", "Price (excl. tax)", "Price (incl. tax)", "Tax", "Availability", "Number of reviews", "Img url"])
                
                for url_book in urls_books_single:
                    books_all = get_info_book(url_book)
                    # Escribe cada valor del diccionario como una fila
                    writer.writerow(books_all.values())
