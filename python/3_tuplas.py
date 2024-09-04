#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:03:17 2024

@author: luisbarranco
programa 3.- tuplas
"""
#tupla son de tipo tuple
#las tuplas son inmutables
tupla = (1,2,3,4,5,6,7,8,":)")
#print(tupla)

#acceder a un valor
#print(tupla[2])

#cambiar valor dara error
#tupla[2]=888#error
#print(tupla)

#print(tupla[1:4])#imprimir un segmento de la tupla

#print(tupla*2)#duplicado

#print(tupla+(90,91,92))#le podemos agregar algo mas unicamente por medio de una tupla
#print(tupla)

#print(tupla.index(5))#recibe elemento, devuelve el indice. Como un buscador de indice

#transformaciones de lista a tupla y viceversa
# print(tupla)
# lista=list(tupla)#constructor
# print(lista)
# print(tuple(lista))

#iteraciones
vehiculos = (('automovil',50,'gasolina'),
            ('autobus',300,'diesel'),
            ('helicoptero',2000,'turbodiesel'),
            ('velero',0,'NA'))

for vehiculo in vehiculos:
    print(len(vehiculo))#tamanio de cada tupla

tipos, capacidades, combustibles =[],[],[]#listas vacias

#pasamos las tuplas a una lista
for tipo,capacidad,combustible in vehiculos:
    tipos.append(tipo)
    capacidades.append(capacidad)
    combustibles.append(combustible)

#imprimimos las listas    
print(tipos)
print(capacidades)
print(combustibles)
    
print(len(capacidades))
print(min(capacidades))
print(max(capacidades))







