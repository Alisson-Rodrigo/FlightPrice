import typing
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QPushButton
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QColor
from PyQt5.QtPrintSupport import *
import sys
import FlightPrice


from tela_principal import Tela_Principal
from tela_inicia import Tela_Inicial

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(600, 400)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_principal = Tela_Principal()
        self.tela_principal.setupUi(self.stack1)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)


class Main(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        self.tela_inicial.pushButton_2.clicked.connect(self.fechar_programa)
        self.tela_inicial.pushButton.clicked.connect(self.buscar_viagens)
        
    def buscar_viagens (self):
        origem = self.tela_inicial.lineEdit_4.text()
        destino = self.tela_inicial.lineEdit_5.text()
        data_ida = self.tela_inicial.lineEdit_7.text()
        data_volta = self.tela_inicial.lineEdit_8.text()
        if origem == "" or destino == "" or data_ida == "" or data_volta == "":
            QMessageBox.about(self, "Erro", "Preencha todos os campos")
        else:
            pacote = FlightPrice.FlightPrice(origem, destino, data_ida, data_volta)
            QMessageBox.about(self, "Um momento", "Aguarde enquanto buscamos os voos")
            self.dados = pacote.buscar_voos()
            self.mostrar_tela_principal()
    
    def mostrar_tela_principal(self):
        self.QtStack.setCurrentIndex(1)
               

    def fechar_programa(self):
        sys.exit(app.exec_())
        

if __name__ == '__main__':
    app = QApplication(sys.argv)    
    show_main = Main()
    sys.exit(app.exec_())
        