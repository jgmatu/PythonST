#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys , types
import json

FIELD = 12
ATTRS = 3

def readIn () :
    return json.loads(sys.stdin.read())

def printwhites (nwhites) :
    for x in range(nwhites) :
        print '',

def printhead () :
    ref = "Ref."
    precio = "Precio"
    descripcion = "Descripcion"

    #Field 1
    print ref ,
    printwhites(FIELD - len(ref))

    #Field 2
    print precio ,
    printwhites(FIELD - len(precio))

    #Field 3
    print descripcion ,
    printwhites(FIELD - len(descripcion))

    # Last Field
    print

    # Row separate values of head.
    print FIELD*ATTRS*'-'



def isNumb (name) :
    return type(name) == types.IntType  or type(name) == types.FloatType

def showObj (jsonObj) :

    keys = jsonObj.keys()
    keys.reverse()

    whites = 0
    for x in keys :

        print jsonObj[x] ,

        if isNumb(jsonObj[x]) :
            #Check if value is a number to convert an string and get its
            #length.
            whites = FIELD - len(str(jsonObj[x]))

        #Print whites between fields.
        printwhites(whites)

    print

def main () :
    # Read json file from stdin and get a structure data json in python data.
    jsonval = readIn()

    #Format json data in Tabular format.
    printhead()
    for x in range(len(jsonval)) :
        showObj(jsonval[x])

if __name__ == "__main__" :
    main()
