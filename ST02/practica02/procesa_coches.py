#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

#python UnicodeEncodeError: 'ascii' codec can't encode character in position : ordinal not in range(128)

import sys , os , shutil
import argparse
import xml.etree.ElementTree as ET

def printAttr (attr) :
    for x in attr.keys() :
        print u"Attribute   : ",
        print x  ,
        print u"  Value : "  ,
        print attr[x]
        #indice = 0
        #while indice < len(attr[x]) :
        #    letra = attr[x][indice]
        #    print unicode(letra)
        #    indice = indice + 1

def formatfile (tag  , attr , text) :
        print u"Etiqueta : " , tag
        #printAttr(attr)
        print attr
        if text != None :
            print u"Texto : " , text


def getXML(filename) :
    root = ET.ElementTree(file=filename).getroot()
    for elemento in root.iter() :
        formatfile(elemento.tag , elemento.attrib , elemento.text)


def main() :
    usage = u"%prog [OPCIONES] input output if not arguments we read stdin"
    parser = argparse.ArgumentParser(usage)

    parser.add_argument("-i" , "--input"  , action="store" ,     dest="input"  , help = "xml file to format")
    arguments = parser.parse_args()

    if arguments.input == None :
        print u"read from stdin"
    else :
        print u"reading from file " + arguments.input
        if not os.path.exists(arguments.input) :
            print u"File : " + arguments.input + u" not exist."
            raise SystemExit
        getXML(arguments.input)


if __name__ == "__main__":
        main()
