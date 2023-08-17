# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicia.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Inicial(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1197, 671)
        MainWindow.setStyleSheet("background-color: #130F1A;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 60, 181, 25))
        self.lineEdit_4.setStyleSheet("border: 1px solid rgb(119, 118, 123);\n"
"border-radius: 5px;\n"
"color: rgb(119, 118, 123);")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(470, 60, 181, 25))
        self.lineEdit_5.setStyleSheet("border: 1px solid rgb(119, 118, 123);\n"
"border-radius: 5px;\n"
"color: rgb(119, 118, 123);")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(680, 60, 111, 25))
        self.lineEdit_7.setStyleSheet("border: 1px solid rgb(119, 118, 123);\n"
"border-radius: 5px;\n"
"color: rgb(119, 118, 123);")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(810, 60, 111, 25))
        self.lineEdit_8.setStyleSheet("border: 1px solid rgb(119, 118, 123);\n"
"border-radius: 5px;\n"
"color: rgb(119, 118, 123);")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 60, 31, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-image: url(lupa.png);\n"
"background-repeat: no-repeat;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(120, 150, 991, 491))
        self.frame.setStyleSheet("background-image: url(mapa_mundiINTEIRO.png);\n"
"background-repeat:no-repeat;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 620, 71, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(198, 70, 0);\n"
"color: black;\n"
"border-radius: 10px;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"color: black;}")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Origem"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Destino"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Ida"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "Volta"))
        self.pushButton_2.setText(_translate("MainWindow", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Inicial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
