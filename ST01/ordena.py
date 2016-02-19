#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import types
import sys

from argparse import ArgumentParser

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


def invalidline (numline , errline) :
    print "Invalid line \t" + str(numline) + " : " + errline


def getLine (line , numline , errline) :
    result = []

    if len(line[-1]) == 0 or line[-1].find(' ') != -1 :
        invalidline(numline , errline)
        raise SystemExit

    for x in range(len(line)) :
        try :
            result.append(int(line[x]))
        except :
            invalidline(numline , errline)
            raise SystemExit

    return result


def formatFile (list_lines) :
    """Function format file convection to convert in number later..."""
    # Drop extremes spaces and /n and data struct convert
    format1 = []
    format2 = []
    for x in range(len(list_lines)) :
            format1.append(list_lines[x].strip())
            if format1[x] != "" :   # Empty lines
                format2.append(format1[x].split(','))

    # Drop all white space between string separe by cuotes
    format3 = []
    for x in range(len(format2)) :
        formataux = []
        for y in range(len(format2[x])):
            formataux.append(format2[x][y].strip())
        format3.append(formataux)
    return format3


def openFile (fileName , mode) :
    try :
        fich = open(fileName , mode)
        return fich
    except :
        print "Error open file " + fileName + " mode : " + mode.upper()
        raise SystemExit


def converNums (linesfomat , lines) :
    listNumb = []
    numline = 1
    for x in range(len(linesfomat)) :
        listNumb.append(getLine(linesfomat[x] , numline , lines[x]))
        numline = numline + 1
    return listNumb



def readFile (fich) :
    list_lines = fich.readlines()
    listformatlines = formatFile(list_lines)
    return converNums(listformatlines , list_lines)


def castNums (listNumb) :
    for x in range(len(listNumb)) :
        for y in range(len (listNumb[x])) :
            listNumb[x][y] = str(listNumb[x][y])
    return listNumb

def writeFile (fich , listNumb) :
    # Sort and cast numbers to write in my file
    listNumb.sort(mySort)
    listNumb = castNums(listNumb)
    for x in range(len(listNumb)) :
        fich.write(",".join(listNumb[x]) + '\n')


def stdin () :

    print "Write numbers in good format"
    lines = []
    linesfomat = []
    for line in sys.stdin.readlines():
        lines.append(line)
    linesfomat = formatFile(lines)
    linesfomat = converNums(linesfomat , lines)
    return linesfomat

def stdout (listNumb) :

    print "Results of sort Numbers in format :"
    listNumb.sort(mySort)
    listNumb = castNums(listNumb)
    for linea in listNumb :
        sys.stdout.write(",".join(linea) + '\n')


def main () :
    
    usage = "Use %prog [Options] [INPUT] [OUPUT] DEFAULT stdin stout"
    parser = ArgumentParser(usage)
    parser.add_argument("-i" , "--input" , action="store" , dest="input", type=str , help="Select a file to input")
    parser.add_argument("-o" , "--output" , action="store" , dest="output", type=str , help="Select a file to output")

    arguments = parser.parse_args()

    listNumb = []
    if arguments.input == None and arguments.output == None :
        #Read stdin write stdout
        listNumb = stdin()
        stdout(listNumb)

    elif  arguments.input != None and arguments.output == None :
        #Read from file and write in stdout
        fich = openFile(arguments.input , "r")
        listNumb = readFile(fich)
        fich.close()
        stdout(listNumb)

    elif arguments.input == None and arguments.output != None :
        #Read from stdin write in file.
        listNumb = stdin()
        fich = openFile(arguments.output , "w")
        writeFile(fich , listNumb)
        fich.close()

    else :
        #Read from file write in file
        fich = openFile(arguments.input , "r")
        listNumb = readFile(fich)
        fich.close()

        fich = openFile(arguments.output , "w")
        writeFile(fich , listNumb)
        fich.close()


if __name__ == "__main__" :
    main()
