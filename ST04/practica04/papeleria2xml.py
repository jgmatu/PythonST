#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

#01234567890123456789012345678901234567890123456789012345678901234567890123456789

import xml.etree.cElementTree as ET
import sys
import json
import xmlpp

def putElement (root , element) :
    elemento = ET.SubElement(root , u"articulo")
    keys = element.keys()

    # XML Element attrs.
    atributos = {}
    for x in keys :
        atributos[unicode(x)] = unicode(element[x])
        elemento.attrib = atributos

def main () :

    # Read file Json and get a python data structure.
    data = sys.stdin.read()
    jsondata  = json.loads(data)

    # Root Element my document xml.
    root = ET.Element("papeleria")

    # Get Elements of XML.
    for x in range(len(jsondata)) :
        putElement(root , jsondata[x])

    # Print XML Format.
    xmlData = ET.tostring(root , encoding="utf-8" , method="xml")
    xmlpp.pprint(xmlData , sys.stdout , 4 , 80)


if __name__ == "__main__" :
    main()
