#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

print
print "Hello world!"

caja01 = []
caja02 = []

caja01.append("Javi")
caja01.append("Venancio")
caja01.append("Manuel")
caja01.append("Paula")
caja01.append("Eva")
caja01.append("Sandra")
caja01.append("Andrea")
print
print "Lista1 :" +  str(caja01)


caja02.append("Miguel")
caja02.append("Vanesa")
caja02.append("Jessica")
caja02.append("Isabel")
caja02.append("Antonio")
caja02.append("Jose")
caja02.append("Adrian")
caja02.append("Maria")
print

print "Lista2 : " + str(caja02)
print


# Clients with a little purchase go first
caja01.insert(0 , "Kiko")
caja02.insert(0 , "Belen")

print caja01
print caja02

# Abierta caja 3 pasan los pares a la caja 03
caja03 = []

caja03.append(caja02.pop(1))
caja03.append(caja02.pop(2))
caja03.append(caja02.pop(3))
caja03.append(caja02.pop(4))


print "Lista 1 :" + str(caja01)
print "Lista 2 :" + str(caja02)
print "Lista 3 :" + str(caja03)


caja01.reverse()

print "Lista 1 :" + str(caja01)

caja01.insert(3 , "Ernesto")

if "Ernesto" in caja01:
    print "Ernesto pasa de la posición " + str(caja01.index("Ernesto") + 1) + " a la 1"
    caja01.remove("Ernesto")
    caja01.insert(0 , "Ernesto")



linea_de_cajas = [caja01 , caja02 , caja03]
for x in range(len(linea_de_cajas)):
    print "Caja " + str(x) + " con clientes : " + str(linea_de_cajas[x])

for x in range(len(linea_de_cajas)):
    linea_de_cajas[x] = ";".join(linea_de_cajas[x])
    print "Caja " + str(x) + " con clientes : " + linea_de_cajas[x]
