import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import QFile
from gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.input_carpeta.clicked.connect(self.cualCarpeta)

    def cualCarpeta(self):
        print("kkkkkkkkkkkk")
        self.ui.facturas_path.setText(u"kkkkkkkkkkkkkk")
        esteFileChooser = QFileDialog()
        esteFileChooser.setFileMode(QFileDialog.Directory)
        if esteFileChooser.exec_():

            self.esteFolder = esteFileChooser.selectedFiles()[0] + "/"

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
