#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

def deletedFromLista (dicValueList , alcoholicas) :
    pos = 0
    while pos < len(dicValueList):
        if dicValueList[pos] in alcoholicas:
            dicValueList.remove(dicValueList[pos])
            pos = pos - 1;
        else:
            pos = pos + 1;


def deleteAlcoholicas (dicc_cities , alcoholicas):
    for x in dicc_cities.keys():
        deletedFromLista(dicc_cities[x] , alcoholicas)


def addTipicalPlate (dicc_cities , comunidad_valenciana):
    tipicalPlate = "Paella"
    for x in dicc_cities.keys():
        if x in comunidad_valenciana:
            dicc_cities[x].append(tipicalPlate)


def deleteComunidadValenciana (dicc_cities , comunidad_valenciana):
    for  x in dicc_cities.keys():
        if  x in comunidad_valenciana:
            del(dicc_cities[x])

def alphabetical_mode (dicc_cities):
    print
    print "Dicctionary in alphabetical mode"
    listKeys = []
    listKeys = dicc_cities.keys()
    listKeys.sort()
    for x in range(len(listKeys)):
        print "Key :" ,  listKeys[x] , "\t" , "Value :" , " | ".join(dicc_cities[listKeys[x]])
    print


def sortByLen (a , b):
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    else:
        return 0

def lenValues_mode (dicc_cities):
    print
    print "List dicctionary by Len of List Values"

    listKeys = []
    listKeys = dicc_cities.keys()

    listKeysLen = []
    for x in listKeys:
        listKeysLen += [[x ,  len(dicc_cities[x])]]

    listKeysLen.sort(sortByLen)
    for x in range(len(listKeysLen)):
        print "Key :" ,  listKeysLen[x][0] , "\t" , "Value :" , " | ".join(dicc_cities[listKeysLen[x][0]])
    print


dicc_cities = {"Salamanca"  : ["Jamón de jagubo" , "Tortilla de Patatas" , "Vino"] ,
                "Valencia"  : ["Fidegua" , "Cerveza"],
                "Málaga"    : ["Sardinas" , "Boquerones" , "Calamaritos" , "Pulpo Frito" , "Verengenas con miel de caña"],
                "País Vasco": ["Sidra" , "Fabada" , "Entrecot" , "Atún"]
            }

dicc_cities["A Coruña"] = ["Pulpo Cocido con Patatas y Pimenton" , "Pimientos de padrón"]
dicc_cities["Madrid"] =  ["Patatas Bravas" , "Cocacola" , "Tortilla de Patatas" , "Fanta de Limon"]


dicc_cities["Málaga"].append("Arroz de los montes")
dicc_cities["Madrid"].append("Fanta de Naranja")
dicc_cities["Madrid"].append("Cerveza")
dicc_cities["Madrid"].append("Vino")
dicc_cities["Alicante"] = ["Calamares"]


alcoholicas = []
alcoholicas = ["Vino" , "Sidra" , "Cerveza"]

deleteAlcoholicas(dicc_cities , alcoholicas)

comunidad_valenciana = []
comunidad_valenciana = ["Valencia" , "Alicante" , "Castellón"]

addTipicalPlate(dicc_cities , comunidad_valenciana)
deleteComunidadValenciana(dicc_cities , comunidad_valenciana)

alphabetical_mode(dicc_cities)

lenValues_mode(dicc_cities)
