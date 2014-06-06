#!usr/bin/env python
# -*- coding: utf-8 -*-
#python version 2.7.6
#by Junior Montilla

from urllib import urlopen, urlencode
from bs4 import BeautifulSoup
from sys import argv
import sqlite3

database = sqlite3.connect('companies.db')
cursor = database.cursor()

if len(argv) > 1:
    for pages in range(int(argv[1])):
        data = urlencode({'st':'advanced', 'page': pages})
        output = urlopen('http://www.camarasantodomingo.do/red-empresarial/busqueda?%s' % data)
        reading = output.read()
        soup = BeautifulSoup(reading)
        for elements in soup.find_all('div', class_='__info'):
            data = elements.find_all(['h3','h4','p'])

            datatostorage = ( 
                               data[0].get_text(),
                               data[1].get_text(),
                               data[2].get_text(),
                               data[3].get_text(),
                               data[4].get_text(),
                                
                                 )
            print datatostorage
            cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Companies
                   (nameofcompany text, place text, phone text, email text, website text)
                         ''')

            cursor.execute('INSERT INTO Companies VALUES(?,?,?,?,?)', datatostorage)
        database.commit()
    database.close()
