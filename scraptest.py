from bs4 import BeautifulSoup
import requests
import csv


# Versiones
import bs4 # Solo para el chequeo
print("Versión de BeautifulSoup:",bs4.__version__)
print("Versión de requests:", requests.__version__)


# Empezamos el scraping

# 1. Obtener el HTML

URL_BASE = 'https://books.toscrape.com/catalogue/psycho-sanitarium-psycho-15_628/index.html'
reponse = requests.get(URL_BASE)
html_reponse = reponse.text

# "Parsear" le HTML
soup = BeautifulSoup(html_reponse, "html.parser")

#Print all HTML 
#--------------print(soup)

#On utiliser le methode find() pour trouver les etiquette html

Title_Book = soup.find('h1')
print(Title_Book.text)

#On utilise select pour trover l'element correct a l'interieur d'un element avec classe
description_book = soup.select('article.product_page > p')

print(type(description_book))



img_book = soup.select_one('div.product_main > p.instock')

stock = soup.select_one('p', class_ = "instock availability")



if stock :
    print(stock.get_text(strip=True))
else :
    print("Stock Indisponible")

table_info = soup.select_one('table.table')

infos_product = table_info.find_all('tr')

rating = soup.select_one('p', class_ = 'star-rating One') 

match rating :
    case 'star-rating One':
        print('Rating is 1/5')
    case 'star-rating Two':
        print('Rating is 1/5')
    case 'star-rating Three':
        print('Rating is 1/5')
    case 'star-rating Four':
        print('Rating is 1/5')
    case 'star-rating Five':
        print('Rating is 1/5')
    case _:
        print('Not rating')  
    

  

        
        
with open('infos.csv', 'w') as file:
   for row in infos_product:
    detail_title = row.find('th')
    detail_info = row.find('td')
    
    if detail_title and detail_info:
        file.write("\n" + Title_Book.get_text(strip=True))
        file.write("\n" + description_book[0].get_text(strip=True))
        file.write("\n" + rating.get_text(strip=True))
        file.write("\n" + stock.get_text(strip=True))
        file.write("\n" + "Product Information : ")
        file.write('\n' + "Espec is : " + detail_title.get_text(strip=True) + " : " + detail_info.get_text(strip=True))
        print('\n' "Espec is : " + detail_title.get_text(strip=True) + " : " + detail_info.get_text(strip=True))
    else:
        file.write("Pas de detail")
    





       





# iterar les items du tableau
#for info_product in infos_product:
#    print("\n This is .. " + str(info_product.get_text(strip=True)))
#

### NO SE CONCATENA ASI CON ELEMENTOS SOUP ###  detail_all  = detail_title + "" + detail_info




