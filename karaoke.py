#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
import os


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):
    def __init__(self, fich):
        smallsmilhandler.SmallSMILHandler.__init__(self)
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fich, 'r'))
        self.lista = cHandler.get_tags()

    def __str__(self):
        hayblancos = "" in self.lista
        while hayblancos:
            borrarelem = (self.lista.index("") - 1)
            del self.lista[borrarelem]
            del self.lista[borrarelem]
            hayblancos = "" in self.lista
        self.pos = []
        n = 0

        for elem in self.lista:  # Buscamos la self.posición de las etiquetas
            if (elem == "root-layout" or elem == "img" or elem == "audio"
               or elem == "textstream"):
                self.pos.append(n)
            elif elem == "region":  # diferenciar entre etiqueta y atributo
                etq = self.lista[n+1]
                if (etq == "id" or etq == "top" or etq == "bottom" or
                   etq == "left" or etq == "right"):
                    self.pos.append(n)
            n = n + 1

        self.cadena = ""
        n = 0  # Recorre la self.lista self.lista
        imprimir = False
        etiqueta = False
        rremoto = ""
        rlocal = []
        for i in self.lista:
            if n == len(self.lista)-1 and n != 0:
                imprimir = True
            for num in self.pos:
                if (num-1) == n and n != 0:
                    imprimir = True
                elif num == n:  # Para tratar a region como atributo o etiqueta
                    etiqueta = True
            if (i == "width" or i == "heigth" or i == "background-color" or
                i == "id" or i == "top" or i == "bottom" or i == "left" or
               i == "right" or i == "src" or i == "begin" or i == "dur"):
                self.cadena = self.cadena + "\t"
                self.cadena = self.cadena + i
                self.cadena = self.cadena + "="
            elif i == "region" and not etiqueta:
                self.cadena = self.cadena + "\t"
                self.cadena = self.cadena + i
                self.cadena = self.cadena + "="
            else:
                self.cadena = self.cadena + i

            if imprimir:
                print self.cadena
                self.cadena = ""
                imprimir = False
            etiqueta = False
            n = n + 1
        return self.cadena

    def do_local(self):
        recursos = []
        n = 0
        for elem in self.lista:
            if elem == "src":        # lista con los recursos a descargar
                    recursos.append(self.lista[n+1])
            n = n + 1
        for rec in recursos:
            instruccion = "wget -q " + rec
            os.system("wget -q " + rec)
        n = 0

        for i in self.lista:
            if i == "src":
                rremoto = self.lista[n+1]
                rlocal = rremoto.split("/")
                self.lista[n+1] = rlocal[-1]
            n = n + 1

try:
    fich = sys.argv[1]
    kl = KaraokeLocal(fich)
    print kl
    kl.do_local()
    print kl

except IndexError:
    print "Usage: python karaoke.py file.smil"
