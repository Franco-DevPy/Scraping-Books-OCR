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

title_Book = soup.find('h1')

title_final = title_Book.get_text()
#print(Title_Book.text)

#On utilise select pour trover l'element correct a l'interieur d'un element avec classe
description_book = soup.select_one('article.product_page > p')

description_text = description_book.get_text(strip=True)
#print(type(description_book))





def find_img():
    img_book = soup.select_one('#product_gallery img')
    if img_book is not None :
        img_src = img_book.get('src')
        return img_src
    else :
        return 'Image indisponible' 
        

img_find = find_img()        
#.get('attribute')

#Recuperation du stock
def find_stock():
    stock = soup.select_one('div.product_main > p.instock')
    if stock is not None :
        stock_final = stock.get_text(strip=True)
        return stock_final
    else :
        return "Stock Indisponible"
    
    
final_stock = find_stock()
    

def findRating():
    rating = soup.select_one('p.star-rating') 
    # Verifica si el elemento existe
    if rating is None:
        return 'No hay rating'
        
    rating_class = rating.get('class')
# rating_class será una lista como ['star-rating', 'One']
#   print("Clases recuperadas:", rating_class)
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
           

final_rating = findRating()


#objeto tag
table_info = soup.find('table', class_="table")

#lista de objetos
infos_product = table_info.find_all('tr')


def table_info():
for row in infos_product:
    info_title = row.find('th')
    info_detail = row.find('td')
    print(f'{info_title.get_text(strip=True)} :  {info_detail.get_text(strip=True)}')   
    




print('\n' + '\n' + '\n' + '\n' +  title_final)
print('\n' + final_rating)
print('\n' + description_text)
print('\n' + final_stock + '\n')

print(str(img_find))


with open('infos.csv', 'w') as file:
    if soup:
        file.write("\n" + title_final.get_text(strip=True))
        file.write("\n" + final_rating)  
        file.write("\n" + final_stock.get_text(strip=True))
        file.write("\n" + description_book[0].get_text(strip=True))
        file.write("\n" + "Product Information : ")
        file.write('\n' + "Espec is : " + detail_title.get_text(strip=True) + " : " + detail_info.get_text(strip=True))
    else:
        file.write("Pas de detail")


print(f'\n\n\n\n' + str(final_rating))





       





# iterar les items du tableau
#for info_product in infos_product:
#    print("\n This is .. " + str(info_product.get_text(strip=True)))
#

### NO SE CONCATENA ASI CON ELEMENTOS SOUP ###  detail_all  = detail_title + "" + detail_info




