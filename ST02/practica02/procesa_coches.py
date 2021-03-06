#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys , os , shutil
import argparse
import xml.etree.ElementTree as ET

MAX = 12

def printspaces (lenword) :
    for x in range(MAX - lenword) :
        print '',

def formatfile (element , attr , text) :
    for x in attr.keys() :
        print attr[x].upper() ,
        printspaces(len(attr[x]))
    print


def prhead () :
    print "Matricula    " + "Modelo       " + "Marca       "
    print "---------" + 8*'-' + ------ + 8*'-' + "----------"


def getXML(filename) :

    try :
        if filename != None :
            root = ET.ElementTree(file=filename).getroot()
        else :
            root = ET.ElementTree(file=sys.stdin).getroot()

        prhead()
        for elemento in root.iter() :
            if root.tag != elemento.tag :
                formatfile(elemento.tag , elemento.attrib , elemento.text)

    except ET.ParseError :
        sys.stderr.write("Error process file xml not well formed file xml" + '\n')
        raise SystemExit

def main() :
    usage = u"%prog [OPCIONES] input output if not arguments we read stdin"
    parser = argparse.ArgumentParser(usage)

    parser.add_argument("-i" , "--input"  , action="store" , dest="input" \
                            , help = "xml file to format")
    arguments = parser.parse_args()

    if arguments.input == None :
        getXML(None)
    else :

        if not os.path.exists(arguments.input) :
            print u"File : " + arguments.input + u" not exist."
            raise SystemExit

        getXML(arguments.input)


if __name__ == "__main__":
        main()
