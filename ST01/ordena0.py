#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import types
import sys

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

def main () :
    lista1 = [[1 , 3] , [5] , [0] , [2 , 2 , 2]]
    lista1.sort(mySort)
    print lista1
    lista2 = [[1 , 3] , [2 , 1 , 1] , [1 , 1 , 1 , 1] , [4] , [5 , 3] , [4 , 3] , [0]]
    lista2.sort(mySort)
    print lista2
    lista3 = []
    if len(lista3) != 0 :
        lista3.sort(mySort)
    else :
        sys.stderr.write("Not is a list allowed exception SystemExit called\n")
        raise SystemExit
    print lista3


if __name__ == "__main__" :
    main()
