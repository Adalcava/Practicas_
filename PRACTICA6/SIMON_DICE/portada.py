'''
Unidad de aprendizaje: Programacion Avanzada
Francisco Rosas Angel Fabian / Boleta: 2023640655
'''

from Ui_PORTADA_SD import *
from PyQt6.QtWidgets import QDialog, QMessageBox
import csv
import sys
import os
import subprocess

class INICIO(QDialog, Ui_Dialog):
    def __init__(self, *parent, **flags):
        super().__init__(*parent, **flags)
        self.setupUi(self)
        
        self.Informacion.clicked.connect(self.Info)
        self.Borrar.clicked.connect(self.Borra)
        self.Iniciar.clicked.connect(self.Juego)
        self.Registrar.clicked.connect(self.Registra)
        self.Salir.clicked.connect(self.salir)  # Conectar el botón Salir con la función salir
        
        self.Cantidad_jugadores.currentIndexChanged.connect(self.cambiar_cantidad_jugadores)
        self.jugadores = []  # Lista para almacenar nombres de jugadores
        self.max_jugadores = 1  # Número máximo de jugadores permitidos (por defecto)
        
        # Establecer el valor predeterminado (1 jugador)
        self.Cantidad_jugadores.setCurrentIndex(0)
        self.cambiar_cantidad_jugadores()  # Actualizar según el valor inicial
        
        self.csv_file = "jugadores.csv"  # Nombre del archivo CSV

    def Info(self):
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Mensaje")
        mensaje.setText("Elija el numero de jugadores y registre el nombre dando click en Registrar por cada nombre que ingrese, posteriormente inicie el juego. Si se equivoca en el numero de jugadores borre el registro e ingrese los datos de nuevo.")
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.exec()
    
    def cambiar_cantidad_jugadores(self):
        # Limpiar la lista de jugadores al cambiar el número de jugadores seleccionado
        self.jugadores = []
        self.lista.clear()
        cantidad = int(self.Cantidad_jugadores.currentText())
        self.lista.setPlaceholderText(f"Ingrese nombres de {cantidad} jugadores")
        self.max_jugadores = cantidad  # Actualizar el número máximo de jugadores
    
    def Juego(self):
        directorio_actual = os.path.dirname(sys.argv[0])
        # Nombre del script que quieres abrir
        nombre_script1 = "interfaz.py"
        # Ruta completa al script que quieres abrir
        ruta_script1 = os.path.join(directorio_actual, nombre_script1)
        # Comando para ejecutar el otro script
        comando = [sys.executable, ruta_script1]
        # Ejecutar el otro script
        subprocess.run(comando)
        self.close()
        
    def Borra(self):
        # Limpiar la lista de jugadores y el widget lista
        self.jugadores = []
        self.lista.clear()
        
        # Borrar el archivo CSV si existe
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
            mensaje_aviso = QMessageBox()
            mensaje_aviso.setWindowTitle("Aviso")
            mensaje_aviso.setText("Registros borrados y archivo CSV eliminado.")
            mensaje_aviso.setIcon(QMessageBox.Icon.Warning)
            mensaje_aviso.exec()
        else:
            mensaje_aviso = QMessageBox()
            mensaje_aviso.setWindowTitle("Aviso")
            mensaje_aviso.setText("No hay registros para borrar.")
            mensaje_aviso.setIcon(QMessageBox.Icon.Warning)
            mensaje_aviso.exec()
    
    def Registra(self):
        if len(self.jugadores) >= self.max_jugadores:
            # Ya se alcanzó el máximo de jugadores permitidos
            mensaje_aviso = QMessageBox()
            mensaje_aviso.setWindowTitle("Error")
            mensaje_aviso.setText(f"No se pueden agregar más de {self.max_jugadores} jugadores.")
            mensaje_aviso.setIcon(QMessageBox.Icon.Critical)
            mensaje_aviso.exec()
        else:
            jugador = self.lista.text().strip()
            if jugador:
                self.jugadores.append(jugador)
                self.lista.clear()
                cantidad = int(self.Cantidad_jugadores.currentText())
                if len(self.jugadores) < cantidad:
                    self.lista.setPlaceholderText(f"Ingrese nombres de {cantidad} jugadores")
                    self.lista.setFocus()
                
                # Guardar jugador en el archivo CSV
                with open(self.csv_file, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([jugador])
            else:
                mensaje_error = QMessageBox()
                mensaje_error.setWindowTitle("Error")
                mensaje_error.setText("Por favor ingrese un nombre válido.")
                mensaje_error.setIcon(QMessageBox.Icon.Critical)
                mensaje_error.exec()
    
    def salir(self):
        # Eliminar el archivo CSV al salir de la aplicación si existe
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        
        # Salir de la aplicación
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = INICIO()
    window.show()
    sys.exit(app.exec())
