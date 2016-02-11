#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import sys , subprocess
import os

def IsDirectory (path) :
    return os.path.exists(path)

def changeVolcals (fileName):
    vocalsAccenture = ["á" , "é" , "í" , "ó" , "ú"]
    vocals = ["a" , "e" , "i" , "o" , "u"]
    fileNameChanged = fileName.strip()
    pos = 0
    while pos < len(vocals):
        fileNameChanged = fileNameChanged.replace(vocalsAccenture[pos] , vocals[pos])
        pos = pos + 1
    return fileNameChanged


def changeSpace (fileName):
    return fileName.replace(" " , "_")

def mayToMin (fileName):
    return fileName.lower()

def changeSpecials (fileName) :
    specials = ["|" , "@" , "#" , "~" ,"!" , "�" , "$" , "%" , "&"]
    fileNameChanged = fileName.strip()
    pos = 0
    while pos < len(specials) :
        fileNameChanged = fileNameChanged.replace(specials[pos] , ".")
        pos = pos + 1
    return fileNameChanged

def changeName (fileName) :
    fileNameChanged = fileName.strip()
    command="mv:" + fileName

    fileNameChanged = changeSpace(fileName)
    fileNameChanged = mayToMin(fileNameChanged)
    fileNameChanged = changeVolcals(fileNameChanged)
    fileNameChanged = changeSpecials(fileNameChanged)

    command += ":" + fileNameChanged
    command_parameters = command.split(":")

    print command_parameters

    try:
        subprocess.call(command_parameters)
    except subprocess.CalledProcessError :
        sys.stderr.write("La orden mv ha producido un error\n")


def changeNames (path) :
    if not IsDirectory(path) :
        sys.stderr.write("Not is a valid directory\n")
        raise SystemExit

    files = os.listdir(path)
    for x in range(len(files)):
        changeName(files[x])


sys.argv.remove(sys.argv[0]) # Delete name of program is not a valid path
if len(sys.argv) == 0:
    print "Work inside the current directory"
    changeNames(".")
else:
    print "Work in the list of path directories"
    xRange = range(len(sys.argv))
    for x in xRange :
        print "path : " + sys.argv[x]
        changeNames(sys.argv[x])
