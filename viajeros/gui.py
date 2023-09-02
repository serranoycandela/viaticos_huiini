# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1076, 485)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionAgregar_o_quitar_personas = QAction(MainWindow)
        self.actionAgregar_o_quitar_personas.setObjectName(u"actionAgregar_o_quitar_personas")
        self.actionAgregar_o_quitar_proyectos = QAction(MainWindow)
        self.actionAgregar_o_quitar_proyectos.setObjectName(u"actionAgregar_o_quitar_proyectos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(25)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(160, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.splitter = QSplitter(self.frame_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 10, 341, 431))
        self.splitter.setOrientation(Qt.Vertical)
        self.carpeta_personal = QPushButton(self.splitter)
        self.carpeta_personal.setObjectName(u"carpeta_personal")
        self.carpeta_personal.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.carpeta_personal.sizePolicy().hasHeightForWidth())
        self.carpeta_personal.setSizePolicy(sizePolicy3)
        self.carpeta_personal.setMinimumSize(QSize(0, 30))
        self.carpeta_personal.setMaximumSize(QSize(16777215, 30))
        self.splitter.addWidget(self.carpeta_personal)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(4)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.splitter.addWidget(self.label_2)
        self.textBrowser = QTextBrowser(self.splitter)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(62)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy5)
        self.splitter.addWidget(self.textBrowser)
        self.excel_button = QPushButton(self.splitter)
        self.excel_button.setObjectName(u"excel_button")
        self.excel_button.setEnabled(False)
        self.splitter.addWidget(self.excel_button)

        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Viaticos Huiini", None))
        self.actionAgregar_o_quitar_personas.setText(QCoreApplication.translate("MainWindow", u"Agregar o quitar personas", None))
        self.actionAgregar_o_quitar_proyectos.setText(QCoreApplication.translate("MainWindow", u"Agregar o quitar proyectos", None))
        self.carpeta_personal.setText(QCoreApplication.translate("MainWindow", u"Prellenar formato de gastos de viaje", None))
        self.label_2.setText("")
        self.excel_button.setText(QCoreApplication.translate("MainWindow", u"Abrir excel", None))
    # retranslateUi

