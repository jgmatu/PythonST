#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

def print_dic (dicc):
    print
    print "****Dicc****"
    for x in dicc.keys():
        print "Key :" ,  x , "\t" , "Value :" , " ".join(dicc[x])
    print


def inlista (patternList , lista) :
    pos = 0
    encontrado = False
    while (not encontrado and pos < len(patternList)) :
        if patternList[pos] in lista :
            encontrado = True
        else:
            pos = pos + 1

    return encontrado , pos

def delte_from_List (dicc , lista):
    print "**** Delete from list ****"
    print " ".join(lista)
    print_dic(dicc)
    for x in dicc.keys():
        result = inlista(lista , dicc[x])
        if result[0] :
            found = result[1]
            print dicc[found]

print "Hello world"


dicc_cities = {"Salamanca" : ["Jamón de jagubo" , "Tortilla de Patatas" , "Vino"] , "Valencia" : ["Paella" , "Fidegua" , "Cerveza"],
             "Málaga" : ["Sardinas" , "Boquerones" , "Calamaritos" , "Pulpo Frito" , "Verengenas con miel de caña"],
             "Pais Vasco" : ["Sidra" , "Fabada" , "Entrecot" , "Atún"]
            }
print_dic(dicc_cities)


dicc_cities["A Coruña"] = ["Pulpo Cocido con Patatas y Pimenton" , "Pimientos de padron"]
dicc_cities["Madrid"] =  ["Patatas Bravas" , "Cocacola" , "Tortilla de Patatas" , "Fanta de Limon"]
print_dic(dicc_cities)



dicc_cities["Málaga"].append("Arroz de los montes")
dicc_cities["Madrid"].append("Fanta de Naranja")
print_dic(dicc_cities)

alcoholicas = []
alcoholicas = ["Vino" , "Sidra" , "Cerveza"]


delte_from_List(dicc_cities , alcoholicas)
