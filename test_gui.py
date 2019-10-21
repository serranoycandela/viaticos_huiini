#-*- encoding: utf-8 -*-
# from PySide2.QtCore import *
#
# from PySide2.QtCore import Qt
# from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys


import gui

class Ui_MainWindow(QMainWindow, gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.input_carpeta.clicked.connect(self.cualCarpeta)

    def cualCarpeta(self):
        print("kkkkkkkkkkkk")
        self.facturas_path.setText("kkkkkkkkkkkkkk")
        # esteFileChooser = QtWidgets.QFileDialog()
        # esteFileChooser.setFileMode(QtWidgets.QFileDialog.Directory)
        # if esteFileChooser.exec_():
        #
        #     self.esteFolder = esteFileChooser.selectedFiles()[0] + "/"

app = QApplication(sys.argv)
ex = Ui_MainWindow()
w = QMainWindow()
ex.setupUi(w)
w.show()
sys.exit(app.exec_())
