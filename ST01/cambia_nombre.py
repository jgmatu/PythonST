#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import sys , subprocess
import shutil ,os

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
    specials = ["|" , "@" , "#" , "~" ,"!" , "�" , "$" , "%" , "&" , ":" , ")" , "("]
    fileNameChanged = fileName.strip()
    for x in range(len(specials)) :
        fileNameChanged = fileNameChanged.replace(specials[x] , ".")
    return fileNameChanged

def changeName (fileName) :
    """ This the names and moves the files to the new name of file """
    fileNameChanged = fileName.strip()
    fileNameChanged = changeSpace(fileName)
    fileNameChanged = mayToMin(fileNameChanged)
    fileNameChanged = changeVolcals(fileNameChanged)
    fileNameChanged = changeSpecials(fileNameChanged)
    return fileNameChanged

def IsDirectory (path) :
    return os.path.exists(path)

def saveNames (path) :
    names = {}
    files = os.listdir(path)   # Files in directory
    for x in range(len(files)):
        fileD = changeName(files[x])
        if names.has_key(fileD):
            names[fileD].append(files[x])
        else :
            names[fileD] = [files[x]]
    return names

def putExt (names , fileDest , files) :
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

def extensions (names) :
    keys = names.keys()
    for x in keys :
        if len(names[x]) != 1 :
            putExt(names , x , names[x])

def changeNames (path) :

    if not IsDirectory(path) :
        sys.stderr.write("Not is a valid directory\n")
        raise SystemExit
    names = {}
    names = saveNames(path)
    print names
    extensions(names)
    print names



sys.argv.remove(sys.argv[0]) # Delete name of program is not a valid path
if len(sys.argv) == 0:
    print "Work inside the current directory"
    changeNames(".")
else:
    print "Work in the list of path directories"
    xRange = range(len(sys.argv))
    for x in xRange :
        changeNames(sys.argv[x])
