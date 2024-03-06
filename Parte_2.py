'''
Cabrera Vazquez Adalberto
No. boleta: 2023640791
Practica 2
06/03/2024
'''
#Importar bibliotecas necesarias
import numpy as np
import os

#Crear la clase alumnos con todos sus atributos
class Alumno:
    def __init__(self, nombre:str, apellidop:str, apellidom:str, noboleta:int, nacimiento:str, carrera:str, grupo:str, correo:str)->None:
        self.__nombre = nombre
        self.__apellidop = apellidop
        self.__apellidom = apellidom
        self.__noboleta = noboleta
        self.__nacimiento = nacimiento
        self.__carrera = carrera
        self.__grupo = grupo
        self.__correo= correo
    #Definir que va a hacer cuando se mande a imprimir      
    def __str__(self) ->str:
        return f'{i+1}. {self.__apellidop} {self.__apellidom}, {self.__nombre} --- {self.__noboleta} --- {self.__nacimiento} ---\n{self.__carrera} --- {self.__grupo} --- {self.__correo}\n'
    
#Crear la clase Profesor
class Profesor:
    def __init__(self, nombrep:str, empleado:str) -> None:
        self.__nombrep= nombrep
        self.__empleado= empleado
    #Definir que va a hacer cuando se mande a imprimir
    def __str__(self) ->str:
        return f'Profesor: {self.__nombrep}\nNo. Empleado: {self.__empleado}'

#Crear el objeto llamado profesor y posteriormente agregas el numero de alumnos que va a registrar
profesor =Profesor(str(input('Favor de ingresar tu nombre: ')),int(input('No. Empleado:')))
noalumnos=int(input('Favor de ingresar el numero de alumnos que va a registrar: '))

os.system('cls')
#Creacion de la lista de alumnos
lista_alumnos=[]
#Bucle para registar a los alumnos y agregarlos en  la lista creando objetos llamados alumnos con la clase de Alumnos
for i in range(noalumnos):
    print('Alumno '+str(i+1))
    alumno=Alumno(str(input('Nombre del alumno: ')), str(input('Apellido paterno del alumno: ')), str(input('Apellido materno del alumno: ')),int(input('No.boleta del alumno: ')), str(input('Fecha de nacimiento (DD/MM/AAAA): ')),str(input('Carrera: ')), str(input('Grupo: ')),str(input('Correo institucional: ')))
    lista_alumnos.append(alumno)
    print('\n')
    i+=1
    
os.system('cls')
#Imprime el objeto de profesor
print(profesor)
print('*'*100)
print('Lista de alumnos inscritos')
print('*'*100)
#Imprime la lista de objetos(alumnos)
for i in range(noalumnos):
    print(lista_alumnos[i])
    i+=1
print('*'*100)
print('Total de alumnos incritos: '+str(noalumnos))