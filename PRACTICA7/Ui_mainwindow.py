# Form implementation generated from reading ui file 'd:\Documentos\SUPERIOR\4toSEMESTRE\Programacion avanzada\Practicas_\PRACTICA7\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 341)
        MainWindow.setMinimumSize(QtCore.QSize(400, 341))
        MainWindow.setMaximumSize(QtCore.QSize(401, 342))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0 ,y2:1,stop:0 rgba(255, 255, 255, 255), stop:0.5 rgba(214,214,255,255), stop:1 rgba(255,255,255,255));")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 140, 101, 16))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 160, 171, 21))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 190, 101, 16))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: transparent;")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 220, 171, 21))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 260, 82, 20))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: transparent;")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 260, 61, 20))
        self.comboBox.setStyleSheet("background-color: transparent;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 30, 141, 91))
        self.label_4.setStyleSheet("background-color: transparent;\n"
"border: 2px solid black;\n"
"border-image: url(:/cct/logo3.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 20, 141, 101))
        self.label_5.setStyleSheet("border: 1px solid black;\n"
"background-color: transparent;\n"
"border-radius: 10px;\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Correo electronico: "))
        self.label_2.setText(_translate("MainWindow", "Contraseña:"))
        self.label_3.setText(_translate("MainWindow", "Status: "))
        self.comboBox.setItemText(0, _translate("MainWindow", "Online"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Offline"))
