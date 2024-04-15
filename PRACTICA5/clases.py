'''
PRACTICA 5
05  de Abril del 2024
Cabrera Vazuez Adalberto
2023640791
'''

from abc import ABCMeta, abstractmethod
import numpy as np
import os

#Super clase mascota
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

class Domestica(Mascota):
    def __init__(self, nombre, edad, dueño, tipo, factorTernura:str):
        super().__init__(nombre, edad, dueño, tipo)
        self.__factorTernura= factorTernura
        
    @property
    def factorTernura(self):
        return self.__factorTernura
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\nEdad: {self.edad} años\nDueño: {self.dueño}\nTipo de mascota:  {self.tipo}\nFacotor de Ternura: {self.factorTernura}'
#sub sub clase que heredade domestica
class Gato(Domestica):
    def __init__(self, nombre, edad, dueño, tipo, factorTernura: str):
        super().__init__(nombre, edad, dueño, tipo, factorTernura)
        
    def habla(self, msj):
        return (f'\nLos gatos dicen {msj}')
#sub sub clase que hereda de domestica
class Perro(Domestica):
    def __init__(self, nombre, edad, dueño, tipo, factorTernura: str):
        super().__init__(nombre, edad, dueño, tipo, factorTernura)
        
    def habla(self, msj):
        return (f'\nLos perros dicen {msj}')
#sub clase que hereda de mascota
class Exotica(Mascota):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro:str) -> None:
        super().__init__(nombre, edad, dueño, tipo)
        self.__factorPeligro=factorPeligro
        
    @property
    def factorPeligro(self):
        return self.__factorPeligro
        
    def __str__(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad} años\nDueño: {self.dueño}\nTipo de mascota: {self.tipo}\nFactor de peligro: {self.factorPeligro}'
#sub sub clase que hereda de exotica
class Vibora(Exotica):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro: str) -> None:
        super().__init__(nombre, edad, dueño, tipo, factorPeligro)

    def habla(self, msj):
        return (f'\nLas viboras dicen {msj}')
#sub sub clase que hereda de exotica
class Tigre(Exotica):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro: str) -> None:
        super().__init__(nombre, edad, dueño, tipo, factorPeligro)
        
    def habla(self, msj):
        return (f'\nLos tigres dicen {msj}')
#sub sub clase que hereda de exotica
class Dinosaurio(Exotica):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro: str) -> None:
        super().__init__(nombre, edad, dueño, tipo, factorPeligro)
#sub subsub clase que hereda de exotica
class Brontosaurio(Dinosaurio):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro: str) -> None:
        super().__init__(nombre, edad, dueño, tipo, factorPeligro)
    
    def habla(self, msj):
        return (f'\nLos brontosaurios dicen {msj}')
#sub subsub clase que hereda de exotica  
class Raptor(Dinosaurio):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro: str) -> None:
        super().__init__(nombre, edad, dueño, tipo, factorPeligro)
    
    def habla(self, msj):
        return (f'\nLos raptors dicen {msj}') 
#sub subsub clase que hereda de exotica
class TRex(Dinosaurio):
    def __init__(self, nombre: str, edad: int, dueño: str, tipo: str, factorPeligro: str) -> None:
        super().__init__(nombre, edad, dueño, tipo, factorPeligro)
    
    def habla(self, msj):
        return (f'\nLos TRex dicen {msj}')

class Lista:
    def __init__(self ) -> None:
        self.__listamascotas = []
        
    def agregarmascota(self, elemento):
        self.__listamascotas.append(elemento)
        with open('PRACTICA5/reporte_inventario.txt', 'a') as archivo:
            # Escribe información en el archivo
                
                archivo.write('\n')
                archivo.write('*'*100)
                archivo.write('\n')
                archivo.write('AGREGANDO MASCOTA...\n')
                archivo.write(str(elemento))
                archivo.write('\n')
                
                
    def mostrarmascota(self):
        for elemento in self.__listamascotas:
            print('*'*80)
            print(elemento)
          
    def buscarnombre(self,nombre):
        for otro in self.__listamascotas:
            if otro.nombre == nombre:
                return otro
        return None
    
    def eliminarcontacto(self, otro):
        with open('PRACTICA5/reporte_inventario.txt', 'a') as archivo:
            # Escribe información en el archivo
                
                archivo.write('\n')
                archivo.write('*'*100)
                archivo.write('\n')
                archivo.write('MASCOTA VENDIDA: ')
                archivo.write(str(otro))
                archivo.write('\n')
                
    '''
with open('PRACTICA5/reporte.txt', 'w') as archivo1:
    # Escribe información en el archivo
    archivo1.write('Hola, mundo!\n')
    archivo1.write('Otra línea de texto ola otravezaxdas\n')'''