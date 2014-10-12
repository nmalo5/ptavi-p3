#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
    
fich = open(sys.argv[1], 'r')

parser = make_parser()
cHandler = smallsmilhandler.SmallSMILHandler()
parser.setContentHandler(cHandler)
parser.parse(open('karaoke.smil'))
ejemplo = cHandler
lista = ejemplo.get_tags()
hayblancos = "" in lista
while hayblancos:
    borrarelem = (lista.index("") - 1)
    del lista[borrarelem]
    del lista[borrarelem]
    hayblancos = ""in lista
pos = []
n = 0
for e in lista:   #Buscamos la posición de las etiquetas
    if e == "root-layout" or e == "region" or e == "img" or e == "audio" or e =="textstream":
        pos.append(n)
    n = n + 1
#print pos    
m = 0 #recorre la lista pos
cadena = ""
n = 0 #recorre la lista lista 
for elem in lista:
    cadena = cadena + elem    
    for num in pos:
        if n == (num-1):
            print cadena
            cadena = ""
    n = n + 1

