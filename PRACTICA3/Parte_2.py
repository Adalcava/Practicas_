'''
Cabrera Vazquez Adalberto
No. boleta: 2023640791
Practica 3
10/03/2024
'''
from abc import ABCMeta, abstractmethod
import numpy as np
import os

class Mascota:
    def __init__(self, nombre:str, edad: int, dueño:str, tipo:str) -> None:
        self.__nombre= nombre
        self.__edad= edad
        self.__dueño= dueño
        self.__tipo= tipo
        
    @property
    def dueño(self):
        return self.__dueño
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def tipo(self):
        return self.__tipo
    
    @abstractmethod
    def habla(self, msj):
        pass
    
    #def __str__(self)->str:
     #   return f'Mi nombre es {self.nombre}, mi edad es de {self.edad} años, mi dueño se llama {self.dueño}, y soy unamascota de tipo {self.tipo}'
        
class Domestica(Mascota):
    def __init__(self, nombre, edad, dueño, tipo, factorTernura:str):
        super().__init__(nombre, edad, dueño, tipo)
        self.__factorTernura= factorTernura
        
    @property
    def factorTernura(self):
        return self.__factorTernura
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}-- Edad: {self.edad} años-- Dueño: {self.dueño}-- Tipo de mascota:  {self.tipo} --Facotor de Ternura {self.factorTernura}'
       
class Gato(Domestica):
    def __init__(self, nombre, edad, dueño, tipo, factorTernura: str):
        super().__init__(nombre, edad, dueño, tipo, factorTernura)
        
    def habla(self, msj):
        return (f'\nLos gatos dicen {msj}')
    
class Perro(Domestica):
    def __init__(self, nombre, edad, dueño, tipo, factorTernura: str):
        super().__init__(nombre, edad, dueño, tipo, factorTernura)
        
    def habla(self, msj):
        return (f'\nLos perros dicen {msj}')
    
class Exotica(Mascota):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro:str) -> None:
        super().__init__(nombre, edad, dueño, tipo)
        self.__factorPeligro=factorPeligro
        
    @property
    def factorPeligro(self):
        return self.__factorPeligro
        
    def __str__(self):
        return f'Nombre: {self.nombre}-- Edad: {self.edad} años---Dueño: {self.dueño}---Tipo de mascota: {self.tipo}--Factor de peligro: {self.factorPeligro}'
        
class Vibora(Exotica):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro: str) -> None:
        super().__init__(nombre, edad, dueño, tipo, factorPeligro)

    def habla(self, msj):
        return (f'\nLas viboras dicen {msj}')
    
class Tigre(Exotica):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro: str) -> None:
        super().__init__(nombre, edad, dueño, tipo, factorPeligro)
        
    def habla(self, msj):
        return (f'\nLos tigres dicen {msj}')
    
class Dinosaurio(Exotica):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro: str) -> None:
        super().__init__(nombre, edad, dueño, tipo, factorPeligro)

    
class Brontosaurio(Dinosaurio):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro: str) -> None:
        super().__init__(nombre, edad, dueño, tipo, factorPeligro)
    
    def habla(self, msj):
        return (f'\nLos brontosaurios dicen {msj}')
        
class Raptor(Dinosaurio):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro: str) -> None:
        super().__init__(nombre, edad, dueño, tipo, factorPeligro)
    
    def habla(self, msj):
        return (f'\nLos raptors dicen {msj}') 
    
class TRex(Dinosaurio):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro: str) -> None:
        super().__init__(nombre, edad, dueño, tipo, factorPeligro)
    
    def habla(self, msj):
        return (f'\nLos TRex dicen {msj}')
    
os.system('cls')
lista_animales=[]
flag= False
while flag==False:
    os.system('cls')
    print('BIENVENIDO A LA TIENDA DE MASCOTAS\n¿Que desea comprar el dia de hoy?:\n1. Domestica\n   1.1 Gato\n   1.2 Perro')
    print('2. Exótica\n   2.1 Vivora\n   2.2 Tigre\n   2.3 Dinosaurio\n      2.3.1 Brontosaurio\n      2.3.2 Raptor\n      2.3.3 TRex')
    print('3. Mostrar a mis animales\n4. Salir')
    opcion=str(input('Ingrese la opcion que desee:'))
    if opcion=='1.1':
        os.system('cls')
        print('Escogiste registrar un gato.\n')
        gato=Gato(str(input('Ingrese el nombre: ')), input('Ingrese edad: '), input('Ingrese su dueño: '), 'Domestico (Gato)', input('Ingrese el factor de ternura:'))
        lista_animales.append(gato)
        print(gato.habla('MIAU MIAU'))
        
        
        input('\nPresiona cualquier tecla para continuar')
    elif opcion=='1.2':
        os.system('cls')
        print('Escogiste registrar un Perro.\n')
        perro= Perro(str(input('Ingrese el nombre: ')), input('Ingrese edad: '), input('Ingrese su dueño: '), 'Domestico (Perro)', input('Ingrese el factor de ternura:'))
        lista_animales.append(perro)
        print(perro.habla('GUAU GUAU'))
        
        input('\nPresiona cualquier tecla para continuar')
    elif opcion=='2.1':
        os.system('cls')
        print('Escogiste registrar una Vivora.\n')
        vivora= Vibora(str(input('Ingrese el nombre: ')), input('Ingrese edad: '), input('Ingrese su dueño: '), 'Exotico (Vivora)', input('Ingrese el factor de peligro:'))
        lista_animales.append(vivora)
        print(vivora.habla('TSSSS'))
        input('\nPresiona cualquier tecla para continuar')
        
    elif opcion=='2.2':
        os.system('cls')
        print('Escogiste registrar una Tigre.\n')
        tigre= Tigre(str(input('Ingrese el nombre: ')), input('Ingrese edad: '), input('Ingrese su dueño: '), 'Exotico (tigre)', input('Ingrese el factor de peligro:'))
        lista_animales.append(tigre)
        print(tigre.habla('RRRRRAR'))
        input('\nPresiona cualquier tecla para continuar')
    elif opcion=='2.3.1':
        os.system('cls')
        print('Escogiste registrar un dinosaurio (Brontosaurio).\n')
        brontosaurio= Brontosaurio(str(input('Ingrese el nombre: ')), input('Ingrese edad: '), input('Ingrese su dueño: '), 'Exotico( Dinosaurio/Brontosaurio)', input('Ingrese el factor de peligro:'))
        lista_animales.append(brontosaurio)
        print(brontosaurio.habla('LIROLELIROLE'))
        input('\nPresiona cualquier tecla para continuar')
    elif opcion=='2.3.2':
        os.system('cls')
        print('Escogiste registrar un dinosaurio (Raptor).\n')
        raptor= Raptor(str(input('Ingrese el nombre: ')), input('Ingrese edad: '), input('Ingrese su dueño: '), 'Exotico( Dinosaurio/Raptor)', input('Ingrese el factor de peligro:'))
        lista_animales.append(raptor)
        print(raptor.habla('RIRIRIR'))
        input('\nPresiona cualquier tecla para continuar')
    elif opcion=='2.3.3':
        os.system('cls')
        print('Escogiste registrar un dinosaurio (TRex).\n')
        trex= TRex(str(input('Ingrese el nombre: ')), input('Ingrese edad: '), input('Ingrese su dueño: '), 'Exotico( Dinosaurio/TRex)', input('Ingrese el factor de peligro:'))
        lista_animales.append(trex)
        print(trex.habla('RAAAAUR'))
        input('\nPresiona cualquier tecla para continuar')
    elif opcion=='3':
        print('Estas son tus mascotas')
        numero_animales=len(lista_animales)
        
        for i in range(numero_animales):
            print(str(i+1)+'. ', end='')
            print(lista_animales[i])
            i+=1
        
        input('\nPresiona cualquier tecla para continuar')
    elif opcion=='4':
        flag=True
    else:
        print('\nFavor de ingresar un numero valido del menu')
        input('\nPresiona cualquier tecla para continuar')
        os.system('cls')