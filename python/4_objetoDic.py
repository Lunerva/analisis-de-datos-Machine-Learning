#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:36:59 2024

@author: luisbarranco
Programa 4.- objetos dict
"""

#forma 1 = Parejas llave:valor
# persona={"nombre":"Jose","apellido_1":"Perez","apellido_2":"Lopez"}
# print(persona)
# print(persona["apellido_2"])

#modificando elemento del diccionario
# persona['nombre']="Luis";
# print(persona)

# #forma 2
# otra = dict(nombre="Armando",escolaridad_maxima="Licenciatura")#constructor
# print(otra)
# del otra["nombre"]
# print(otra)

#primera forma
persona={"nombre":"Jose","apellido_1":"Perez","apellido_2":"Lopez"}
# print(persona.get("nombre"))

#update
persona.update({"nombre":"Pedro","codigo_postal":"27000"})
# print(persona)

persona.update({"Profesion":"ISC"})
# print(persona)

#setdefault
persona.setdefault("email","correo_isc@itlalaguna.edu.mx")
# print(persona)
persona.setdefault("certificacion")
# print(persona)


# elementos = persona.items()#creamos un objeto iterable
# print(elementos)
# for elemento in elementos:
#     print(elemento)
    
    
#keys del diccionario
llaves = persona.keys()
print(llaves)
for clave in llaves:
    print(clave)
    
#valores del diccionario
valores = persona.values()
print(valores)
for val in valores:
    print(val)






