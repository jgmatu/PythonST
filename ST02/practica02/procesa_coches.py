#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import sys , os , shutil
import argparse
import xml.etree.ElementTree as ET


def formatfile (tag  , attr , text) :
        print "Etiqueta : " , tag
        print "Atributos : " ,attr
        print "Texto : " , text


def getXML(filename) :
    root = ET.ElementTree(file=filename).getroot()
    for elemento in root.iter() :
        formatfile(elemento.tag , elemento.attrib , elemento.text)


def main() :
    usage = "%prog [OPCIONES] input output if not arguments we read stdin"
    parser = argparse.ArgumentParser(usage)

    parser.add_argument("-i" , "--input"  , action="store" ,     dest="input"  , help = "xml file to format")
    arguments = parser.parse_args()

    if arguments.input == None :
        print "read from stdin"
    else :
        print "read from file " + arguments.input
        if not os.path.exists(arguments.input) :
            print "File : " + arguments.input + " not exist."
            raise SystemExit
        getXML(arguments.input)


if __name__ == "__main__":
        main()
