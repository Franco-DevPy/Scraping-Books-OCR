import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin

url = 'https://books.toscrape.com/'
response = requests.get(url)

soup =  BeautifulSoup(response.text , 'html.parser')


#pprint(soup.prettify())
#FIND ALL URL CATEGORY 
def find_category(url):
        response = requests.get(url)
        soup =  BeautifulSoup(response.text , 'html.parser')
        if soup is not None:
                urls_absolutes = []
                aside = soup.find('aside')
                aside_category = aside.find('div', class_="side_categories")
                links = aside_category.find_all('a')
                #categories_title =  [category.text.strip() for category in links[1:]]
                categories_url =  [category['href'] for category in links[1:]]
                for category_url in categories_url:
                        url_absolut = urljoin(url, category_url)
                        urls_absolutes.append(url_absolut)

        return urls_absolutes 




#result = find_category(url)
#print(type(result))  
#print("\n".join(result))





"""

PRUEBA function
def find_book_category(url):
    reponse = requests.get(url)
    html_reponse = reponse.text
    soup = BeautifulSoup(html_reponse, "html.parser")
    ol = soup.find('ol', class_="row")
    books = ol.find_all('h3')
    
    if ol is not None:
       for book in books:
        book_title = book.find('a').get('title')
        print(book_title)             
    else: 
        return 'Pas de livre de ce category'   

    #button next
    next_li = soup.find('li', class_="next" )
    url_next = next_li.find('a').get('href')
    url_absolut = urljoin(url, url_next)
        
    if url_absolut is not None:
                reponse_next = requests.get(url_absolut)
                html_reponse_next = reponse_next.text
                soup_next = BeautifulSoup(html_reponse_next, "html.parser")
                ol_next = soup_next.find('ol', class_="row")
                books_next = ol_next.find_all('h3')
                if ol is not None:
                        for book_next in books_next:
                                books_next_title = book_next.find('a').get('title')
                                print(books_next_title)             
                        else: 
                                return 'Pas de livre de ce category'   
    else:
        print('pas de li')           
                        
    
 find_book_category(url)
   
  """




def find_book_category_url(url):
        while url:
            response = requests.get(url)
            html_response = response.text
            soup = BeautifulSoup(html_response, "html.parser")
            
            row = soup.find('ol', class_='row')
            if row is not None:
                title_h = row.find_all("h3")
                for title in title_h:
                    #title_book = title.find('a').get('title')
                    title_book = title.find('a').get('href')
                    title_url = urljoin(url, title_book )
                    print(title_url)
            else:
                print('Pas de livre de ce category')
        

            next_button = soup.find('li', class_="next")
            if next_button is not None:
                href_button = next_button.find('a').get('href')
                url = urljoin(url, href_button)
            else:
                url = None
            
            
            
            
        
        
                
url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"             
find_book_category_url(url)        