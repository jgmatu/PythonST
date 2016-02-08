#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import sys
import os

def IsDirectory (path) :
    return os.path.exists(path)

def changeName (fileName) :
    mandato="mv " + fileName
    mandato_troceado=mandato.split()
    try:
        subprocess.check_output(mandato_troceado)
    except subprocess.CalledProcessError:
        sys.stderr.write("La orden mv ha producido un error\n")
        raise SystemExit


def changeNames (path) :
    if not IsDirectory(path) :
        sys.stderr.write("Not is a valid directory\n")
        raise SystemExit
    files = os.listdir(path)
    for x in range(len(files))
        changeName(files)
        
sys.argv.remove(sys.argv[0]) # Delete name of program is not a valid path
if len(sys.argv) == 0 :
    print "Work inside the current directory"
    changeNames(".")
else :
    print "Work in the list of path directories"
    xRange = range(len(sys.argv))
    for x in xRange :
        print "path : " + sys.argv[x]
        changeNames(sys.argv[x])
