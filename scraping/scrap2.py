import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin
from scraptest import *

url = 'https://books.toscrape.com/'
response = requests.get(url)

soup =  BeautifulSoup(response.text , 'html.parser')


#pprint(soup.prettify())

 
#FIND ALL URL CATEGORY 

def find_category(url):
        response = requests.get(url)
        soup =  BeautifulSoup(response.text , 'html.parser')
        if soup is not None:
                nmb = 0
                urls_absolutes = []
                aside = soup.find('aside')
                aside_category = aside.find('div', class_="side_categories")
                links = aside_category.find_all('a')
                categories_title =  [category.text.strip() for category in links[1:]]
                categories_url =  [category['href'] for category in links[1:]]
                for categorie_title ,category_url in zip(categories_title, categories_url):
                    url_absolut = urljoin(url, category_url)
                    urls_absolutes.append(url_absolut)
                    nmb += 1
                    #print('URLS DES CATEGORIES: ', nmb )        
                    #print(categorie_title, url_absolut)

        return urls_absolutes 


url = 'https://books.toscrape.com/'

urls_all_category = find_category(url)


"""print('\n''Liste Url Category : ')
print(urls_all_category)
print('\n')"""


with open("URL_category.txt", "w", ) as file:
    for url_single in urls_all_category:
        file.write(f"{url_single}\n")




def all_book_for_category():
        categories = urls_all_category
        for category_url in categories:
            # 2. Inicializar la lista de libros
            urls_books_single = []
            # 3. Mientras haya una página
            while category_url:
                # 3a. Buscar los libros en la página actual
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
                
                # 3b. Verificar si hay un botón "next"
                next_button = soup.find('li', class_="next")
                if next_button is not None:
                    href_button = next_button.find('a').get('href')
                    category_url = urljoin(url, href_button)
                else:
                    category_url = None       
            # 4. Guardar los libros en un archivo CSV
            with open(f"data/{title_book_h}.txt", "w") as file:
                for url_book in urls_books_single:
                    books_all = get_info_book(url_book)
                    file.write(f"{books_all}\n")
                    
                            

all_book_for_category()

        
"""

def find_next_button(url):
        next_url = ""
        response = requests.get(url)
        html_response = response.text
        soup = BeautifulSoup(html_response, "html.parser") 
        next_button = soup.find('li', class_="next")
        if next_button is not None:
            href_button = next_button.find('a').get('href')
            next_url = urljoin(url, href_button)
            return next_url
        else:
            url = None
        




#RECUPERATION SINGLE BOOK  URL FOR PAG
def find_book_category_url():
    urls_books_single = []
    for url_single in urls_all_category:
        url = url_single
        nmb = 0
        while url:
            response = requests.get(url)
            html_response = response.text
            soup = BeautifulSoup(html_response, "html.parser") 
            row = soup.find('ol', class_='row')
            if row is not None:
                title_h = row.find_all("h3")
                for title in title_h:
                    title_book = title.find('a').get('title')
                    title_href = title.find('a').get('href')
                    final_url = urljoin(url, title_href )
                    urls_books_single.append(final_url)
                    nmb += 1
                    #print('URL BOOK SINGLE :' , nmb)
                    #print(title_book , final_url)
            else:
                print('Pas de livre de ce category')
        

            next_button = soup.find('li', class_="next")
            if next_button is not None:
                href_button = next_button.find('a').get('href')
                url = urljoin(url, href_button)
            else:
                url = None
        
        # TODO: Écrire fichier de la catégorie
            
    return urls_books_single
            
          
urls_book = find_book_category_url() 



with open("URL_book.txt", "w") as file:
    for url_book in urls_book:
        file.write(f"{url_book}\n")
        
        
 
with open("Detail_single_book.txt", "w" ) as file:
    for url_book in urls_book:
        print(f"Procesando URL: {url_book}")
        books_all = get_info_book(url_book)
        file.write(f"{books_all}\n")
        
        """
        
       
        
        
        
       


                
#url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"  
           

#print('\n''Liste Url category single book : ')
#print(urls_book)

#urls_all_category = find_category(url)

#find_book_category_url(urls_all_category)






"""i = 0

while i < len(urls_book):
    book = get_info_book(urls_book[i])
    i += i
    print(book)
    """
### DEBEMOS BUSCAR LA FORMA DE QUE ITERE Y TRABAJE CON TODOS LOS URL,
# ASI COMBINAMOS LAS FUNCIONES Y CONSEGUIMOS UN RESULTADO COMPLETO DE LOS URL DE LA CATEGORIAS Y DE TODOS LOS LIBROS LOS DETALLES            

""" 
        
for books_detail in urls_book:
    print(f"Procesando URL: {books_detail}")  # Verifica cada URL
    books_all = get_info_book(books_detail)
    print(books_all)

"""