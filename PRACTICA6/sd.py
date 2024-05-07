import pyfirmata
import random
import time
import inspect

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

melodia = [262, 196, 196, 220, 196, 0, 247, 262]
duracion_notas = [4, 8, 8, 4, 4, 4, 4, 4]
nivel_actual = 1
velocidad = 500
NIVEL_MAX = 100
secuencia = [0] * NIVEL_MAX
secuencia_usuario = [0] * NIVEL_MAX

# Configurar la placa Arduino

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
board = pyfirmata.Arduino('COM6')  # Reemplaza '/dev/ttyACM0' con el puerto de tu Arduino

# Configurar los pines como entrada/salida
entrada_pins = [ENTRADA_A, ENTRADA_B, ENTRADA_C, ENTRADA_D]
salida_pins = [SALIDA_A, SALIDA_B, SALIDA_C, SALIDA_D]

for pin in entrada_pins:
    board.digital[pin].mode = pyfirmata.INPUT

for pin in salida_pins:
    board.digital[pin].mode = pyfirmata.OUTPUT
    board.digital[pin].write(0)

# Función para generar la secuencia
def generar_secuencia():
    random.seed()
    for i in range(NIVEL_MAX):
        secuencia[i] = random.randint(2, 5)

# Función para reproducir una melodía de error
def reproducir_melodia_error():
    for i in range(8):
        duracion_nota = 1000 / duracion_notas[i]
        board.digital[BUZZER].write(1)
        board.pass_time(duracion_nota)
        board.digital[BUZZER].write(0)
        pausa_entre_notas = duracion_nota * 1.30
        time.sleep(pausa_entre_notas / 1000.0)

# Función para mostrar la secuencia actual
def mostrar_secuencia():
    for i in range(nivel_actual):
        pin = salida_pins[secuencia[i] - 2]
        board.digital[pin].write(1)
        time.sleep(velocidad / 1000.0)
        board.digital[pin].write(0)
        time.sleep(0.2)

# Función para leer la secuencia ingresada por el usuario
def leer_secuencia():
    for i in range(nivel_actual):
        flag = 0
        while flag == 0:
            if board.digital[ENTRADA_D].read() == 0:
                pin = SALIDA_D
            elif board.digital[ENTRADA_C].read() == 0:
                pin = SALIDA_C
            elif board.digital[ENTRADA_B].read() == 0:
                pin = SALIDA_B
            elif board.digital[ENTRADA_A].read() == 0:
                pin = SALIDA_A
            else:
                continue
            
            board.digital[pin].write(1)
            board.digital[BUZZER].write(1)
            time.sleep(0.3)
            board.digital[BUZZER].write(0)
            secuencia_usuario[i] = pin
            flag = 1
            time.sleep(0.2)
            
            if secuencia_usuario[i] != salida_pins[secuencia[i] - 2]:
                secuencia_error()
                return
            
            board.digital[pin].write(0)

# Función para manejar una secuencia incorrecta
def secuencia_error():
    for pin in salida_pins:
        board.digital[pin].write(1)
    time.sleep(0.25)
    for pin in salida_pins:
        board.digital[pin].write(0)
    time.sleep(0.25)
    reproducir_melodia_error()
    resetear_juego()

# Función para manejar una secuencia correcta
def secuencia_correcta():
    global nivel_actual, velocidad
    if nivel_actual < NIVEL_MAX:
        nivel_actual += 1
    velocidad -= 50
    time.sleep(0.2)

# Función principal
def simon_dice():
    while True:
        if nivel_actual == 1:
            generar_secuencia()
            mostrar_secuencia()
            leer_secuencia()
        else:
            mostrar_secuencia()
            leer_secuencia()

# Reiniciar juego
def resetear_juego():
    global nivel_actual, velocidad
    nivel_actual = 1
    velocidad = 500

try:
    simon_dice()
finally:
    board.exit()
