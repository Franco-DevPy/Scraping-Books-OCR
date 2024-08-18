#SCRAP SINGLE PAG 

from bs4 import BeautifulSoup
import requests
import csv


"""
URL_BASE = "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
reponse = requests.get(URL_BASE)
html_reponse = reponse.text

soup = BeautifulSoup(html_reponse, "html.parser")
"""

        
        
        
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
        description_text = description_select.get_text(strip=True)
        return description_text
        


def find_img(soup):
    img_book = soup.select_one('#product_gallery img')
    if img_book is not None :
        img_src = img_book.get('src')
        return img_src
    else :
        return 'Image indisponible' 
        


#url = "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"

def get_info_book(url):
    reponse = requests.get(url)
    html_reponse = reponse.text
    soup = BeautifulSoup(html_reponse, "html.parser")
    # TODO: Récupérer toutes les infos
    return {
        'Title': find_title(soup),
        #'Category': find_category(soup),
        #'Rating': findRating(soup),
        #'Stock' : find_stock(soup),
        #'Description': description_book(soup),
        #**find_table(soup),
        #'Img url': find_img(soup),
    
    }
    
    
#print(get_info_book(url))
    
    
    
"""    
    
url = 'https://books.toscrape.com/'
#RECUPERATION DE URL DES LES CATEGORIES
def category_book_url(url):
    reponse = requests.get(url)
    html_reponse = reponse.text
    soup = BeautifulSoup(html_reponse, "html.parser")
    url = soup.select_one('ul.nav-list > li > ul ')
    category_books =  {}
    if url is not None:
        url_li = url.find_all('li')
        for url_single in url_li:
            url_category = url_single.find('a')['href']
            url_nom = url_single.get_text(strip=True)
            if url_category is not None and url_nom is not None:
                 category_books[url_nom] = url_category
            else: 
                return 'Not Category LI'
        return category_books
    else:
        print('Pas de catégorie')
        

print(type(category_book_url()))
"""
















"""

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

"""

"""

category_book_url(url)


def get_category_books_urls(category_url):
  
    
    print("Getting books urls ", category_url)
    

    # TODO: Récupérer la dynamiquement la liste de tous les livres

    return ["https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html", "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"]

"""

"""
def get_category_books_info(category_url):
    print("Scraping category ", category_url)
    books_info = []

    for book_url in get_category_books_urls(category_url):
       print("Scraping ", book_url)
       books_info.append(get_info_book(book_url))
    
    return books_info


print(get_category_books_info(category_url)) 
"""








       
"""
with open('infos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    if soup:
        writer.writerow(["Title:", title_final])
        writer.writerow(["Rating: ", final_rating])
        writer.writerow(["Stock: ", final_stock])
        writer.writerow(["Description: ", description_text])
        writer.writerow(["Product Information: "])
        
        if table_info is not None:      
            infos_product = table_info.find_all('tr')
            for row in infos_product:
                info_title = row.find('th').get_text(strip=True)
                info_detail = row.find('td').get_text(strip=True)
                writer.writerow([info_title, info_detail])
        else:
            writer.writerow(["Not detail product"])
    else:
        writer.writerow(["Pas de Book"])

"""