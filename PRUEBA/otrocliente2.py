from PyQt6.QtCore import QPropertyAnimation, QRect, QThread, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QDialog, QFileDialog
from PyQt6.QtGui import QPixmap
from Ui_mainwindow import *
from Ui_ventanachat2 import *
import sys
import socket
import winsound
import pyfirmata
import time
import inspect





class ThreadSocket(QThread):
    signal_message = pyqtSignal(str)
    
    def __init__(self, host, port, name):
        super().__init__()
        self.host = host
        self.port = port
        self.name = name

    def run(self):
        global connected, server
        try:
            server.connect((self.host, self.port))
            connected = True
            server.send(bytes(f"<name>{self.name}", 'utf-8'))
            while connected:
                message = server.recv(BUFFER_SIZE)
                if message:
                    self.signal_message.emit(message.decode("utf-8"))
                else:
                    self.signal_message.emit("<!!disconnected!!>")
                    break
        except Exception as e:
            self.signal_message.emit("<!!error!!>")
        finally:
            server.close()
            connected = False

    def stop(self):
        global connected
        connected = False
        self.wait()

class ventana_chat(QDialog, Ui_Dialog):
    def __init__(self, nombre_usuario, servidor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.nombre_usuario = nombre_usuario
        self.servidor = servidor

        self.coneccion = ThreadSocket(servidor, 5004, nombre_usuario)
        self.coneccion.signal_message.connect(self.mensage_entrante)
        self.coneccion.start()
        
        self.enviar.clicked.connect(self.enviar_mensaje)
        self.cfoto.clicked.connect(self.cambiarfoto)
        self.zumbido.clicked.connect(self.enviar_zumbido)
        self.listaamigos.currentIndexChanged.connect(self.mensajeprivado) 

    def enviar_mensaje(self):
        mensaje = self.escribir_mensaje.text()
        if mensaje and connected:
            server.send(bytes(mensaje, 'utf-8'))
            self.escribir_mensaje.clear()
            self.mensage_entrante(f"<Tú> {mensaje}\n")

    def cambiarfoto(self):
        foto_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar foto de perfil", "", "Images (*.png *.xpm *.jpg)")
        if foto_path:
            self.fotoperfil2.setPixmap(QPixmap(foto_path))
            if connected:
                server.send(bytes(f"", 'utf-8'))

                
    def mensajeprivado(self):
        persona=self.listaamigos.currentText()
        if persona=='Tigre':
            self.escribir_mensaje.setText("/sendto Tigre (PRIVADO) → ")
        elif persona=='Ricardo':
            self.escribir_mensaje.setText("/sendto Ricardo (PRIVADO) → ")
        elif persona=='Todos':
            self.escribir_mensaje.setText("")        
            
    def enviar_zumbido(self):
        zum = '/zumbido/'
        if connected:
            server.send(bytes(zum, 'utf-8'))

    def recibir_zumbido(self):       
        original_geometry = self.geometry()
        frequency = 1000  # Frecuencia en Hertz
        duration = 500    # Duración en milisegundos
        winsound.Beep(frequency, duration)

        self.anim = QPropertyAnimation(self, b'geometry')
        self.anim.setDuration(100)  # Duración de cada paso de la animación en milisegundos

        # Crear una secuencia de vibración
        shake_values = []
        offset = 10  # El desplazamiento de la vibración
        for _ in range(10):  # Numero de movimientos
            shake_values.append(QRect(original_geometry.x() + offset, original_geometry.y(), original_geometry.width(), original_geometry.height()))
            shake_values.append(QRect(original_geometry.x() - offset, original_geometry.y(), original_geometry.width(), original_geometry.height()))
            offset = -offset  # Alternar el desplazamiento

        shake_values.append(original_geometry)

        for i, value in enumerate(shake_values):
            self.anim.setKeyValueAt(i / len(shake_values), value)

        self.anim.start()

    def mensage_entrante(self, mensaje):
        if mensaje == '/zumbido/':
            self.recibir_zumbido()
        elif mensaje.startswith('/foto/'):
            foto_path = mensaje.split('/foto/')[1]
            self.fotoperfil1.setPixmap(QPixmap(foto_path))
        else:
            if mensaje.startswith('<Tigre>'):
                self.fotoperfil1.setPixmap(QPixmap('TIGRE.jpg'))
            elif mensaje.startswith('<Ricardo>'):
                self.fotoperfil1.setPixmap(QPixmap('RICHIE.jpg'))
            self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText() + mensaje)
            for i in range(1):
                winsound.Beep(440, 150)
                winsound.Beep(523, 150)# Tono La (A) durante 500 ms
                time.sleep(1)
                i+=1

class ventana_inicio(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.conneccion = None
        self.setupUi(self)
        self.Ingresar.clicked.connect(self.cambiar_ventana)

    def cambiar_ventana(self):
        nombre_usuario = self.lineEdit.text()
        servidor = self.lineEdit_2.text()
        ventana = ventana_chat(nombre_usuario, servidor)
        ventana.exec()

if __name__ == "__main__":
    nombre_usuario = ""
    servidor = ""
    BUFFER_SIZE = 1024  # Usamos un número pequeño para tener una respuesta rápida
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    app = QtWidgets.QApplication(sys.argv)
    window = ventana_inicio()
    window.show()
    sys.exit(app.exec())

