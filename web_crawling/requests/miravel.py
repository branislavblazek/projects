# -*- coding: utf-8 -*-

import csv
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

def get_content_url(base_url):
    content = requests.get(base_url).content
    soup = BeautifulSoup(content, "html.parser")

    more_products_link = soup.find("a", id='moreProductPage')
    url = unquote(more_products_link.get('href'))
    total = url[url.rindex("/") + 1:]
    return "{0}?p={1}/{1}".format(base_url, total)

def extract_product(product):
        product_link = product.find('a')
        name = product_link.text
        url = product_link.get('href')
        price = product.find('div', 'price').text.strip("\n")
        return [name, url, price]

def main():
    base_url = "http://www.miravel.cz/lubrikacni-gely/"

    content_url = get_content_url(base_url)
    # put parameters into url
    content = requests.get(content_url).content
    soup = BeautifulSoup(content, "html.parser")
    products = soup.find_all('div', 'productPreview')
    
    with open("output.csv", "w+", newline='') as file:
        file_writer = csv.writer(file)
        file_writer.writerow(["Nazov", "Url", "Cena"])
        for product in products:
            data = extract_product(product)
            file_writer.writerow(data)
        

main()