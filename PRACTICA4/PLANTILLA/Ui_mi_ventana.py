# Form implementation generated from reading ui file 'd:\Documentos\SUPERIOR\4toSEMESTRE\Programacion avanzada\Practicas_\PRACTICA4\mi_ventana.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Adal(object):
    def setupUi(self, Adal):
        Adal.setObjectName("Adal")
        Adal.resize(450, 450)
        Adal.setMinimumSize(QtCore.QSize(50, 50))
        Adal.setMaximumSize(QtCore.QSize(450, 450))
        self.centralwidget = QtWidgets.QWidget(parent=Adal)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 10, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 50, 104, 71))
        self.textEdit.setObjectName("textEdit")
        Adal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Adal)
        self.statusbar.setObjectName("statusbar")
        Adal.setStatusBar(self.statusbar)

        self.retranslateUi(Adal)
        QtCore.QMetaObject.connectSlotsByName(Adal)

    def retranslateUi(self, Adal):
        _translate = QtCore.QCoreApplication.translate
        Adal.setWindowTitle(_translate("Adal", "MainWindow"))
        self.pushButton.setText(_translate("Adal", "hola"))
        self.textEdit.setHtml(_translate("Adal", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hola</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
