'''
    Cabrera Vazquez Adalberto
    No. boleta: 2023640791
    Practica 2
    06/03/2024
'''

import numpy as np
import os
#Creacion de la clase Persona
class Persona:
    def __init__(self, nombre:str, edad:int, estatura: float, numero:int)->None:
        self.__nombre=nombre
        self.__edad=edad
        self.__estatura=estatura
        self.__numero=numero
        
    def __str__(self) ->str:
        return f'¡Hola!, Mi nombre es {self.__nombre}, tengo {self.__edad} años, nací en {2024-self.__edad}, mido {self.__estatura} metros y mi numero es  {self.__numero}. ¡SALUDOS!'
#Creacion de la lista persona con for para almacenar en lista
lista_personas=[]
for i in range(3):
    print('')
    persona =Persona(str(input('Favor de ingresar tu nombre: ')),int(input('Edad:')),float(input('Estatura:')),int(input('numero telefonico:'))) 
    lista_personas.append(persona)
    i+=1
os.system('cls')
#impresion de la lista
for i in range(3):
    print('Persona '+str(i+1)+':')
    print(lista_personas[i])
    print('')
    i+=1
