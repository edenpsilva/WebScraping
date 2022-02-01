# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 11:54:45 2022

@author: EdenPereiradaSilva
"""

from util import get_books
from selenium import webdriver

import pandas as pd

import sqlite3 as conector

books = []

url = 'http://books.toscrape.com/index.html'
navegador = webdriver.Chrome()
navegador.maximize_window()
try:
    navegador.get(url)

    element = navegador.find_element('xpath','//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul')
    all_options = element.find_elements('tag name', "a")
    category = [(e.text, e.get_attribute('href')) for e in all_options]
    
    for c, url in category: 
        try:
            navegador.get(url)
        except:
            continue
        while url!='':
            books += get_books(url,c)
            try:              
                n = navegador.find_element('class name', 'next')
                n = n.find_element('tag name', 'a')
                url = n.get_attribute('href')
                n.click()
    
            except:
                url =''
                pass
            
except:
    print("não foi possível atualizar o dados") 
#saving in csv
df = pd.DataFrame(data=books, columns=['name', 'category', 'star rating', 'price', 'stock status'])
df.to_csv('books.csv', index=False)      


#saving direct in the database
connection = conector.connect('books.db')

cursor = connection.cursor()

command = """
                insert into BOOK(BO_NM_TITLE,
                                    BO_DS_CATEGORY, 
                                    BO_NR_STARS,
                                    BO_NR_PRICE, 
                                    BO_IN_STOCK) VALUES(?,?,?,?,?);
"""
for b in books:
    cursor.execute((command),b)

connection.commit()
cursor.close()
connection.close() 
        