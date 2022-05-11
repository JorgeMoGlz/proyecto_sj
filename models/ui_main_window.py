# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowbWeQio.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 600)
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_date = QLabel(self.centralwidget)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setGeometry(QRect(170, 10, 491, 41))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        self.label_date.setFont(font)
        self.label_gold_price = QLabel(self.centralwidget)
        self.label_gold_price.setObjectName(u"label_gold_price")
        self.label_gold_price.setGeometry(QRect(20, 80, 151, 16))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_gold_price.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(650, 80, 161, 16))
        self.label.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 832, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SJ Project", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"\u00daltima actualizaci\u00f3n de precios: 13 de diciembre del 2022", None))
        self.label_gold_price.setText(QCoreApplication.translate("MainWindow", u"Precio oro: 9999.99", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Precio  plata: 999.99", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

