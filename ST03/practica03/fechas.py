#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys , os , shutil
import datetime , pytz



def openfile (fileName , mode) :
    try :
        fich = open(fileName , mode)
        return fich
    except IOError :
        sys.stderr.write("Error open file " + fileName + " mode : " + mode.upper())
        raise SystemExit

def readfile (filename) :
    fileR = openfile(filename , "r")
    for x in fileR.readlines() :
        print x

def main () :
    readfile("listzonas.txt")

if __name__ == "__main__" :
    main()
