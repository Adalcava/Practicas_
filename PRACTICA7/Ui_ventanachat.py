# Form implementation generated from reading ui file 'd:\Documentos\SUPERIOR\4toSEMESTRE\Programacion avanzada\Practicas_\PRACTICA7\ventanachat.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(884, 521)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0 ,y2:1,stop:0 rgba(255, 255, 255, 255), stop:0.5 rgba(214,214,255,255), stop:1 rgba(255,255,255,255));")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.lista_contactos = QtWidgets.QListWidget(parent=self.frame_6)
        self.lista_contactos.setGeometry(QtCore.QRect(0, 0, 220, 442))
        self.lista_contactos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lista_contactos.setObjectName("lista_contactos")
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.destinatario = QtWidgets.QLabel(parent=self.frame_4)
        self.destinatario.setGeometry(QtCore.QRect(10, 20, 400, 30))
        self.destinatario.setStyleSheet("background-color: rgb(236, 243, 253);\n"
"border-radius: 10px;")
        self.destinatario.setObjectName("destinatario")
        self.mostrar_mensajes = QtWidgets.QLabel(parent=self.frame_4)
        self.mostrar_mensajes.setGeometry(QtCore.QRect(10, 50, 400, 200))
        self.mostrar_mensajes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mostrar_mensajes.setText("")
        self.mostrar_mensajes.setObjectName("mostrar_mensajes")
        self.escribir_mensaje = QtWidgets.QLineEdit(parent=self.frame_4)
        self.escribir_mensaje.setGeometry(QtCore.QRect(10, 300, 400, 70))
        self.escribir_mensaje.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.escribir_mensaje.setObjectName("escribir_mensaje")
        self.enviar = QtWidgets.QPushButton(parent=self.frame_4)
        self.enviar.setGeometry(QtCore.QRect(330, 400, 75, 24))
        self.enviar.setObjectName("enviar")
        self.zumbido = QtWidgets.QPushButton(parent=self.frame_4)
        self.zumbido.setGeometry(QtCore.QRect(380, 270, 30, 30))
        self.zumbido.setStyleSheet("background-color: rgb(236, 243, 253);")
        self.zumbido.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Documentos\\SUPERIOR\\4toSEMESTRE\\Programacion avanzada\\Practicas_\\PRACTICA7\\zumbido.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.zumbido.setIcon(icon)
        self.zumbido.setIconSize(QtCore.QSize(30, 30))
        self.zumbido.setObjectName("zumbido")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(10, 270, 400, 30))
        self.label_7.setStyleSheet("background-color: rgb(236, 243, 253);\n"
"border-radius: 10px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_10.setGeometry(QtCore.QRect(10, 370, 400, 20))
        self.label_10.setStyleSheet("background-color: rgb(236, 243, 253);\n"
"border-radius: 10px;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_7.raise_()
        self.destinatario.raise_()
        self.mostrar_mensajes.raise_()
        self.escribir_mensaje.raise_()
        self.enviar.raise_()
        self.zumbido.raise_()
        self.label_10.raise_()
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.fotoperfil1 = QtWidgets.QLabel(parent=self.frame_5)
        self.fotoperfil1.setGeometry(QtCore.QRect(20, 50, 180, 120))
        self.fotoperfil1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fotoperfil1.setText("")
        self.fotoperfil1.setObjectName("fotoperfil1")
        self.fotoperfil2 = QtWidgets.QLabel(parent=self.frame_5)
        self.fotoperfil2.setGeometry(QtCore.QRect(20, 270, 180, 120))
        self.fotoperfil2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fotoperfil2.setText("")
        self.fotoperfil2.setObjectName("fotoperfil2")
        self.nombre1 = QtWidgets.QLabel(parent=self.frame_5)
        self.nombre1.setGeometry(QtCore.QRect(20, 20, 180, 30))
        self.nombre1.setStyleSheet("background-color: rgb(236, 243, 253);\n"
"")
        self.nombre1.setText("")
        self.nombre1.setObjectName("nombre1")
        self.nombre2 = QtWidgets.QLabel(parent=self.frame_5)
        self.nombre2.setGeometry(QtCore.QRect(20, 240, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nombre2.setFont(font)
        self.nombre2.setStyleSheet("background-color: rgb(236, 243, 253);")
        self.nombre2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nombre2.setObjectName("nombre2")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_8.setGeometry(QtCore.QRect(15, 16, 190, 181))
        self.label_8.setStyleSheet("background-color: rgb(236, 243, 253);\n"
"border-radius: 10px;\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_9.setGeometry(QtCore.QRect(15, 230, 190, 181))
        self.label_9.setStyleSheet("background-color: rgb(236, 243, 253);\n"
"border-radius: 10px;\n"
"")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_9.raise_()
        self.label_8.raise_()
        self.fotoperfil1.raise_()
        self.fotoperfil2.raise_()
        self.nombre1.raise_()
        self.nombre2.raise_()
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.destinatario.setText(_translate("Dialog", "Para:"))
        self.enviar.setText(_translate("Dialog", "Enviar"))
        self.nombre2.setText(_translate("Dialog", "Tu"))