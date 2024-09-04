#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:12:44 2024

@author: luisbarranco
Practica 5.- Cadenas
"""
# saludo = "hola mundo"
# print(saludo[1])

# #da error porque no se puede modificar de esta forma
# # saludo[1] = 'a'

# print(saludo.count("o"))
# print(saludo.upper())
# print(saludo.lower())
# print(saludo.capitalize())

# lectura = "contrato de prestacion de servicios entre {1} y {0}.".format("juan", "Pedro")
# print(lectura)
# lectura = "contrato de servicios entre {comprador} y {vendedor}.".format(comprador="Juan",vendedor="Pedro")
# print(lectura)

#Big data
# cad = "Hugo, Paco, Luis".split(",")#dividio los elementos por medio de las comas
# print(cad)

# cad = "Hugo, Paco, Luis".split("* ")
# print(cad)

# nom = "Hugo.\nPaco.\nLuis."
# print(nom)

# print(nom.splitlines())

# print(nom.find("Hugo"))

cad = "Hola, mundo"

print(cad.startswith("H"))
print(cad.endswith("do"))

print(cad.isascii())
print(cad.isalpha())
car = "aa#%&!"
print(car.isalpha())
car = "hola"
print(car.isalpha())
num="123"
print(num.isnumeric())
print(len(cad))
print(max(cad))
print(min(cad))

#transformaciones
print(bytes(cad,"utf-8")) #string a byte
print(str(b"hola"[1:3],'ascii')) #de char a string
for letra in cad:
    print(letra)










