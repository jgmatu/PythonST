#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

def print_dic (dicc):
    print
    print "****Dicc****"
    for x in dicc.keys():
        print "Key :" ,  x , "\t" , "Value :" , " | ".join(dicc[x])
    print


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


dicc_cities = {"Salamanca" : ["Jamón de jagubo" , "Tortilla de Patatas" , "Vino"] ,
                "Valencia" : ["Paella" , "Fidegua" , "Cerveza"],
                "Málaga" : ["Sardinas" , "Boquerones" , "Calamaritos" , "Pulpo Frito" , "Verengenas con miel de caña"],
                "Pais Vasco" : ["Sidra" , "Fabada" , "Entrecot" , "Atún"]
            }


dicc_cities["A Coruña"] = ["Pulpo Cocido con Patatas y Pimenton" , "Pimientos de padrón"]
dicc_cities["Madrid"] =  ["Patatas Bravas" , "Cocacola" , "Tortilla de Patatas" , "Fanta de Limon"]


dicc_cities["Málaga"].append("Arroz de los montes")
dicc_cities["Madrid"].append("Fanta de Naranja")
dicc_cities["Madrid"].append("Cerveza")
dicc_cities["Madrid"].append("Vino")



alcoholicas = []
alcoholicas = ["Vino" , "Sidra" , "Cerveza"]


deleteAlcoholicas(dicc_cities , alcoholicas)

print_dic(dicc_cities)
