'''
Unidad de aprendizaje: Programacion Avanzada
Francisco Rosas Angel Fabian / Boleta: 2023640655


from Ui_INTERFAZ import *
from PyQt6.QtWidgets import QMainWindow, QMessageBox
import csv
import sys
import os
import subprocess

class Interfaz(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags):
        super().__init__(*parent, **flags)
        self.setupUi(self)
        
        self.Volver.clicked.connect(self.Regresa)
        self.Salir.clicked.connect(self.close)  # Conectar el botón Salir para cerrar la ventana
        self.closeEvent = self.eliminarCSV  # Conectar el evento de cierre a eliminarCSV
        
        # Conectar la función para mostrar los nombres al mostrar la ventana
        self.showEvent = self.mostrarNombres
        
    def mostrarNombres(self, event):
        # Abrir el archivo CSV y leer los nombres
        nombres = self.leerNombresDesdeCSV()
        
        # Mostrar los nombres en los QLabel correspondientes
        if nombres:
            for i, nombre in enumerate(nombres, start=1):
                if i == 1:
                    self.jugador1.setText(nombre)
                elif i == 2:
                    self.jugador2.setText(nombre)
                elif i == 3:
                    self.jugador3.setText(nombre)
                elif i == 4:
                    self.jugador4.setText(nombre)
                elif i == 5:
                    self.jugador5.setText(nombre)
                    
    def leerNombresDesdeCSV(self):
        nombres = []
        try:
            with open("jugadores.csv", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Asegurarse de que la fila no esté vacía
                        nombres.append(row[0])  # Agregar el nombre del jugador
        except FileNotFoundError:
            # Si no se encuentra el archivo CSV, mostrar un mensaje de advertencia
            QMessageBox.warning(self, "Archivo no encontrado", "No se encontró el archivo CSV.")
        
        return nombres

    def Regresa(self):
        directorio_actual = os.path.dirname(sys.argv[0])
        # Nombre del script que quieres abrir
        nombre_script2 = "portada.py"
        # Ruta completa al script que quieres abrir
        ruta_script2 = os.path.join(directorio_actual, nombre_script2)
        # Comando para ejecutar el otro script
        comando = [sys.executable, ruta_script2]
        # Ejecutar el otro script
        subprocess.run(comando)
        self.eliminarCSV()
        self.close()
    
    def eliminarCSV(self, event):
        # Eliminar el archivo CSV si existe al cerrar la ventana
        csv_file = "jugadores.csv"
        if os.path.exists(csv_file):
            os.remove(csv_file)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Interfaz()
    window.show()
    sys.exit(app.exec())'''
    
import pyfirmata
import random
import time
import sys
import winsound
from PyQt6 import QtCore, QtGui, QtWidgets
from Ui_INTERFAZ import Ui_MainWindow
import csv
import os
import subprocess
import inspect

# Definición de pines
BUZZER = 12
ROJO = 10
VERDE = 9
AMARILLO = 8
NARANJA = 7
SERVO = 11

# Configurar la placa Arduino
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
board = pyfirmata.Arduino('COM5')  # Reemplaza '/dev/ttyACM0' con el puerto de tu Arduino
it = pyfirmata.util.Iterator(board)
it.start()

# Ángulos para los jugadores
ANGULOS = {
    1: 36,
    2: 72,
    3: 108,
    4: 144,
    5: 180
}

class SimonDice(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.jugadores = []  # Lista para almacenar los jugadores activos
        self.nivel = 1  # Nivel inicial del juego
        self.siguiente_angulo = None  # Angulo del servo para el próximo jugador
        self.servo = None  # Objeto para el servo
        self.pausado = False  # Estado de pausa del juego
        self.init_board()  # Inicializar placa Arduino y servo

        self.Volver.clicked.connect(self.regresar)
        self.Salir.clicked.connect(self.close)
        self.Reiniciar.clicked.connect(self.reiniciar_juego)
        self.PausaContinua.clicked.connect(self.pausar_continuar_juego)

    def init_board(self):
        try:
            board = pyfirmata.Arduino('COM5')  # Reemplazar con el puerto correcto
            self.servo = board.get_pin('d:11:s')  # Configurar el pin 11 como servo
        except:
            print("Error al inicializar la placa Arduino.")

    def generar_secuencia(self):
        secuencia = []
        for _ in range(self.nivel):
            secuencia.append(random.randint(3, 6))  # Generar secuencia de pines (3 a 6)
        return secuencia

    def reproducir_secuencia(self, secuencia):
        for pin in secuencia:
            self.encender_led(pin)
            self.reproducir_sonido(pin)
            time.sleep(1)
            self.apagar_led(pin)
            time.sleep(0.5)

    def encender_led(self, pin):
        if pin == 6:
            self.servo.write(ANGULOS[len(self.jugadores)])  # Configurar ángulo del servo
        else:
            board.digital[pin].write(1)

    def apagar_led(self, pin):
        if pin != 6:
            board.digital[pin].write(0)

    def reproducir_sonido(self, pin):
        if pin == ROJO:
            winsound.Beep(440, 500)  # Tono La (A) durante 500 ms
        elif pin == VERDE:
            winsound.Beep(523, 500)  # Tono Do# (C#) durante 500 ms
        elif pin == AMARILLO:
            winsound.Beep(587, 500)  # Tono Re# (D#) durante 500 ms
        elif pin == NARANJA:
            winsound.Beep(659, 500)  # Tono Fa# (F#) durante 500 ms

    def recibir_secuencia(self):
        usuario = []
        while len(usuario) < self.nivel:
            for pin in [ROJO, VERDE, AMARILLO, NARANJA]:
                if board.digital[pin].read() == 0:
                    usuario.append(pin)
                    self.encender_led(pin)
                    self.reproducir_sonido(pin)
                    time.sleep(0.5)
                    self.apagar_led(pin)
                    time.sleep(0.15)
        return usuario

    def comparar_secuencias(self, secuencia, usuario):
        if secuencia == usuario:
            return True
        else:
            return False

    def iniciar_juego(self):
        while True:
            if self.pausado:
                time.sleep(0.5)  # Esperar medio segundo antes de continuar
                continue  # Saltar a la próxima iteración del bucle si está pausado

            secuencia = self.generar_secuencia()
            self.reproducir_secuencia(secuencia)
            usuario = self.recibir_secuencia()
            if not self.comparar_secuencias(secuencia, usuario):
                self.mostrar_mensaje_eliminar()
                self.jugadores.pop(0)  # Eliminar jugador fallido
                if len(self.jugadores) == 1:
                    self.finalizar_juego()
                    break
            else:
                self.actualizar_puntajes()
                self.nivel += 1

    def mostrar_mensaje_eliminar(self):
        for i, jugador in enumerate(self.jugadores, start=1):
            getattr(self, f"mensaje{i}").setText("eliminado")

    def actualizar_puntajes(self):
        for i, jugador in enumerate(self.jugadores, start=1):
            getattr(self, f"score{i}").setText(str(self.nivel - 1))

    def finalizar_juego(self):
        if len(self.jugadores) == 1:
            self.Ganador.setText(f"Gana {self.jugadores[0]}")
        else:
            self.Ganador.setText("Nadie gana")

    def Regresa(self):
        directorio_actual = os.path.dirname(sys.argv[0])
        # Nombre del script que quieres abrir
        nombre_script2 = "portada.py"
        # Ruta completa al script que quieres abrir
        ruta_script2 = os.path.join(directorio_actual, nombre_script2)
        # Comando para ejecutar el otro script
        comando = [sys.executable, ruta_script2]
        # Ejecutar el otro script
        subprocess.run(comando)
        self.eliminarCSV()
        self.close()
    
    def eliminarCSV(self, event):
        # Eliminar el archivo CSV si existe al cerrar la ventana
        csv_file = "jugadores.csv"
        if os.path.exists(csv_file):
            os.remove(csv_file)

    def reiniciar_juego(self):
        # Implementa la función para reiniciar el juego
        self.jugadores = []
        self.nivel = 1
        self.pausado = False
        # Reiniciar los puntajes en la interfaz
        for i in range(1, 6):
            getattr(self, f"score{i}").setText("")
        self.iniciar_juego()

    def pausar_continuar_juego(self):
        self.pausado = not self.pausado
        if not self.pausado:
            self.iniciar_juego()  # Reanudar el juego si estaba pausado

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SimonDice()
    window.show()
    window.iniciar_juego()  # Iniciar el juego automáticamente al abrir la ventana
    sys.exit(app.exec())
