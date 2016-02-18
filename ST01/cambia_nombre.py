#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import sys , subprocess
import shutil ,os
from optparse import OptionParser

def changeVolcals (fileName):
    vocalsAccenture = ["á" , "é" , "í" , "ó" , "ú"]
    vocals = ["a" , "e" , "i" , "o" , "u"]
    fileNameChanged = fileName.strip()
    for x  in range(len(vocals)):
        fileNameChanged = fileNameChanged.replace(vocalsAccenture[x] , vocals[x])
    return fileNameChanged


def changeSpace (fileName):
    return fileName.replace(" " , "_")

def mayToMin (fileName):
    return fileName.lower()

def changeSpecials (fileName) :
    specials = ["|" , "@" , "#" , "~" ,"!" , "�" , "$" , "%" , "&" , ":" , ")" , "(" , "-"]
    fileNameChanged = fileName.strip()
    for x in range(len(specials)) :
        fileNameChanged = fileNameChanged.replace(specials[x] , ".")
    return fileNameChanged


def thereOpt(options) :
    return options.space or options.case or options.accent or options.weird

def changeName (fileName , options) :
    """ This the names and moves the files to the new name of file """
    fileNameChanged = fileName.strip()

    if thereOpt(options) :
        if options.space :
            fileNameChanged = changeSpace(fileName)
        if options.case :
            fileNameChanged = mayToMin(fileNameChanged)
        if options.accent :
            fileNameChanged = changeVolcals(fileNameChanged)
        if options.weird :
            fileNameChanged = changeSpecials(fileNameChanged)
    else :
        fileNameChanged = changeSpace(fileName)
        fileNameChanged = mayToMin(fileNameChanged)
        fileNameChanged = changeVolcals(fileNameChanged)
        fileNameChanged = changeSpecials(fileNameChanged)

    return fileNameChanged

def IsDirectory (path) :
    return os.path.exists(path)

def saveNames (path , options) :
    names = {}
    files = os.listdir(path)   # Files in directory
    for x in range(len(files)):
        fileD = changeName(files[x] , options)
        if names.has_key(fileD):
            names[fileD].append(files[x])
        else :
            names[fileD] = [files[x]]
    return names

def putExt (names , fileDest , files) :
    """The files whose have colsions we put the extions to file"""
    pos = 0
    fileExt = fileDest.strip()

    while pos < len(files):
        fileExt = fileDest
        if (pos > 9) :
            ext = "0" + str(pos)
        elif (pos > 99):
            ext = str(pos)
        else :
            ext = "0"*2 + str(pos + 1)
        fileExt += ext
        names[fileDest].remove(files[pos - 1])
        names[fileDest].append(fileExt)
        pos = pos + 1

def colisions (names) :
    """ Comprobar si hay ficheros que colisionen """
    keys = names.keys()
    for x in keys :
        if len(names[x]) != 1 :
            """ Los nombres de ficheros que tengan mas de uno en la lista
            respecto del original son varios ficheros que dan el mismo nombre
            hay que ponerles la extension"""
            putExt(names , x , names[x])

def changeNames (path , parser , options) :
    namesSource = {}
    namesDest = {}

    if not IsDirectory(path) :
        parser.error("Not is a valid directory \n")
        raise SystemExit
    names = saveNames(path , options)
    colisions(names)

    """ Inicialize the number of colisions changed..."""
    keys = names.keys()
    for x in keys :
        names[x].append(0)

    """ Move the files to its new name"""
    files = os.listdir(path)
    for x in range(len(files)):
        fileName = changeName(files[x] , options)
        if len (names[fileName]) != 2 :
            """Change names of files with colsisions with her extension"""
            num = names[fileName].pop(len(names[fileName]) - 1)
            source =  os.path.join(path , files[x])
            dest =  os.path.join(path , names[fileName][num])
            shutil.move(source , dest)
            names[fileName].append(num + 1)
        else :
            """Default change name..."""
            source =  os.path.join(path , files[x])
            dest = os.path.join(path , fileName)
            shutil.move(source , dest)



def recursiving (path , parser , options) :
    for x in os.walk(path) :
        changeNames(x[0] , parser , options)

def workInDirectories (arguments , parser , options) :
    """Work in the list of path directories"""
    print "Work in the list of path directories"
    xRange = range(len(arguments))
    for x in xRange :
        if options.recursive :
            recursiving(arguments[x] , parser , options)
        else :
            changeNames(arguments[x] , parser , options)


def workinActualDir (path , parser , options) :
    print "Work inside the current directory"
    changeNames(path , parser , options)

def main() :
    usage = "Use: %prog [OPTION]... DIRECTORY... "
    parser = OptionParser(usage)
    parser.add_option("-r" , "--recursive" , action="store_true" , dest="recursive" , help="Uso recursivo")
    parser.add_option("-s" , "--space" , action="store_true" , dest="space" , help="Replace space to _")
    parser.add_option("-c" , "--case" , action="store_true" , dest="case" , help="Replace may to min")
    parser.add_option("-n" , "--enne" , action="store_true" , dest="enne" , help="Replace enne to nh")
    parser.add_option("-t" , "--accent" , action="store_true" , dest="accent" , help= "Replace vocals accenture")
    parser.add_option("-w" , "--weird" , action="store_true" , dest="weird" , help= "Replace Specials caracters")
    (options , arguments) = parser.parse_args()

    if len(arguments) == 0:
        workinActualDir("." , parser , options)
    else:
        workInDirectories(arguments , parser , options)

if __name__ == "__main__" :
    main()
