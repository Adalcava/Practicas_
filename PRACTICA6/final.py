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
SERVO_PIN = 11  # Pin para controlar el servo

# Configurar la placa Arduino
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
board = pyfirmata.Arduino('COM6')  # Reemplaza 'COM5'
it = pyfirmata.util.Iterator(board)
it.start()

# Configurar pines de entrada y salida
for pin in [ENTRADA_A, ENTRADA_B, ENTRADA_C, ENTRADA_D]:
    board.digital[pin].mode = pyfirmata.INPUT
for pin in [SALIDA_A, SALIDA_B, SALIDA_C, SALIDA_D]:
    board.digital[pin].mode = pyfirmata.OUTPUT

# Configurar pin para controlar el servo
board.digital[SERVO_PIN].mode = pyfirmata.SERVO

# Lista de jugadores y ángulos disponibles para el servo
num_jugadores = 0
jugadores = []
angles = [36, 72, 108, 144, 180]

def generar_secuencia(nivel):
    secuencia = []
    for _ in range(nivel):
        pin = random.randint(SALIDA_A, SALIDA_D)
        secuencia.append(pin)
        board.digital[pin].write(1)
        time.sleep(1)
        board.digital[pin].write(0)
        time.sleep(0.5)
    return secuencia

def obtener_entrada_usuario(nivel):
    usuario = []
    for _ in range(nivel):
        while True:
            if board.digital[ENTRADA_A].read():
                usuario.append(SALIDA_A)
                board.digital[SALIDA_A].write(1)
                time.sleep(0.5)
                board.digital[SALIDA_A].write(0)
                break
            elif board.digital[ENTRADA_B].read():
                usuario.append(SALIDA_B)
                board.digital[SALIDA_B].write(1)
                time.sleep(0.5)
                board.digital[SALIDA_B].write(0)
                break
            elif board.digital[ENTRADA_C].read():
                usuario.append(SALIDA_C)
                board.digital[SALIDA_C].write(1)
                time.sleep(0.5)
                board.digital[SALIDA_C].write(0)
                break
            elif board.digital[ENTRADA_D].read():
                usuario.append(SALIDA_D)
                board.digital[SALIDA_D].write(1)
                time.sleep(0.5)
                board.digital[SALIDA_D].write(0)
                break
            time.sleep(0.15)
    return usuario

def comparar(secuencia, usuario):
    return secuencia == usuario

def jugar_simon_dice():
    global num_jugadores, jugadores
    
    while len(jugadores) > 1:
        nivel = len(jugadores)  # Nivel basado en la cantidad de jugadores restantes
        secuencia = generar_secuencia(nivel)
        print("Secuencia:", secuencia)
        board.digital[BUZZER].write(1)
        time.sleep(2)
        board.digital[BUZZER].write(0)
        time.sleep(1)
        
        for jugador in jugadores:
            # Asigna el ángulo aleatorio al servo del jugador
            angle = random.choice(angles)
            board.digital[SERVO_PIN].write(angle)
            print(f"Jugador {jugador} (Ángulo: {angle} grados) - Turno de jugar:")
            usuario = obtener_entrada_usuario(nivel)
            print(f"Jugador {jugador} intentó:", usuario)
            
            if not comparar(secuencia, usuario):
                print(f"¡Jugador {jugador} eliminado!")
                jugadores.remove(jugador)  # Eliminar jugador incorrecto
                break
        
        time.sleep(3)  # Tiempo para mostrar resultados y preparar para el siguiente jugador
    
    print(f"¡El jugador {jugadores[0]} es el ganador!")

# Obtener la cantidad de jugadores desde un menú
def obtener_numero_jugadores():
    while True:
        try:
            num = int(input("Ingrese la cantidad de jugadores (entre 1 y 5): "))
            if 1 <= num <= 5:
                return num
            else:
                print("Por favor, ingrese un número válido de jugadores.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def asignar_jugadores_y_angles(num_jugadores):
    global jugadores
    jugadores = list(range(1, num_jugadores + 1))
    random.shuffle(angles)  # Mezclar los ángulos disponibles
    print("Asignación de jugadores y ángulos:")
    for jugador, angle in zip(jugadores, angles):
        print(f"Jugador {jugador} - Ángulo: {angle} grados")

if __name__ == "__main__":
    num_jugadores = obtener_numero_jugadores()
    print(f"Comenzando juego con {num_jugadores} jugadores...")
    asignar_jugadores_y_angles(num_jugadores)
    jugar_simon_dice()
