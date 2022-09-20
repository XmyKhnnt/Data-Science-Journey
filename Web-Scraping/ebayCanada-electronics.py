# Extract data ffrom https://www.newegg.ca/
# Brand, Gadget Name, Price, Shipping fee
# Needed Modules

from bs4 import BeautifulSoup
import numpy as np
from pyparsing import Regex
import requests
import pandas as pd 
import os 


# Making request 
def extract(page):
    url = f"https://www.newegg.ca/p/pl?N=100165973%2050001077%2050105360%2050001759%2050015388%2050118945%2050096270&page={page}"
    
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'xml')

    return soup



def transform(soup):

    phones = soup.find_all('div', class_ = 'item-cell')

    for item in phones:

        brand = item.find('div', class_ = 'item-branding')
        try:
            brands = brand.a.img['title']
        except:
            brands = 'unspecified'

        item_name = item.find('a', class_ = 'item-title').text.strip()
        
        price = item.find('li', class_ ='price-current' ).text
       
        shipping = item.find('li', class_ = 'price-ship').text

        
    
        items = {
            'Brand': brands,
            'Product Name': item_name,
            'Price': price,
            'Shipping Fee': shipping
        }

        products.append(items)

products = []



for i in range(1, 51):
    print(f'Getting page {i}')
    x = extract(i)
    transform(x)



df = pd.DataFrame(products)
print(df)
path = r'D:\Web Development\test 2\Web Scraping Porjects\Data'



df.to_csv(os.path.join(path, 'cp-products - list.csv'))
