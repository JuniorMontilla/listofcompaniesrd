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
<<<<<<< HEAD
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
=======
        for numberofregisters in range(5068):
                data = urlencode({"st":argv[1], "page": numberofregisters})
                reading = urlopen("http://www.camarasantodomingo.do/red-empresarial/busqueda?%s" % data)
                soup = BeautifulSoup(reading)
                for elements in soup.find_all("div", class_="__info"):
                         item = elements.get_text()
                         persistense = open("listofcompanies.txt", 'a')
                         persistense.write(item.encode('utf-8'))
                persistense.close()
>>>>>>> 20154d71723496a71c720e9f97611f1b06fa1a30
