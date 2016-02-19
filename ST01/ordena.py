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

def getLine (line , numline) :
    result = []

    if len(line[-1]) == 0 or line[-1].find(' ') != -1 :
        print "There is a not valid line of file there is a cuotte :" + str(numline)
        raise SystemExit

    for x in range(len(line)) :
        try :
            result.append(int(line[x]))
        except :
            print "Not is a number : " + line[x] + " numline : " + str(numline)
            raise SystemExit
    return result

def formatF (list_lines) :
    listformatlines = []
    line = ""
    print list_lines
    for x in range(len(list_lines)) :
        list_lines[x].strip()
    print list_lines
    return listformatlines


def readFile (fileName) :
    try :
        fich = open(fileName , "r")
    except :
        print "Error open file : " + fileName + "\ttry again"
        raise SystemExit
    list_lines = fich.readlines()

    listNumb = []
    listStr =  []
    numline = 1

    listStr = formatF(list_lines)
    for x in range(len(listStr)) :
        listNumb.append(getLine(listStr , numline))
        numline = numline + 1
    fich.close()
    return listNumb


def writeFile (fileName , listNumb) :

    try :
        fich = open(fileName , "w")
    except :
        print "Error open file : " + fileName + "\t try again"
        raise SystemExit

    # Sort and cast numbers to write in my file */
    listNumb.sort(mySort)
    for x in range(len(listNumb)) :
        for y in range(len (listNumb[x])) :
            listNumb[x][y] = str(listNumb[x][y])

    for x in range(len(listNumb)) :
        fich.write(" ".join(listNumb[x]) + '\n')
    fich.close()


def stdin () :
    lines = []
    lines = formatF(lines)
    for line in sys.stdin.readlines():
        lines.append(line)
        sys.stdout.write(line)
    print lines


def main () :
    usage = "Use %prog [Opciones] [INPUT] [OUPUT] DEFAULT stdin stout"
    parser = ArgumentParser(usage)
    parser.add_argument("-i" , "--input" , action="store" , dest="input", type=str , help="Select a file to input")
    parser.add_argument("-o" , "--output" , action="store" , dest="output", type=str , help="Select a file to output")

    arguments = parser.parse_args()


    listNumb = []
    if arguments.input == None and arguments.output == None :

        #Read stdin write stdout
        print "Read stdin write stdout"

    elif  arguments.input != None and arguments.output == None :

        #Read from file and write in stdout
        print "Read from file : " + arguments.input + "\twrite in stdout"

    elif arguments.input == None and arguments.output != None :

        #Read from stdin write in file.
        print "Read from stdin and write in file : " + arguments.output

    else :

        #Read from file write in file
        print "Read from file : " + arguments.input +   "\tand write in file : " + arguments.output

    #stdin()
    listNumb = readFile("prueba.txt")
    writeFile("write.txt"  , listNumb)

if __name__ == "__main__" :
    main()
