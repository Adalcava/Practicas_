'''
Cabrera Vazquez Adalberto
No. boleta: 2023640791
Practica 3
09/03/2024
'''
from abc import ABCMeta, abstractmethod
import numpy as np
import os

os.system('cls')

class Computadora(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, memoria:str, procesador: str, almacenamiento:str, gpu:str) -> None:
        self.__memoria= memoria
        self.__procesador= procesador
        self.__almacenamiento= almacenamiento
        self.__gpu= gpu
        
        #Memoria
    @property
    def memoria(self):
        return self.__memoria
        
    @memoria.setter
    def memoria(self, nuevamemoria:str):
        self.__memoria= nuevamemoria
    # Procesador
    @property
    def procesador(self):
        return self.__procesador
        
    @procesador.setter
    def procesador(self, nuevoproce:str):
        self.__procesador= nuevoproce
    #Almacenamiento
    @property
    def almacenamiento(self):
        return self.__almacenamiento
        
    @almacenamiento.setter
    def almacenamiento(self, nuevoalma:str):
        self.__almacenamiento= nuevoalma
    #GPU
    @property
    def gpu(self):
        return self.__gpu
        
    @gpu.setter
    def gpu(self, nuevogpu:str):
        self.__gpu=nuevogpu
            
    def presentar(self):
        print(f', su memoria es de {self.__memoria} GB, su procesador es un {self.__procesador}, tiene un almacenamiento de {self.__almacenamiento}, y una gpu {self.__gpu}.')
        
class ComputadoraPortatil(Computadora):
    def __init__(self, memoria, procesador,almacenamiento, gpu, marca:str) -> None:
        super().__init__(memoria, procesador, almacenamiento, gpu)
        self.__marca = marca
        
    def __str__(self)->str:
        return f'Hola la computadora portatil es de la marca {self.__marca}'

class ComputadoraEscritorio(Computadora):
    def __init__(self, memoria, procesador, almacenamiento, gpu, tamaño:str) ->None:
        super().__init__(memoria, procesador, almacenamiento, gpu)
        self.__tamaño = tamaño
        
    def __str__(self)-> str:
        return f'Hola la computadora de escritorio tiene un tamaño de {self.__tamaño} cms cúbicos'
    
class TelefonoInteligente(Computadora):
    def __init__(self, memoria, procesador, almacenaminto, gpu, numero:str) ->None:
        super().__init__(memoria, procesador, almacenaminto, gpu)
        self.__numero= numero
    
    def __str__(self)-> str:
        return f'Hola el numero del telefono inteligente es {self.__numero}'

class Tablet(Computadora):
    def __init__(self,memoria, procesador, almacenamiento, gpu, peso:str) ->None:
        super().__init__(memoria,procesador, almacenamiento, gpu)
        self.__peso= peso
    
    def __str__(self)->str:
         return f'Hola el peso es de {self.__peso} gr'
            
portatil_1=ComputadoraPortatil('16', 'Intel® Celeron® G','1T', 'Zotac(20)','Samsung')
portatil_2=ComputadoraPortatil('8', 'AMD Ryzen™ 9', '256 Gb', 'SAPPHIRE(11)', 'Apple')
portatil_3=ComputadoraPortatil('4', 'Intel® Core™ i5-10xxx', '512 Gb', 'ASRock(9)','LENOVO')

escritorio_1=ComputadoraEscritorio('4', 'Intel® Core™ i5-12xxx', '256 Gb','PowerColor(4)', '22000')
escritorio_2=ComputadoraEscritorio('8','AMD Ryzen™ 5', '512 Gb', 'ASUS(60)', '23000')
escritorio_3=ComputadoraEscritorio('8', 'Intel® Core™ i3-10xxx', '1T', 'MSI(26)','21000')

telefono_1=TelefonoInteligente('8', 'Qualcomm Snapdragon 8 Gen 2', '512 Gb', 'Adreno 750', '9984037473')
telefono_2=TelefonoInteligente('4','Apple A16 Bionic', '256 Gb', 'Apple M2 10-Core GPU', '9981007887')
telefono_3=TelefonoInteligente('8' ,'Samsung Exynos 2200', '64 Gb', 'Mali-G615 MP6','9981000105')

tablet_1=Tablet('32',' 1.5GHz	Dual-Core Cortex-A9, 1.6GHz', '512 Gb','ARM Mali-T764','500')
tablet_2=Tablet('16','Octa-Core Cortex-A7, 1.6GHz','256 Gb','ARM Mali-450MP6', '460')
tablet_3=Tablet('8','Quad-Core 64Bit Cortex-A53, 2.0GHz','256 Gb','Mali400MP2', '520')

print('Portatil 1:\n'+ str(portatil_1), end="")
portatil_1.presentar()
print('\nPortatil 2:\n'+ str(portatil_2), end="")
portatil_2.presentar()
print('\nPortatil 3:\n'+ str(portatil_3), end="")
portatil_3.presentar()

print('\nEscritorio 1:\n'+ str(escritorio_1), end="")
escritorio_1.presentar()
print('\nEscritorio 2:\n'+ str(escritorio_2), end="")
escritorio_2.presentar()
print('\nEscritorio 3:\n'+ str(escritorio_3), end="")
escritorio_3.presentar()

print('\nTelefono 1:\n'+ str(telefono_1), end="")
telefono_1.presentar()
print('\nTelefono 2:\n'+ str(telefono_2), end="")
telefono_2.presentar()
print('\nTelefono 3:\n'+ str(telefono_3), end="")
telefono_3.presentar()

print('\nTablet 1:\n'+ str(tablet_1), end="")
tablet_1.presentar()
print('\nTablet 2:\n'+ str(tablet_2), end="")
tablet_2.presentar()
print('\nTablet 3:\n'+ str(tablet_3), end="")
tablet_3.presentar()


