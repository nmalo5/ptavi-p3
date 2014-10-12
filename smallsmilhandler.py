#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.width = ""
        self.heigth = ""
        self. background_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.lista = []

    def startElement(self, name, attrs):

        if name == "root-layout":
            self.width = attrs.get("width", "")
            self.height = attrs.get("height", "")
            self.background_color = attrs.get("background-color", "")
            self.lista = (self.lista + ["root-layout", "width", self.width,
                          "heigth", self.height, "background-color",
                          self.background_color])
        elif name == "region":
            self.id = attrs.get("id", "")
            self.top = attrs.get("top", "")
            self.bottom = attrs.get("bottom", "")
            self.left = attrs.get("left", "")
            self.rigth = attrs.get("rigth", "")
            self.lista = (self.lista + ["region", "id", self.id, "top",
                          self.top, "bottom", self.bottom, "left", self.left,
                          "rigth", self.rigth])
        elif name == "img":
            self.src = attrs.get("src", "")
            self.region = attrs.get("region", "")
            self.begin = attrs.get("begin", "")
            self.dur = attrs.get("dur", "")
            self.lista = (self.lista + ["img", "src", self.src, "region",
                          self.region, "begin", self.begin, "dur", self.dur])
        elif name == "audio":
            self.src = attrs.get("src", "")
            self.begin = attrs.get("begin", "")
            self.dur = attrs.get("dur", "")
            self.lista = (self.lista + ["audio", "src", self.src, "begin",
                          self.begin, "dur", self.dur])
        elif name == "textstream":
            self.src = attrs.get("src", "")
            self.region = attrs.get("region", "")
            self.lista = (self.lista + ["textstream", "src", self.src,
                          "region", self.region])

    def get_tags(self):
        return self.lista
#if __name__ == "__main__":

 #   parser = make_parser()
   # cHandler = SmallSMILHandler()
    #parser.setContentHandler(cHandler)
    #parser.parse(open('karaoke.smil'))
    #ejemplo = cHandler
    #print ejemplo.get_tags()
