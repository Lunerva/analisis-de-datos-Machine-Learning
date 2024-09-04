#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:37:40 2024

@author: luisbarranco
Practica 6.- funciones
"""

#metodo esta dentro de una clase
#la funcion esta separada


# def saludo():
#     print("hola desde la funcion")
    
    
# saludo()


# def suma(primero, segundo):
#     '''Despliega la suma de dos objetos'''
#     """ Despliega... """
#     print(primero+segundo)
    
    
# suma(5,10)


# def promedio(*muestras):#la tupla se envia con asterisco
#     '''calcula el promedio de la muestra
#     correspondiente a todos los paramatros ingresados'''
#     print(type(muestras))
#     promedio = sum(muestras)/len(muestras)
#     print('El promedio de la muestra de %d elementos es %.3f' %(len(muestras),promedio))
    

# promedio(1,3,5,8,11,24,90,29)
# promedio(14,38,1)

# def promedio(titulo, *muestras):
#     '''calcula el promedio de la muestra correspondiente a todos los parametros del primero,
#     el cual sera utilizado como titulo'''
#     promedio = sum(muestras)/len(muestras)
#     print(titulo)
#     print('El promedio de la muestra de %d elementos es %.3f' %(len(muestras),promedio))
    
    
    
# promedio('Conteo de abejas en campo', 34,45,61,23,47,41,52)


#objeto dirt doble **
# def superficie(**dato):
#     '''Calcula la uperficie de una figura geometrica si los parametros ingresados coinciden'''
#     superficie = 0
#     print(type(dato))
#     if dato["tipo"] == "Rectangulo":
#         superficie = dato["base"] * dato["altura"]
#     elif dato["tipo"] == "Triangulo":
#         superficie = float(dato["base"]) *float(dato["altura"]) / 2
#     elif dato["tipo"] == "Circulo":
#         superficie = float(dato["radio"]) ** 2  * 3.1416
#     else:
#         print("No puedo calcular la superficie")
#     if superficie != 0:
#         print("La superficie del %s es de %.2f" %(dato["tipo"].lower(),superficie))


# superficie(base = 20, altura = 30, tipo = "Rectangulo")
# superficie(radio=10,base=10,tipo="Circulo")


#return
# def promedio(*muestras):
#     return (len(muestras), sum(muestras)/len(muestras))

# media = promedio(1,3,5,8,11,24,90,29)
# print(type(media))
# print(media)
# print('El promedio de la muestra de %d elementos es %.3f.'%(media))

#funciones anidadas
# def lista_primos(limite):
#     '''Genera una lista de los numeros primos comprendidos entre el 2 y el valor de limite'''    
#     #la lista inicia con el numero 2
#     lista = [2]
#     def esprimo(numero):
#         '''valida si el numero es divisble entre algun elemento de Lista'''
#         '''regresa false de lo contrario, regresa True'''
#         for primo in lista:
#             if numero % primo ==0:
#                 return False
#         return True
#     #se realizara una iteracion de cada numero entero desde 3 hasta el 
#     for numero in range(3,limite+1):
#         #si esprimo(numero) regresa True, aniade el valor.
#         #de numero a lista
#         if esprimo(numero):
#             lista.append(numero)
#     return lista
    
# print(lista_primos(200))

# def factorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         fact = numero * factorial(numero-1)
#         return fact
# print(factorial(5))

#  TAREA, 10 ejemplos minimo de cada uno
#  manejo de excepciones, funciones de orden superior
#  y decoradores, que es, como se programa, ejemplos
# nombre del programa 7_Tarea o el numero que siga


# funciones lambda o anonimas
# sintaxis: lambda <argumentos>:<codigo>

#las funciones lambda se usan mas que las anonimas

# saluda = lambda texto = 'mundo', ancho = 50 : print('Hola,{}.'.format(texto).center(ancho))

# saluda()
# saluda('mundi', 20)

#funcion lambda con condicional
# lambda <argumentos>:<expresion_1> if <condicion> else <expresion_2>

es_par = lambda numero : True if numero % 2 == 0 else False
print(es_par(2))

factorial = lambda numero: numero * factorial(numero-1) if numero > 1 else 1    
print(factorial(5))
















