# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 20:47:27 2022

@author: EdenPereiradaSilva
"""

from bs4 import BeautifulSoup
import requests

is_in_stock = lambda p: 'in stock' if p.text.find('In stock')>0 else 'not in stock'

get_name = lambda item: item.find('img').get('alt')
get_price = lambda item: float(item.find('p',class_='price_color').text[1:])
get_stock = lambda item: is_in_stock(item.find('p',class_='instock availability'))
get_rate = lambda item: name_to_number(item.p.get('class')[1])

def name_to_number(n):
    if n.lower() == "one":
        return 1
    if n.lower() == "two":
        return 2
    if n.lower() == "three":
        return 3
    if n.lower() == "four":
        return 4
    if n.lower() == "five":
        return 5

    return 0

def get_feature(prods, f):
    return [f(p) for p in prods]

def get_prod(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    prods = soup.find_all('article',class_='product_pod')  
    return prods


def get_books(url, category):
    prods = get_prod(url)
    
    names = get_feature(prods, get_name)
    rates = get_feature(prods, get_rate)
    prices = get_feature(prods, get_price)
    stock = get_feature(prods, get_stock)
    
    return [ (n,category,r,p,s) for n,r,p,s in zip(names, rates, prices,stock) ]


