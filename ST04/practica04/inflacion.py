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

    print ref ,
    printwhites(FIELD - len(ref))
    print precio ,
    printwhites(FIELD - len(precio))
    print descripcion ,
    printwhites(FIELD - len(descripcion))
    print
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
            jsonObj[x] = jsonObj[x] * (1 + INFLACION*0.01)

        print jsonObj[x] ,
        if isNumb(jsonObj[x]) :
            whites = FIELD - len(str(jsonObj[x]))
        printwhites(whites)
    print

def main () :
    jsonval = readIn()
    printhead()
    for x in range(len(jsonval)) :
        showObj(jsonval[x])

if __name__ == "__main__" :
    main()
