#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
try:
    fich = open(sys.argv[1], 'r')

    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    ejemplo = cHandler
    lista = ejemplo.get_tags()
    posregion = 7  #guardamos la pos de la etiqueta region para diferenciar mas adelante
    hayblancos = "" in lista
    while hayblancos:
        borrarelem = (lista.index("") - 1)
        del lista[borrarelem]
        del lista[borrarelem]
        hayblancos = "" in lista
    pos = []
    n = 0
    for e in lista:   #Buscamos la posición de las etiquetas
        if e == "root-layout" or e == "img" or e == "audio" or e =="textstream":
            pos.append(n)
        elif e == "region": #En region debemos diferenciar entre etiqueta y atributo
            etq = lista[n+1]
            if etq == "id" or etq == "top" or etq == "bottom" or etq == "left" or etq == "right":
                pos.append(n)
        n = n + 1
    print len(lista)
    cadena = ""
    n = 0 #recorre la lista lista 
    imprimir = False
    etiqueta = False
    for i in lista: 
        if n == len(lista)-1 and n != 0:
           imprimir = True
        for num in pos : 
            if (num-1) == n and n!= 0:
                imprimir = True
            elif num == n:     #para tratar a region como atributo o etiqueta
                etiqueta = True
        if (i == "width" or i == "heigth" or i == "background-color" or i == "id"
            or i == "top" or i == "bottom" or i == "left" or i == "right" 
            or i == "src" or i == "begin" or i == "dur"):  #todos los atributos excepto region
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
except IndexError:
    print "Usage: python karaoke.py file.smil"
