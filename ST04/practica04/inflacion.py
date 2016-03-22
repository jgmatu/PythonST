#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys , types
import json

INFLACION = 3
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
    precio = "precio"

    keys = jsonObj.keys()
    keys.reverse()

    whites = 0
    for x in keys :

        if x in precio :
            # Calc inflation in script.
            jsonObj[x] = jsonObj[x] * (1 + INFLACION*0.01)

        print jsonObj[x] ,

        if isNumb(jsonObj[x]) :
            # Conver to String the number to get its length and calc spaces.
            whites = FIELD - len(str(jsonObj[x]))

        #Print whites between fileds.
        printwhites(whites)
    print

def main () :
    # Read all the text ang get an string with data next step was load the
    # string like a json file.
    jsonval = readIn()

    # Tabular format data get with file.
    printhead()
    for x in range(len(jsonval)) :
        showObj(jsonval[x])

if __name__ == "__main__" :
    main()
