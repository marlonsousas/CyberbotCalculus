__author__ = "Marlon Sousa"
__licence__ = "Cyberbot©"
__date__ = "2021"

from PyQt5 import QtCore, QtGui, QtWidgets
from libs.graph import *
from libs.calculus import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 500)
        MainWindow.setMinimumSize(QtCore.QSize(645, 500))
        MainWindow.setMaximumSize(QtCore.QSize(645, 500))
        MainWindow.setStyleSheet("background: #212531;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 301, 101))
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setLineWidth(-2)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 180, 191, 71))
        self.pushButton.clicked.connect(lambda: derivadaFunc())
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: white;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 180, 191, 71))
        self.pushButton_2.clicked.connect(lambda: integrateFunc())
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 120, 381, 41))
        self.textEdit.setStyleSheet("color: white;\n"
"font-size: 25px;")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 340, 141, 141))
        self.label_2.setStyleSheet("background-image: url(:/newLogo/img/image.png);")
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setPixmap(QtGui.QPixmap(":/newLogo/img/image.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 460, 101, 21))
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 290, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def derivadaFunc():
            mytext = self.textEdit.toPlainText()
            if not mytext:
                pass
            else:
                try:
                    print(derivate(mytext))
                    self.label_4.setText(str(derivate(mytext)))
                    graph2d(mytext)
                except:
                    print("Function Error")
                
        
        def integrateFunc():
            mytext = self.textEdit.toPlainText()
            if not mytext:
                pass
            else:
                try:
                    print(integral(mytext))
                    self.label_4.setText(str(integral(mytext)))
                    graph2d(mytext)
                except:
                    print("Function Error")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cyberbot Calculus"))
        self.label.setText(_translate("MainWindow", "Cyberbot Calculus ∞"))
        self.pushButton.setText(_translate("MainWindow", "Derivate"))
        self.pushButton_2.setText(_translate("MainWindow", "Integral"))
        self.label_3.setText(_translate("MainWindow", "Marlon Sousa"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
