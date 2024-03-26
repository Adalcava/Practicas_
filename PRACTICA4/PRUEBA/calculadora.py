from PyQt6.QtGui import QKeyEvent
from Ui_calculadora import *
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        
        self.btn0.clicked.connect(self.setNumero)
        self.btn1.clicked.connect(self.setNumero)
        self.btn2.clicked.connect(self.setNumero)
        self.btn3.clicked.connect(self.setNumero)
        self.btn4.clicked.connect(self.setNumero)
        self.btn5.clicked.connect(self.setNumero)
        self.btn6.clicked.connect(self.setNumero)
        self.btn7.clicked.connect(self.setNumero)
        self.btn8.clicked.connect(self.setNumero)
        self.btn9.clicked.connect(self.setNumero)
        
        self.btnPunto.clicked.connect(self.setPunto)
        
        self.btnAC.clicked.connect(self.setCero)
        
        self.btnMas.clicked.connect(self.setMas)
        self.btnMenos.clicked.connect(self.setMenos)
        self.btnPor.clicked.connect(self.setMultiplicacion)
        self.btnDivi.clicked.connect(self.setDivision)
        self.btnporcentaje.clicked.connect(self.setPorcentaje)
        self.btninvertor.clicked.connect(self.setInv)
        self.btnIgual.clicked.connect(self.setIgual)
        
    def keyPressEvent(self, key: QKeyEvent) -> None:
        super().keyPressEvent(key)
        if key.key() >= QtCore.Qt.Key.Key_0 and key.key() <= QtCore.Qt.Key.Key_9:
            self.setNumber(key.key()-QtCore.Qt.Key.Key_0)
        elif key.key() == QtCore.Qt.Key.Key_Period:
            self.setPunto()

        
    def setCero(self):
        self.etiqueta.setText("")
        
    def setMenos(self):
        cadena = self.etiqueta.text()
        if cadena.find('+')!=-1 or cadena.find('-')!=-1 or cadena.find('*')!=-1  or cadena.find('%')!=-1 or cadena.find('(+/-)')!=-1:
            pass
        else:
            cadena = cadena + "-"
            self.etiqueta.setText(cadena) 
            
    def setMas(self):
        cadena = self.etiqueta.text()
        if cadena.find('+')!=-1 or cadena.find('-')!=-1 or cadena.find('*')!=-1 or cadena.find('/')!=-1 or cadena.find('%')!=-1 or cadena.find('(+/-)')!=-1:
            pass
        else:
            cadena = cadena + "+"
            self.etiqueta.setText(cadena) 
            
    def setMultiplicacion(self):
        cadena = self.etiqueta.text()
        if cadena.find('+')!=-1 or cadena.find('-')!=-1 or cadena.find('*')!=-1 or cadena.find('/')!=-1 or cadena.find('%')!=-1 or cadena.find('(+/-)')!=-1:
            pass
        else:
            cadena = cadena + "*"
            self.etiqueta.setText(cadena) 
    
    def setDivision(self):
        cadena = self.etiqueta.text()
        if cadena.find('+')!=-1 or cadena.find('-')!=-1 or cadena.find('*')!=-1 or cadena.find('/')!=-1 or cadena.find('%')!=-1 or cadena.find('(+/-)')!=-1:
            pass
        else:
            cadena = cadena + "/"
            self.etiqueta.setText(cadena) 
    
    def setPorcentaje(self):
        cadena = self.etiqueta.text()
        if cadena.find('+')!=-1 or cadena.find('-')!=-1 or cadena.find('*')!=-1 or cadena.find('/')!=-1 or cadena.find('%')!=-1 or cadena.find('(+/-)')!=-1:
            pass
        else:
            cadena = cadena + "% "
            self.etiqueta.setText(cadena) 
            
    def setInv(self):
        cadena=self.etiqueta.text()
        if cadena.find('*')!=-1 or cadena.find('/')!=-1 or cadena.find('%')!=-1 or cadena.find('(+/-)')!=-1:
            pass
        else:
            cadena=cadena+' (inv)'
            self.etiqueta.setText(cadena) 
        
    def setPunto(self):
        cadena = self.etiqueta.text()
        
        
        if (cadena.find('+')==-1 or cadena.find('-')==-1 or cadena.find('*')==-1 or cadena.find('/')==-1 or cadena.find('%')==-1 or cadena.find(' (+/-)')==-1) and cadena.find(".") == -1:
            cadena = cadena + "."
            self.etiqueta.setText(cadena) 
            
        elif cadena.find('+')!=-1 :
            posicion=cadena.find('+')
            if cadena.find('.',posicion)==-1:
                cadena = cadena + "."
                self.etiqueta.setText(cadena) 
                
        elif cadena.find('-')!=-1:
            posicion=cadena.find('-')
            if cadena.find('.',posicion)==-1:
                cadena = cadena + "."
                self.etiqueta.setText(cadena) 
        
        elif cadena.find('*')!=-1:
            posicion=cadena.find('*')
            if cadena.find('.',posicion)==-1:
                cadena = cadena + "."
                self.etiqueta.setText(cadena)
        
        elif cadena.find('/')!=-1:
            posicion=cadena.find('/')
            if cadena.find('.',posicion)==-1:
                cadena = cadena + "."
                self.etiqueta.setText(cadena)
        
        elif cadena.find('%')!=-1:
            posicion=cadena.find('%')
            if cadena.find('.',posicion)==-1:
                cadena = cadena + "."
                self.etiqueta.setText(cadena)
                
        elif cadena.find('(+/-)')!=-1:
            print('hola')
    
    def setNumber(self, numero:int):
        cadena = self.etiqueta.text() + str(numero)
        flotante = float(cadena)
        if flotante.is_integer():
            entero = int(flotante)
            cadena = str(entero)
        else:
            cadena = str(flotante)
            
        self.etiqueta.setText(cadena)
        print(cadena)
    
    def setNumero(self):
        cadena = self.etiqueta.text() + self.sender().text()
        '''flotante = float(cadena)
        if flotante.is_integer():
            entero = int(flotante)
            cadena = str(entero)
        else:
            cadena = str(flotante)'''
            
        self.etiqueta.setText(cadena)
        print(cadena)
    
    def setIgual(self):
        cadena=self.etiqueta.text()
        
        if cadena.find('+')!=-1 :
            indice_operador = cadena.find('+')
            # Extraer los operandos
            operando1 = float(cadena[:indice_operador])
            operando2 = float(cadena[indice_operador + 1:])
            self.etiqueta.setText(str(operando1+operando2))
            
        elif cadena.find('-')!=-1  and cadena.find('inv')==-1 and cadena.find('/')==-1:
            indice_operador = cadena.find('-')
            # Extraer los operandos
            operando1 = float(cadena[:indice_operador])
            operando2 = float(cadena[indice_operador + 1:])
            self.etiqueta.setText(str(operando1-operando2))
            
        elif cadena.find('*')!=-1:
            indice_operador = cadena.find('*')
            # Extraer los operandos
            operando1 = float(cadena[:indice_operador])
            operando2 = float(cadena[indice_operador + 1:])
            self.etiqueta.setText(str(operando1*operando2))
        
        elif cadena.find('/')!=-1 :
            indice_operador = cadena.find('/')
            # Extraer los operandos
            operando1 = float(cadena[:indice_operador])
            operando2 = float(cadena[indice_operador + 1:])
            if operando2==0:
                self.etiqueta.setText('Syntax Error')
            else:
                self.etiqueta.setText(str(operando1/operando2))
            
        elif cadena.find('%')!=-1:
            indice_operador = cadena.find('%')
            # Extraer los operandos
            operando1 = float(cadena[:indice_operador])
            operando2 = float(cadena[indice_operador + 1:])
            self.etiqueta.setText(str((operando1*operando2)/100))
            
        elif cadena.find('inv')!=-1 :
            indice_operador = cadena.find('(inv)')
            # Extraer los operandos
            operando1 = float(cadena[:indice_operador])
 
            if operando1>0:
                self.etiqueta.setText(str(operando1*(-1)))
            else:
                self.etiqueta.setText(str(operando1*(-1)))
            
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    