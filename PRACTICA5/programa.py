'''
PRACTICA 5
05  de Abril del 2024
Cabrera Vazuez Adalberto
2023640791
'''

from PyQt6.QtCore import Qt
from Ui_vender import *
from Ui_administrar import *
from Ui_MASCOTAS import *
from Ui_reporte import *
from PyQt6.QtWidgets import QMainWindow, QDialog, QWidget, QMessageBox, QApplication
import sys
import clases as cd
#Creacion de la lista de animales
lista_animales = cd.Lista()
#Ventana pricipal
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        #Presionar los botones administrar, vender y reporte
        self.btn_administrar.clicked.connect(self.showAdmin) 
        self.btn_vender.clicked.connect(self.showVender)
        self.btn_reporte.clicked.connect(self.showReporte)

    def showAdmin(self):
        DialogoAdmin(self, Qt.WindowType.Dialog).exec() #ejecuta el DialogoAdmin
        
    def showVender(self):
        DialogoVender(self, Qt.WindowType.Dialog).exec()    #ejecuta el DialogoVender
        
    def showReporte(self):
        DialogoReporte(self, Qt.WindowType.Dialog).exec()   #Ejecuta el DialogoReporte

        
class DialogoAdmin(QDialog, Ui_admin):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__(parent, flags)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.guardar) #Cuando presione el boton aceptar entonces ejecutara la funcion guardar
        
        
    def guardar(self):  #Guarda los informacion en variables
        NOMBRE = self.nombre.toPlainText()
        EDAD = self.edad.value()
        DUEÑO = self.dueno.toPlainText()
        TIPO = self.comboBox.currentText()
        NIVEL = self.nivel.value()
        # Dependiendo del tipo de animal crea un objeto del mismo y guarda la informacion
        if TIPO=='Gato':
            mascota=cd.Gato(NOMBRE, EDAD, DUEÑO, TIPO, NIVEL)
            lista_animales.agregarmascota(mascota)
            
            
        elif TIPO=='Perro':
            mascota=cd.Perro(NOMBRE, EDAD, DUEÑO, TIPO, NIVEL)
            lista_animales.agregarmascota(mascota)
            
        
        elif TIPO=='Tigre':
            mascota=cd.Tigre(NOMBRE, EDAD, DUEÑO, TIPO, NIVEL)
            lista_animales.agregarmascota(mascota)
            
        
        elif TIPO=='Vibora':
            mascota=cd.Vibora(NOMBRE, EDAD, DUEÑO, TIPO, NIVEL)
            lista_animales.agregarmascota(mascota)
            
        
        elif TIPO=='Trex':
            mascota=cd.TRex(NOMBRE, EDAD, DUEÑO, TIPO, NIVEL)
            lista_animales.agregarmascota(mascota)
            
            
        elif TIPO=='Velociraptor':
            mascota=cd.Raptor(NOMBRE, EDAD, DUEÑO, TIPO, NIVEL)
            lista_animales.agregarmascota(mascota)
            
            
        elif TIPO=='Brontosaurio':
            mascota=cd.Brontosaurio(NOMBRE, EDAD, DUEÑO, TIPO, NIVEL)
            lista_animales.agregarmascota(mascota)
            
class DialogoVender(QDialog, Ui_Vender):    #Dialogo Vender
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__(parent, flags)
        self.setupUi(self)
        lista_animales.mostrarmascota()
        self.pushButton.clicked.connect(self.buscar)    #Al presionar el boton ejecuta la funcion "buscar"
        self.buttonBox.accepted.connect(self.venderlo)  #Al presionar el boton ejecta la funcion venderlo 
        
    def buscar (self):
        nombreabuscar = self.dueno.toPlainText()    #lee el nombre de la mascota
        nombreencontrado = lista_animales.buscarnombre(nombreabuscar)   #Usa la funcion buscar por nombre de la clase lista
        if nombreencontrado: #Dependiendo de si esta o no, manda un mensaje 
            self.textBrowser.setPlainText('SI SE ENCUENTRA EL ANIMAL EN VENTA') 
        else:
            self.textBrowser.setPlainText('NO SE ENCUENTRA EL ANIMAL EN VENTA, BUSQUE OTRO')
    
    def venderlo(self):
        
        mascotaenventa=self.textBrowser.toPlainText()  #lee lo que esta en el texto
        if mascotaenventa=='NO SE ENCUENTRA EL ANIMAL EN VENTA, BUSQUE OTRO': # si no se encuentra manda una advertencia
            QMessageBox.warning(self, 'Advertencia', 'No puedes vender una mascota que no este en el inventario')
            
        else: 
            nombreaborrar = self.dueno.toPlainText()    #Si si esta reporta y elimina macota
            lista_animales.eliminarcontacto(nombreaborrar)
            lista_animales.mostrarmascota()
        
class DialogoReporte(QDialog, Ui_Reporte):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__(parent, flags)
        self.setupUi(self)
        lista_animales.mostrarmascota()
        '''for elemento in lista_animales:
            self.repositorio.setText('*'*100)
            self.repositorio.setText(elemento)'''
        
        with open('PRACTICA5/reporte_inventario.txt', 'r') as f:    #Lee lo que esta en el archivo de reporte y lo muestra en la caja de texto
                contenido = f.read()
        self.repositorio.setPlainText(contenido)
       

        
if __name__ == "__main__": #Ejecuta la ventana principal
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())