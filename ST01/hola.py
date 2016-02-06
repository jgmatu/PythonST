#!/usr/bin/python -tt

def concat (x , y) :
    return x + y;


# Dictionary
llegadas = {"MS" : ['Madrid-Sevilla' , 34 , True , "Llegando"],
            "BM" : ['Barcelona-Madrid' , 44 , True , "Retraso"],
            "MA" : ['Madrid-Alicatne' , 32 , False , "Estacion"],
            "LG" : ['Lleida-Galicia' , 34 , True , "Estacion"]}

keysDic = llegadas.keys()

keysDic.sort()

for x in keysDic:
    print "Key   :" + str(x), "\tValue" + str(llegadas[x])

llegadas["MS"].insert(2 , "Embarque")
print llegadas["MS"]

llegadas["MS"] =  concat(llegadas["MS"] , [1])

print llegadas["MS"]

print (concat('2' , '3'))

llegadas["LG"].append("Jabalquinto")

for x in llegadas.keys() :
    print
    print x , llegadas[x]


string = "ahora eres feliz... no te falta nada se agradecido... has jugado a la comba con alba y mireiya has hablado con alba y te quieres mas que a nada en el mundo... no pidas mas" \
      " por que no hay nada mas bello que lo que estas haciendo ahora mismo javi :)"

listaStr = string.split()

print

print listaStr

happyStr = " ".join(listaStr)

print
print happyStr
print

guiones = "desnudameeee-juega-conmigo-a-serrr-la-perdicion-que-todo-hombre-quisieraposeer-y-olvidateeee-de-toodoo-lo-quefuii-quieremeee-por-lo-que-pueda-llegar-a-ser-en-tu-vidaa"

listGuion = guiones.split("-")

print listGuion

print
for x in range(10):
    print x,
