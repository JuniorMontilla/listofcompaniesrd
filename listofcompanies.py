#!usr/bin/env python
# -*- coding: utf-8 -*-
#python version 2.7.6
#by Junior Montilla

from urllib import urlopen, urlencode
from bs4 import BeautifulSoup
from sys import argv

if len(argv) > 1:
        for numberofregisters in range(5068):
                data = urlencode({"st":argv[1], "page": numberofregisters})
                reading = urlopen("http://www.camarasantodomingo.do/red-empresarial/busqueda?%s" % data)
                soup = BeautifulSoup(reading)
                for elements in soup.find_all("div", class_="__info"):
                         item = elements.get_text()
                         persistense = open("listofcompanies.txt", 'a')
                         persistense.write(item.encode('utf-8'))
                persistense.close()
