#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys , os , shutil
import argparse
import xmlpp


TAB = 8

def openFile (fileName , mode) :
    try :
        fich = open(fileName , mode)
        return fich
    except :
        sys.stderr.write("Error open file " + fileName + " mode : " + mode.upper())
        raise SystemExit


filename = "coches.xml"

fileR = openFile(filename , "r")
dataFile = fileR.read()
fileR.close()

fileW = openFile("/tmp/a" , "w")
xmlpp.pprint(dataFile , fileW , TAB , 80)
fileW.close()

fileW = openFile("/tmp/a" , "r")
print "!" , dataFile
print "!" , fileW.read()
fileW.close()

shutil.move("/tmp/a" , filename)
