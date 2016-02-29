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

def changeEnne (fileName) :
    fileNameChanged = fileName.strip()
    fileNameChanged = fileNameChanged.replace("ñ" , "ny")
    return fileNameChanged

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
    fileNameChanged = changeEnne(fileNameChanged)
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

def changeNames (path) :
    namesSource = {}
    namesDest = {}

    if not IsDirectory(path) :
        sys.stderr.write("Not is a valid directory\n")
        raise SystemExit
    names = saveNames(path)
    colisions(names)

    """ Inicialize the number of colisions changed..."""
    keys = names.keys()
    for x in keys :
        names[x].append(0)

    """ Move the files to its new name"""
    files = os.listdir(path)
    for x in range(len(files)):
        if len (names[changeName(files[x])]) != 2 :
            """Change names of files with colsisions with her extension"""
            num = names[changeName(files[x])].pop(len(names[changeName(files[x])]) - 1)
            source =  os.path.join(path , files[x])
            dest =  os.path.join(path , names[changeName(files[x])][num])
            shutil.move(source , dest)
            names[changeName(files[x])].append(num + 1)
        else :
            """Default change name..."""
            source =  os.path.join(path , files[x])
            dest = os.path.join(path , changeName(files[x]))
            shutil.move(source , dest)


sys.argv.remove(sys.argv[0]) # Delete name of program is not a valid path
if len(sys.argv) == 0:
    print "Work inside the current directory"
    changeNames(".")
else:
    print "Work in the list of path directories"
    xRange = range(len(sys.argv))
    for x in xRange :
        changeNames(sys.argv[x])
