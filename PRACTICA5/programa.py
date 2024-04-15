from PyQt6.QtCore import Qt
from Ui_vender import *
from Ui_administrar import *
from Ui_MASCOTAS import *
from Ui_reporte import *
from PyQt6.QtWidgets import QMainWindow, QDialog, QWidget, QMessageBox, QApplication
import sys
import clases as cd

lista_animales = cd.Lista()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        
        self.btn_administrar.clicked.connect(self.showAdmin)
        self.btn_vender.clicked.connect(self.showVender)
        self.btn_reporte.clicked.connect(self.showReporte)

    def showAdmin(self):
        DialogoAdmin(self, Qt.WindowType.Dialog).exec()
        
    def showVender(self):
        DialogoVender(self, Qt.WindowType.Dialog).exec()
        
    def showReporte(self):
        DialogoReporte(self, Qt.WindowType.Dialog).exec()

        
class DialogoAdmin(QDialog, Ui_admin):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__(parent, flags)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.guardar)
        
        
    def guardar(self):
        NOMBRE = self.nombre.toPlainText()
        EDAD = self.edad.value()
        DUEÑO = self.dueno.toPlainText()
        TIPO = self.comboBox.currentText()
        NIVEL = self.nivel.value()
        
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
            
class DialogoVender(QDialog, Ui_Vender):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__(parent, flags)
        self.setupUi(self)
        lista_animales.mostrarmascota()
        self.pushButton.clicked.connect(self.buscar)
        self.buttonBox.accepted.connect(self.venderlo)
        
    def buscar (self):
        nombreabuscar = self.dueno.toPlainText()
        nombreencontrado = lista_animales.buscarnombre(nombreabuscar)
        if nombreencontrado:
            self.textBrowser.setPlainText('SI SE ENCUENTRA EL ANIMAL EN VENTA')
        else:
            self.textBrowser.setPlainText('NO SE ENCUENTRA EL ANIMAL EN VENTA, BUSQUE OTRO')
    
    def venderlo(self):
        
        mascotaenventa=self.textBrowser.toPlainText()
        if mascotaenventa=='NO SE ENCUENTRA EL ANIMAL EN VENTA, BUSQUE OTRO':
            QMessageBox.warning(self, 'Advertencia', 'No puedes vender una mascota que no este en el inventario')
            
        else: 
            nombreaborrar = self.dueno.toPlainText()
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
        
        with open('PRACTICA5/reporte_inventario.txt', 'r') as f:
                contenido = f.read()
        self.repositorio.setPlainText(contenido)
       

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())