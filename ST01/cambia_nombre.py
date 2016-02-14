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

def changeName (path , fileName) :
    """ This function modify the names and moves the files to the new name of file """
    fileNameChanged = fileName.strip()

    routeS = os.path.join(path , fileNameChanged)

    fileNameChanged = changeSpace(fileName)
    fileNameChanged = mayToMin(fileNameChanged)
    fileNameChanged = changeVolcals(fileNameChanged)
    fileNameChanged = changeSpecials(fileNameChanged)
    routeD = os.path.join(path , fileNameChanged)

    shutil.move(routeS , routeD)

def IsDirectory (path) :
    return os.path.exists(path)

def changeNames (path) :
    if not IsDirectory(path) :
        sys.stderr.write("Not is a valid directory\n")
        raise SystemExit

    files = os.listdir(path)
    for x in range(len(files)):
        changeName(path , files[x])


sys.argv.remove(sys.argv[0]) # Delete name of program is not a valid path
if len(sys.argv) == 0 :
    print "Work inside the current directory"
    changeNames(".")
else :
    print "Work in the list of path directories"
    xRange = range(len(sys.argv))
    for x in xRange :
        changeNames(sys.argv[x])
