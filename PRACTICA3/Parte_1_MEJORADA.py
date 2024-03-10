'''
Cabrera Vazquez Adalberto
No. boleta: 2023640791
Practica 3
09/03/2024
'''
from abc import ABCMeta, abstractmethod
import numpy as np
import os
from tabulate import tabulate

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
       
class ComputadoraPortatil(Computadora):
    def __init__(self, memoria, procesador,almacenamiento, gpu, marca:str) -> None:
        super().__init__(memoria, procesador, almacenamiento, gpu)
        self.__marca = marca
    
    @property
    def marca(self):
        return self.__marca

class ComputadoraEscritorio(Computadora):
    def __init__(self, memoria, procesador, almacenamiento, gpu, tamaño:str) ->None:
        super().__init__(memoria, procesador, almacenamiento, gpu)
        self.__tamaño = tamaño
        
    @property
    def tamaño(self):
        return self.__tamaño
    
class TelefonoInteligente(Computadora):
    def __init__(self, memoria, procesador, almacenaminto, gpu, numero:str) ->None:
        super().__init__(memoria, procesador, almacenaminto, gpu)
        self.__numero= numero
    
    @property
    def numero(self):
        return self.__numero

class Tablet(Computadora):
    def __init__(self,memoria, procesador, almacenamiento, gpu, peso:str) ->None:
        super().__init__(memoria,procesador, almacenamiento, gpu)
        self.__peso= peso
    
    @property
    def peso(self):
        return self.__peso
            
portatil_1=ComputadoraPortatil('16', 'Intel® Celeron® G','1T', 'Zotac(20)','Samsung')
portatil_2=ComputadoraPortatil('8', 'AMD Ryzen™ 9', '256 Gb', 'SAPPHIRE(11)', 'Apple')
portatil_3=ComputadoraPortatil('4', 'Intel® Core™ i5-10xxx', '512 Gb', 'ASRock(9)','LENOVO')

escritorio_1=ComputadoraEscritorio('4', 'Intel® Core™ i5-12xxx', '256 Gb','PowerColor(4)', '22000')
escritorio_2=ComputadoraEscritorio('8','AMD Ryzen™ 5', '512 Gb', 'ASUS(60)', '23000')
escritorio_3=ComputadoraEscritorio('8', 'Intel® Core™ i3-10xxx', '1T', 'MSI(26)','21000')

telefono_1=TelefonoInteligente('8', 'Qualcomm Snapdragon 8 Gen 2', '512 Gb', 'Adreno 750', '9984037473')
telefono_2=TelefonoInteligente('4','Apple A16 Bionic', '256 Gb', 'Apple M2 10-Core GPU', '9981007887')
telefono_3=TelefonoInteligente('8' ,'Samsung Exynos 2200', '64 Gb', 'Mali-G615 MP6','9981000105')

tablet_1=Tablet('32',' 1.5GHz Dual-Core Cortex-A9, 1.6GHz', '512 Gb','ARM Mali-T764','500')
tablet_2=Tablet('16','Octa-Core Cortex-A7, 1.6GHz','256 Gb','ARM Mali-450MP6', '460')
tablet_3=Tablet('8','Quad-Core 64Bit Cortex-A53, 2.0GHz','256 Gb','Mali400MP2', '520')



data_portatil=[
    ["Dispositivo",'Memoria [Gb]', 'Procesador', 'Almacenamiento','GPU', 'Marca'],
    ['Portatil 1', portatil_1.memoria, portatil_1.procesador, portatil_1.almacenamiento, portatil_1.gpu, portatil_1.marca],
    ['Portatil 2', portatil_2.memoria, portatil_2.procesador, portatil_2.almacenamiento, portatil_2.gpu, portatil_2.marca],
    ['Portatil 3', portatil_3.memoria, portatil_3.procesador, portatil_3.almacenamiento, portatil_3.gpu, portatil_3.marca]
]

data_escritorio=[
    ["Dispositivo",'Memoria [Gb]', 'Procesador', 'Almacenamiento','GPU', 'Tamaño [cm3]'],
    ['Escritorio 1', escritorio_1.memoria, escritorio_1.procesador, escritorio_1.almacenamiento, escritorio_1.gpu, escritorio_1.tamaño],
    ['Escritorio 2', escritorio_2.memoria, escritorio_2.procesador, escritorio_2.almacenamiento, escritorio_2.gpu, escritorio_2.tamaño],
    ['Escritorio 3', escritorio_3.memoria, escritorio_3.procesador, escritorio_3.almacenamiento, escritorio_3.gpu, escritorio_3.tamaño]
]

data_telefono=[
    ["Dispositivo",'Memoria [Gb]', 'Procesador', 'Almacenamiento','GPU', 'Numero'],
    ['Telefono 1', telefono_1.memoria, telefono_1.procesador, telefono_1.almacenamiento, telefono_1.gpu, telefono_1.numero],
    ['Telefono 2', telefono_2.memoria, telefono_2.procesador, telefono_2.almacenamiento, telefono_2.gpu, telefono_2.numero],
    ['Telefono 3', telefono_3.memoria, telefono_3.procesador, telefono_3.almacenamiento, telefono_3.gpu, telefono_3.numero]
]

data_tablet=[
    ["Dispositivo",'Memoria [Gb]', 'Procesador', 'Almacenamiento','GPU', 'Peso [gr]'],
    ['Tablet 1', tablet_1.memoria, tablet_1.procesador, tablet_1.almacenamiento, tablet_1.gpu, tablet_1.peso],
    ['Tablet 2', tablet_2.memoria, tablet_2.procesador, tablet_2.almacenamiento, tablet_2.gpu, tablet_2.peso],
    ['Tablet 3', tablet_3.memoria, tablet_3.procesador, tablet_3.almacenamiento, tablet_3.gpu, tablet_3.peso]
]

print(tabulate(data_portatil, headers="firstrow", tablefmt="grid"))
print('')
print(tabulate(data_escritorio, headers="firstrow", tablefmt="grid"))
print('')
print(tabulate(data_telefono, headers="firstrow", tablefmt="grid"))
print('')
print(tabulate(data_tablet, headers="firstrow", tablefmt="grid"))