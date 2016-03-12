#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import sys , os , shutil
import argparse
import xml.etree.ElementTree as ET

MAX = 55


def printnumSong (numSong) :
    if int(numSong) < 10 :
        print numSong + '  ' ,
    elif int(numSong) < 100 :
        print numSong + ' ' ,
    else :
        print numSong + '',

def printspaces (lenword) :
    for x in range(MAX - lenword) :
        print '',

def formatfile (attr , numsong) :
    printnumSong(str(numsong))
    printspaces(40)
    keys = attr.keys()
    keys.reverse()
    for x in keys :
        print attr[x].upper() ,
        if not x in "duracion" :
            printspaces(len(attr[x]))
    print

def printborder () :
    print '-------'*MAX

def printheader (attr) :
    keys = attr.keys()
    keys.sort()

    printborder()
    for x in keys :
        print attr[x].upper() ,

        if not x in "titulo" :
            print ' '*MAX ,
    print
    printborder()

def getXML(filename) :

    try :
        if filename != None :
            root = ET.ElementTree(file=filename).getroot()
        else :
            root = ET.ElementTree(file=sys.stdin).getroot()

        numsong = 1
        for elemento in root.iter() :

            if elemento.tag in "disco" :
                printheader(elemento.attrib)
                numsong = 1
                continue

            if root.tag != elemento.tag :
                formatfile(elemento.attrib , numsong)
                numsong = numsong + 1

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
