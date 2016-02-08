#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

def modo_laxo (nota) :
    if nota < 4 :
        return "Suspenso"

    if nota >= 4 and nota < 6 :
        return "Suficiente"

    if nota >= 6 and nota < 7 :
        return "Bien"

    if nota >= 7 and nota < 9 :
        return "Notable"

    if nota >= 9 and nota <= 10 :
        return "Sobresaliente"

    return "Not Nota"


def modo_normal (nota):
    if nota < 4.5 :
        return "Suspenso"

    if nota >= 4.5 and nota < 6:
        return "Suficiente"

    if nota >= 6 and nota < 7:
        return "Bien"

    if nota >= 7 and nota < 9:
        return "Notable"

    if nota >= 9 and nota <= 10:
        return "Sobresaliente"

    return "Result"

def modo_extricto(nota):
    if nota < 5 :
        return "Suspenso"

    if nota >= 5 and nota < 6:
        return "Suficiente"

    if nota >= 6 and nota < 7:
        return "Bien"

    if nota >= 7 and nota < 9:
        return "Notable"

    if nota >= 9 and nota <= 10:
        return "Sobresaliente"

    return "Not Nota"


def redondea_nota (nota , modo):
    if nota < 0 or nota > 10:
        return "Nota not possible"

    if modo == "laxo" :
        return modo_laxo(nota)
    elif modo == "normal":
        return modo_normal(nota)
    elif modo == "extricto":
        return modo_extricto(nota)
    else:
        return "Bad mode"


nota = 4
modo = ["laxo" , "normal"  , "extricto"]

print redondea_nota(10 , modo[1])
