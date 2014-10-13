#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
import os
try:
    fich = open(sys.argv[1], 'r')
except IndexError:
    print "Usage: python karaoke.py file.smil"
parser = make_parser()
cHandler = smallsmilhandler.SmallSMILHandler()
parser.setContentHandler(cHandler)
parser.parse(fich)
ejemplo = cHandler
lista = ejemplo.get_tags()
hayblancos = "" in lista
while hayblancos:
    borrarelem = (lista.index("") - 1)
    del lista[borrarelem]
    del lista[borrarelem]
    hayblancos = "" in lista
pos = []
n = 0
recursos = []
for elem in lista:  # Buscamos la posición de las etiquetas
    if (elem == "root-layout" or elem == "img" or elem == "audio"
       or elem == "textstream"):
        pos.append(n)
    elif elem == "region":  # Para diferenciar entre etiqueta y el atributo
        etq = lista[n+1]
        if (etq == "id" or etq == "top" or etq == "bottom" or etq == "left"
           or etq == "right"):
            pos.append(n)
    if elem == "src":                #lista con los recursos a descargar 
            recursos.append(lista[n+1])
    n = n + 1
for rec in recursos: 
    instruccion = "wget -q " + rec
    #print instruccion 
    os.system("wget -q " + rec)

cadena = ""
n = 0  # Recorre la lista lista
imprimir = False
etiqueta = False
rremoto = ""
rlocal = []
for i in lista:
    if i == "src":  
        rremoto = lista[n+1]
        rlocal = rremoto.split("/") 
        lista[n+1] = rlocal[-1]         
    if n == len(lista)-1 and n != 0:
        imprimir = True
    for num in pos:
        if (num-1) == n and n != 0:
            imprimir = True
        elif num == n:  # Para tratar a region como atributo o etiqueta
            etiqueta = True
    if (i == "width" or i == "heigth" or i == "background-color" or i ==
       "id" or i == "top" or i == "bottom" or i == "left" or i == "right"
       or i == "src" or i == "begin" or i == "dur"):  # Todos menos region
        cadena = cadena + "\t"
        cadena = cadena + i
        cadena = cadena + "="
    elif i == "region" and not etiqueta:
        cadena = cadena + "\t"
        cadena = cadena + i
        cadena = cadena + "="
    else:
        cadena = cadena + i

    if imprimir:
        print cadena
        cadena = ""
        imprimir = False
    etiqueta = False
    n = n + 1

