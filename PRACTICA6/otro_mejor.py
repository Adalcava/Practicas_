import pyfirmata
import random
import time
import inspect
import sys

# Definición de pines
BUZZER = 10
ENTRADA_A = 2
ENTRADA_B = 3
ENTRADA_C = 4
ENTRADA_D = 5
SALIDA_A = 6
SALIDA_B = 7
SALIDA_C = 8
SALIDA_D = 9

# Configurar la placa Arduino
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
board = pyfirmata.Arduino('COM6')  # Reemplaza '/dev/ttyACM0' con el puerto de tu Arduino
it = pyfirmata.util.Iterator(board)
it.start()

board.digital[2].mode = pyfirmata.INPUT
board.digital[3].mode = pyfirmata.INPUT
board.digital[4].mode = pyfirmata.INPUT
board.digital[5].mode = pyfirmata.INPUT

pin11 = board.get_pin('d:11:s') # s para servo
angle = 0
angles = []

secuencia=[]
i=1
nivel=[i]
usuario=[]

def secuencia_usuario(self):
    a=1
    
    while a <= len(self):
        
        lectura_A = board.digital[2].read()
        lectura_B = board.digital[3].read()
        lectura_C = board.digital[4].read()
        lectura_D = board.digital[5].read()
        
        if lectura_A is True:
            usuario.append(6)
            board.digital[6].write(1)
            time.sleep(0.5)
            board.digital[6].write(0)
            a+=1
        elif lectura_B is True:
            usuario.append(7)
            board.digital[7].write(1)
            time.sleep(0.5)
            board.digital[7].write(0)
            a+=1
        elif lectura_C is True:
            usuario.append(8)
            board.digital[8].write(1)
            time.sleep(0.5)
            board.digital[8].write(0)
            a+=1
        elif lectura_D is True:
            usuario.append(9)
            board.digital[9].write(1)
            time.sleep(0.5)
            board.digital[9].write(0)
            a+=1

        time.sleep(0.15)
    
def comparar(a,b):
    if a==b:
        print('tas bien siguiente')
    else:
        print('tas mal')
        pass
        
def azar(self):
    for i in self:
        pin=random.randint(6,9)
        secuencia.append(pin)
        board.digital[pin].write(1)
        time.sleep(1)
        board.digital[pin].write(0)
        time.sleep(1)
        i+=1
        
def jugar_1():
    global i, secuencia, usuario, nivel
    while True:
        usuario=[]
        secuencia=[]
        azar(nivel)
        time.sleep(0.5)
        print(secuencia)
        board.digital[BUZZER].write(1)
        time.sleep(1)
        board.digital[BUZZER].write(0)
        time.sleep(1)
        secuencia_usuario(nivel)
        print(usuario)

        i+=1
        nivel.append(i)
        
        comparar(usuario, secuencia)
        time.sleep(1)

def jugar_2():
    global i, secuencia, usuario, nivel, angles, angle
    angles=[18,54]
    
    while True:
        if len(angles)==0:
            print('termino el juego')
        else:
            angle=random.choice(angles)
            pin11.write(angle)
            angles.remove(angle)
            jugar_1()
        
        
    
    
num_jugadores=int(input('BIENVENIDO: INGRESE EL NUMERO DE JUGADORES: '))

if num_jugadores==1:
    jugar_1()
    
    
elif num_jugadores==2: 
    jugar_2()
    

    
    
        

