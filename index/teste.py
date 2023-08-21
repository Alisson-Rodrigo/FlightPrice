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
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

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

        self.tela_principal.pushButton_3.clicked.connect(self.fechar_programa)
        
    def buscar_viagens (self):
        origem = self.tela_inicial.lineEdit_4.text()
        destino = self.tela_inicial.lineEdit_5.text()
        data_ida = self.tela_inicial.lineEdit_7.text()
        data_volta = self.tela_inicial.lineEdit_8.text()
        if origem == "" or destino == "" or data_ida == "" or data_volta == "":
            QMessageBox.about(self, "Erro", "Preencha todos os campos")
        else:
            pacote = FlightPrice.Buscador_voos(origem, destino, data_ida, data_volta)
            QMessageBox.about(self, "Um momento", "Aguarde enquanto buscamos os voos")
            self.dados = pacote.melhores_precos()
            self.mostrar_tela_principal()
    

    def mostrar_tela_principal(self):
        self.QtStack.setCurrentIndex(1)
        
        if self.dados != None:
            if 'voo1' in self.dados:
                self.tela_principal.lineEdit.setText(self.dados['voo1']['companhia'])
                self.tela_principal.lineEdit_2.setText(self.dados['voo1']['preço'])
                self.tela_principal.lineEdit_3.setText(self.dados['voo1']['horario_partida'])
                self.tela_principal.lineEdit_4.setText(self.dados['voo1']['horario_chegada'])
            else:
                self.tela_principal.lineEdit.setText("Não há voos")
                self.tela_principal.lineEdit_2.setText("Não há voos")
                self.tela_principal.lineEdit_3.setText("Não há voos")
                self.tela_principal.lineEdit_4.setText("Não há voos")

            if 'voo2' in self.dados:
                self.tela_principal.lineEdit_5.setText(self.dados['voo2']['companhia'])
                self.tela_principal.lineEdit_6.setText(self.dados['voo2']['preço'])
                self.tela_principal.lineEdit_7.setText(self.dados['voo2']['horario_partida'])
                self.tela_principal.lineEdit_8.setText(self.dados['voo2']['horario_chegada'])
            else:
                self.tela_principal.lineEdit_5.setText("Não há voos")
                self.tela_principal.lineEdit_6.setText("Não há voos")
                self.tela_principal.lineEdit_7.setText("Não há voos")
                self.tela_principal.lineEdit_8.setText("Não há voos")
        
            if 'voo3' in self.dados:
                self.tela_principal.lineEdit_9.setText(self.dados['voo3']['companhia'])
                self.tela_principal.lineEdit_10.setText(self.dados['voo3']['preço'])
                self.tela_principal.lineEdit_11.setText(self.dados['voo3']['horario_partida'])
                self.tela_principal.lineEdit_12.setText(self.dados['voo3']['horario_chegada'])
            else:
                self.tela_principal.lineEdit_9.setText("Não há voos")
                self.tela_principal.lineEdit_10.setText("Não há voos")
                self.tela_principal.lineEdit_11.setText("Não há voos")
                self.tela_principal.lineEdit_12.setText("Não há voos")

            if 'voo4' in self.dados:
                self.tela_principal.lineEdit_13.setText(self.dados['voo4']['companhia'])
                self.tela_principal.lineEdit_14.setText(self.dados['voo4']['preço'])
                self.tela_principal.lineEdit_15.setText(self.dados['voo4']['horario_partida'])
                self.tela_principal.lineEdit_16.setText(self.dados['voo4']['horario_chegada'])
            else:
                self.tela_principal.lineEdit_13.setText("Não há voos")
                self.tela_principal.lineEdit_14.setText("Não há voos")
                self.tela_principal.lineEdit_15.setText("Não há voos")
                self.tela_principal.lineEdit_16.setText("Não há voos")

            if 'voo5' in self.dados:
                self.tela_principal.lineEdit_17.setText(self.dados['voo5']['companhia'])
                self.tela_principal.lineEdit_18.setText(self.dados['voo5']['preço'])
                self.tela_principal.lineEdit_19.setText(self.dados['voo5']['horario_partida'])
                self.tela_principal.lineEdit_20.setText(self.dados['voo5']['horario_chegada'])
            else:
                self.tela_principal.lineEdit_17.setText("Não há voos")
                self.tela_principal.lineEdit_18.setText("Não há voos")
                self.tela_principal.lineEdit_19.setText("Não há voos")
                self.tela_principal.lineEdit_20.setText("Não há voos")
        else:
            QMessageBox.about(self, "Erro", "Não há voos disponíveis")
        
     
    def fechar_programa(self):
        sys.exit(app.exec_())
        

if __name__ == '__main__':
    app = QApplication(sys.argv)    
    show_main = Main()
    sys.exit(app.exec_())
        