from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import csv
import re

"""
URL_BASE = "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
reponse = requests.get(URL_BASE)
html_reponse = reponse.text

soup = BeautifulSoup(html_reponse, "html.parser")
"""

        
#RECUPERATION SINGLE BOOK        
        
def find_title(soup):
    title = soup.find('h1')
    if title:
        return title.get_text(strip=True)
    else:
        print('No title found')
        return 'Not Title'



def find_category(soup):
        category = soup.select('ul.breadcrumb li')[2]
        if category is not None:
            return category.get_text(strip=True)
        else:
            return 'Not Category Book'
       
    

def find_stock(soup):
    stock = soup.select_one('div.product_main > p.instock')
    if stock is not None :
        stock_final = stock.get_text(strip=True)
        return stock_final
    else :
        return "Stock Indisponible"
    
    
    

def findRating(soup):
    rating = soup.select_one('p.star-rating') 
    # Verifica si el elemento existe
    if rating is None:
        return 'No hay rating'
    else:
        rating_class = rating.get('class')
        match rating_class :
                case ['star-rating', 'One']:
                    return 'Rating is 1/5'
                case ['star-rating', 'Two']:
                    return 'Rating is 2/5'
                case ['star-rating', 'Three']:
                    return 'Rating is 3/5'
                case ['star-rating', 'Four']:
                    return 'Rating is 4/5'
                case ['star-rating', 'Five']:
                    return 'Rating is 5/5'
                case _:
                    return'Not rating'
           
           
def find_table(soup):
        table_data = {}
        table_info = soup.find('table', class_="table")
        if table_info is not None:
            table_detail = table_info.find_all('tr')
            for tr in table_detail:
                th_detail = tr.find('th')
                td_detail = tr.find('td')
                if th_detail is not None and td_detail is not None:
                    table_data[th_detail.get_text(strip=True)] = td_detail.get_text(strip=True)
                else:
                    return 'Not Raw'            
            return table_data 
        else:
            return 'Not Table'
    

def description_book(soup):
        description_select = soup.select_one('article.product_page > p')
        if  description_select is not None:
            description_text = description_select.get_text(strip=True)
            return description_text
        else:
            return 'No description'



"""
def find_img(soup):
    url_base = "https://books.toscrape.com/"
    title = soup.find('h1').get_text(strip=True)
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    img_book = soup.select_one('#product_gallery img')
    img_book = soup.select_one('#product_gallery img')
    if img_book is not None :
        img_src = img_book.get('src')
        url_img_aboslut = urljoin(url_base, img_src)
        url_content = requests.get(url_img_aboslut)
        with open(f"scraping/data/img/{title}.jpg", "wb") as fichie_img:
            fichie_img.write(url_content.content)
            return url_img_aboslut
    else :
        return 'Image indisponible' 
        """



# RETURN SINGLE BOOK
def get_info_book(url):
    reponse = requests.get(url)
    html_reponse = reponse.text
    soup = BeautifulSoup(html_reponse, "html.parser")
    return {
        'Title': find_title(soup),
        'Category': find_category(soup),
        'Rating': findRating(soup),
        'Stock' : find_stock(soup),
        'Description': description_book(soup),
        **find_table(soup),
        #'Img url': find_img(soup),
    
    }
    