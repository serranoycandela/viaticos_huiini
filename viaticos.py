#-*- encoding: utf-8 -*-
import xml.etree.ElementTree as etree
import os
import xlsxwriter
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QTableWidget,QTableWidgetItem,QPushButton
from PySide2.QtCore import QFile, QRect
from PySide2.QtGui import QIcon
from gui import Ui_MainWindow
import json
from os.path import dirname, realpath, join, abspath

# pyside2-uic gui.ui -o gui.py
#C:\Users\arabela\Anaconda3\Scripts\pyinstaller --noconsole viaticos.spec
#excludes=['scipy','numpy']
#C:\Users\arabela\Anaconda3\Scripts\pyinstaller viaticos.spec
class EditPersonasDialog(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.tabla = QTableWidget(self)
        self.tabla.setColumnCount(1)

        self.tabla.setColumnWidth(0,150)
        self.tabla.setHorizontalHeaderItem (0, QTableWidgetItem("Personas"))
        self.guardar = QPushButton("Gardar",self)
        self.guardar.clicked.connect(self.guardarPersonas)
        try:
            self.dirPath = dirname(abspath(__file__))
        except NameError:  # We are the main py2exe script, not a module
            self.dirPath = dirname(abspath(sys.argv[0]))

        with open(join(self.dirPath,'personas.json')) as p:
            personas = json.load(p)


        self.tabla.setRowCount(len(personas)+5)
        row = -1
        for persona in personas:
            row += 1
            self.tabla.setItem(row, 0, QTableWidgetItem(persona))
        #self.lista_personas.setItem(1, 0, newItem)
    def guardarPersonas(self):
        personas = []
        for row in range(self.tabla.rowCount()):
            print (row)
            if self.tabla.item(row,0):
                print ("agregando: ", self.tabla.item(row,0).text())
                personas.append(self.tabla.item(row,0).text())

        with open(join(self.dirPath,'personas.json'), 'w') as p:
            json.dump(personas, p)
        self.close()


class EditProyectosDialog(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.tabla = QTableWidget(self)
        self.tabla.setColumnCount(1)

        self.tabla.setColumnWidth(0,150)
        self.tabla.setHorizontalHeaderItem (0, QTableWidgetItem("Proyectos"))

        try:
            dirPath = dirname(abspath(__file__))
        except NameError:  # We are the main py2exe script, not a module
            dirPath = dirname(abspath(sys.argv[0]))

        with open(join(dirPath,'proyectos.json')) as p:
            proyectos = json.load(p)


        self.tabla.setRowCount(len(proyectos)+5)
        row = -1
        for proyecto in proyectos[1:]:
            row += 1
            self.tabla.setItem(row, 0, QTableWidgetItem(proyecto))
        #self.lista_personas.setItem(1, 0, newItem)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.input_carpeta.clicked.connect(self.cualCarpeta)
        try:
            self.dirPath = dirname(abspath(__file__))
        except NameError:  # We are the main py2exe script, not a module
            self.dirPath = dirname(abspath(sys.argv[0]))

        #self.proyectos = ["","Papiit", "Consolidacion", "Fomix", "Binacional", "Otros"]
        self.leerPersonas()
        self.leerProyectos()
        self.ui.tableWidget.setColumnCount(1)

        self.ui.tableWidget.setColumnWidth(0,100)

        #self.personas = ["Daniela", "Edith", "Rodrigo", "Fidel", "Ileana", "Luis", "Nadia", "Paola", "Victor", "Yosune", "Rocio", "Bertha"]
        self.ui.proyecto_box.addItems(self.proyectos)
        self.ui.proyecto_box.currentIndexChanged.connect(self.seleccionaProyecto)
        self.ui.actionAgregar_o_quitar_personas.triggered.connect(self.editPersonas)
        self.ui.actionAgregar_o_quitar_proyectos.triggered.connect(self.editProyectos)
        self.ui.cancelarButton.clicked.connect(self.cancelaEditar)
        self.ui.guardarButton.clicked.connect(self.guarda)
        self.ui.editFrame.hide()

    def cancelaEditar(self):
        self.ui.editFrame.hide()
    def leerPersonas(self):
        with open(join(self.dirPath,'personas.json')) as p:
            self.personas = json.load(p)
    def leerProyectos(self):
        with open(join(self.dirPath,'proyectos.json')) as p:
            self.proyectos = json.load(p)
    def editPersonas(self):
        print("editaria personas")

        self.ui.editFrame.show()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setHorizontalHeaderItem (0, QTableWidgetItem("Personas"))
        self.ui.tableWidget.setRowCount(len(self.personas)+5)
        row = -1
        for persona in self.personas:
            row += 1
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(persona))
    def editProyectos(self):
        self.ui.editFrame.show()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setHorizontalHeaderItem (0, QTableWidgetItem("Proyectos"))
        self.ui.tableWidget.setRowCount(len(self.proyectos)+5)
        row = -1
        for proyecto in self.proyectos[1:]:
            row += 1
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(proyecto))

    def guarda(self):
        if self.ui.tableWidget.horizontalHeaderItem(0).text() == "Personas":
            self.guardaPersonas()
        elif self.ui.tableWidget.horizontalHeaderItem(0).text() == "Proyectos":
            self.guardaProyectos()
    def guardaPersonas(self):
        print("aqui guardaria personas")

        self.personas = []
        for row in range(self.ui.tableWidget.rowCount()):
            print (row)
            if self.ui.tableWidget.item(row,0):
                if len(self.ui.tableWidget.item(row,0).text())>0:
                    print ("agregando: ", self.ui.tableWidget.item(row,0).text())
                    self.personas.append(self.ui.tableWidget.item(row,0).text())

        with open(join(self.dirPath,'personas.json'), 'w') as p:
            json.dump(self.personas, p)
        self.ui.editFrame.hide()
    def guardaProyectos(self):
        print("aqui guardaria proyectos")
        self.proyectos = [""]
        for row in range(self.ui.tableWidget.rowCount()):
            print (row)
            if self.ui.tableWidget.item(row,0):
                if len(self.ui.tableWidget.item(row,0).text())>0:
                    print ("agregando: ", self.ui.tableWidget.item(row,0).text())
                    self.proyectos.append(self.ui.tableWidget.item(row,0).text())

        with open(join(self.dirPath,'proyectos.json'), 'w') as p:
            json.dump(self.proyectos, p)
        self.ui.editFrame.hide()
        self.ui.proyecto_box.clear()
        self.ui.proyecto_box.addItems(self.proyectos)

    def seleccionaProyecto(self):
        self.ui.input_carpeta.setEnabled(True)
    def cualCarpeta(self):

        esteFileChooser = QFileDialog()
        esteFileChooser.setFileMode(QFileDialog.Directory)
        if esteFileChooser.exec_():
            self.ui.textBrowser.clear()
            self.esteFolder = esteFileChooser.selectedFiles()[0] + "/"

            self.procesaCarpeta(self.esteFolder)


    def procesaCarpeta(self,path):

        xlsx_path = os.path.join(path,"resumen.xlsx")
        workbook = xlsxwriter.Workbook(xlsx_path)
        worksheet = workbook.add_worksheet("viaticos")

        worksheet.write(0, 0,     "Usuario")
        worksheet.write(0, 1,     "Proyecto")
        worksheet.write(0, 2,     "Fecha")
        worksheet.write(0, 3,     "Folio facturas")
        worksheet.write(0, 4,     "Tipo")
        worksheet.write(0, 5,     "Monto")
        worksheet.write(0, 6,     "Estatus")
        worksheet.write(0, 7,     "Comentario")
        worksheet.write(0, 8,     "Clave PS")
        worksheet.write(0, 9,     "Descripcion")

        row = 0
        suma = 0
        arch_total=0
        dicc_users = {}
        self.ui.textBrowser.append("Carpeta: "+ path)
        for carpeta in os.listdir(path):
            if os.path.isdir(os.path.join(path,carpeta)):

                carpeta_usuario = os.path.join(path,carpeta)
                usuario = carpeta
                self.ui.textBrowser.append("Procesando: "+ usuario)
                suma_user=0
                dicc_users[usuario]=0
                for archivo in os.listdir(carpeta_usuario):
                    if archivo.endswith(".xml"):
                        arch_total+=1
                        nombre = archivo.split(".")[0]
                        if len(nombre) > 5:
                            nombre = nombre[-5:]
                        row += 1
                        xml_path = os.path.join(carpeta_usuario,archivo)
                        tree = etree.parse(xml_path)

                        root = tree.getroot()
                        total = float(root.get("Total"))
                        dicc_users[usuario] += total
                        ComplementoTag = root.find("{http://www.sat.gob.mx/cfd/3}Complemento")
                        TimbreFiscalDigitalTag = ComplementoTag.find("{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital")
                        fechaTimbrado = TimbreFiscalDigitalTag.get("FechaTimbrado").split("T")[0]

                        conceptosTag = root.find("{http://www.sat.gob.mx/cfd/3}Conceptos")

                        listaconceptosTag = conceptosTag.findall ("{http://www.sat.gob.mx/cfd/3}Concepto")
                        primerConceptoTag = listaconceptosTag[0]
                        descripcion = primerConceptoTag.get("Descripcion")[0:36]
                        clave_ps = primerConceptoTag.get("ClaveProdServ")
                        print (xml_path, total, fechaTimbrado, descripcion, nombre)
                        #worksheet.data_validation('A'+str(row+1), {'validate': 'list', 'source': self.personas})
                        worksheet.write(row, 0,     usuario)
                        worksheet.data_validation('B'+str(row+1), {'validate': 'list', 'source': self.proyectos})
                        worksheet.write(row, 1,     self.ui.proyecto_box.currentText())
                        worksheet.write(row, 2,     fechaTimbrado)
                        worksheet.write(row, 3,     nombre)

                        worksheet.data_validation('E'+str(row+1), {'validate': 'list', 'source': ['Alimentos', 'Hospedaje', 'Transportacion', 'Otros']})
                        worksheet.write(row, 5,     total)
                        suma+=total
                        worksheet.data_validation('G'+str(row+1), {'validate': 'list', 'source': ['Pendiente', 'Reembolzado']})
                        #worksheet.data_validation('H'+str(row+1), {'validate': 'list', 'source': ['Si', 'No']})
                        worksheet.write(row, 8,     clave_ps)

                        worksheet.write(row, 9,     descripcion)

                        # Write a total using a formula.
                        # worksheet.write(row, 0, 'Total')
                        # worksheet.write(row, 1, '=SUM(B1:B4)')


        sumRow = row+1
        worksheet.write(sumRow, 4,     "Suma")
        worksheet.write(sumRow, 5,     '=SUM(F2:F'+str(sumRow)+')')
        #sumas_row = sumRow + 2
        #sumas_row_inicial = str(sumRow + 2)
        sumas_row = 4
        sumas_row_inicial = "5"
        sumas_column_inicial = 14
        suma_total = 0
        format = workbook.add_format()

        format.set_pattern(1)
        format.set_bg_color('#d3d3d3')
        worksheet.write(sumas_row-1, sumas_column_inicial+1,'Total', format)
        worksheet.write(sumas_row-1, sumas_column_inicial+2,'Alimentos', format)
        worksheet.write(sumas_row-1, sumas_column_inicial+3,'Hospedaje', format)
        worksheet.write(sumas_row-1, sumas_column_inicial+4,'Transportacion', format)
        worksheet.write(sumas_row-1, sumas_column_inicial+5,'Otros', format)
        for key, value in dicc_users.items():
            self.ui.textBrowser.append(key+": "+ str(value))
            worksheet.write(sumas_row, sumas_column_inicial,     key, format)
            #worksheet.write(sumas_row, 5,     value)
            worksheet.write(sumas_row, sumas_column_inicial+1,     '=SUMIF(A2:A'+str(sumRow)+',"'+key+'",F2:F'+str(sumRow)+')')
            worksheet.write(sumas_row, sumas_column_inicial+2,     '=SUMIFS(F2:F'+str(sumRow)+',A2:A'+str(sumRow)+',"'+key+'",E2:E'+str(sumRow)+',"Alimentos")')
            worksheet.write(sumas_row, sumas_column_inicial+3,     '=SUMIFS(F2:F'+str(sumRow)+',A2:A'+str(sumRow)+',"'+key+'",E2:E'+str(sumRow)+',"Hospedaje")')
            worksheet.write(sumas_row, sumas_column_inicial+4,     '=SUMIFS(F2:F'+str(sumRow)+',A2:A'+str(sumRow)+',"'+key+'",E2:E'+str(sumRow)+',"Transportacion")')
            worksheet.write(sumas_row, sumas_column_inicial+5,     '=SUMIFS(F2:F'+str(sumRow)+',A2:A'+str(sumRow)+',"'+key+'",E2:E'+str(sumRow)+',"Otros")')
            suma_total += value
            sumas_row += 1

        totales_row_str = str(sumas_row)

        worksheet.write(sumas_row, sumas_column_inicial+1,     '=SUM(P'+sumas_row_inicial+':P'+totales_row_str+')')
        worksheet.write(sumas_row, sumas_column_inicial+2,     '=SUM(Q'+sumas_row_inicial+':Q'+totales_row_str+')')
        worksheet.write(sumas_row, sumas_column_inicial+3,     '=SUM(R'+sumas_row_inicial+':R'+totales_row_str+')')
        worksheet.write(sumas_row, sumas_column_inicial+4,     '=SUM(S'+sumas_row_inicial+':S'+totales_row_str+')')
        worksheet.write(sumas_row, sumas_column_inicial+5,     '=SUM(T'+sumas_row_inicial+':T'+totales_row_str+')')

        self.ui.textBrowser.append("Total: "+str(suma_total))
        workbook.close()
        self.ui.textBrowser.append("Resumen: "+xlsx_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.setWindowIcon(QIcon(join(window.dirPath,'logo.ico')))
    window.setWindowIcon(QIcon(join(window.dirPath,'logo.ico')))
    sys.exit(app.exec_())
