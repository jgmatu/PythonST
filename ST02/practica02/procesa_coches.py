#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

#python UnicodeEncodeError: 'ascii' codec can't encode character in position : ordinal not in range(128)

import sys , os , shutil
import argparse
import xml.etree.ElementTree as ET

def valuelenmax (attrs) :
    listkeys = attrs.keys()
    listkeys.sort()
    maxval = 0
    for x  in listkeys :
        if len(attrs[x]) > maxval :
            maxval = len(attrs[x])
    return maxval

def printmargen (margen) :
    for x in range(margen) :
        print '' ,

def formatWhites (attrval , whites , total) :
    if whites <= 0 :
        print attrval ,
    else :
        margen = (whites / 2) + total
        print margen ,
        printmargen(margen)
        print attrval ,


def printast (maxline) :
    print
    for x in range(maxline) :
        print "-",
    print

def formatfile (tag  , attrs , text , header) :
    listkeys = attrs.keys()
    listkeys.sort()
    whites = valuelenmax(attrs)
    total = 0
    if not header :

        for x in listkeys :
            value = len(x)
            formatWhites(x.upper() , whites , 0)
        printast(whites * len(listkeys))

    for x in listkeys :
        formatWhites(attrs[x] , whites , total)
        value = len(attrs[x])
        total = whites - value
    print

def getXML(filename) :

    try :

        if filename != None :
            root = ET.ElementTree(file=filename).getroot()
        else :
            root = ET.ElementTree(file=sys.stdin).getroot()

        header = False
        for elemento in root.iter() :
            if root.tag != elemento.tag :
                formatfile(elemento.tag , elemento.attrib , elemento.text , header)
                if not header :
                    header = True

    except ET.ParseError :
        sys.stderr.write("Error process file xml not well formed file xml" + '\n')
        raise SystemExit

def main() :
    usage = u"%prog [OPCIONES] input output if not arguments we read stdin"
    parser = argparse.ArgumentParser(usage)

    parser.add_argument("-i" , "--input"  , action="store" ,     dest="input" \
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
