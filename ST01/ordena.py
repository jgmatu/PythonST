#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import types
import sys

from optparse import OptionParser

def isNumber (element):
    return type(element) == types.IntType or type(element) == types.FloatType or \
                type(element) == types.LongType

def sum_elemtens (list_elements):
    total = 0

    for x in range(len(list_elements)):
        if isNumber(list_elements[x]):
            total += list_elements[x]
        else:
            sys.stderr.write("Not is a number element exception SystemExit called\n")
            raise SystemExit
    return total

def mySort (a , b):
    if sum_elemtens(a) < sum_elemtens(b) :
        return -1
    elif sum_elemtens(a) > sum_elemtens(b):
        return 1
    else :
        if len(a) < len(b):
            return -1
        elif len(a) > len(b):
            return 1
        else:
            return 0

def isLine (line) :
    print line
    return True

def readFile (fileName) :
    try :
        fich = open(fileName , "r")
    except :
        print "Error open file : " + fileName + " try again"
        raise SystemExit
    list_lines = fich.readlines()
    listNumb = []
    for x in range(len(list_lines)) :
        if isLine(list_lines[x]) :
            print "Tested line ok"
        else :
            print "Tested line fail"
        listNumb.append(list_lines[x].split(','))

def main () :
    usage = "Use %prog [Opciones] [INPUT] [OUPUT] DEFAULT stdin stout"
    parser = OptionParser(usage)
    parser.add_option("-i" , "--input" , action="store_true" , dest="input", help="Select a file to input")
    parser.add_option("-o" , "--output" , action="store_true" , dest="output", help="Select a file to output")

    (options , arguments) =  parser.parse_args()

    if len(arguments) == 0 :
        #Read stdin write stdout
        print "Read stdin write stdout"
    elif  len(arguments) == 1 and options.input :
        #Read from file and write in stdout
        print "Read from file and write in stdout"
    elif len(arguments) == 1 and options.output :
        #Read from stdin write in file.
        print "Read from stdin and write in file"
    else :
        #Read from file write in file
        print "read from file  and write in file"

    readFile("prueba.txt")

if __name__ == "__main__" :
    main()
