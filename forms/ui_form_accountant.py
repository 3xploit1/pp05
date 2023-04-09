# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_accountantZmmPWA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow_accountant(object):
    def setupUi(self, MainWindow_accountant):
        if not MainWindow_accountant.objectName():
            MainWindow_accountant.setObjectName(u"MainWindow_accountant")
        MainWindow_accountant.resize(576, 324)
        self.centralwidget = QWidget(MainWindow_accountant)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_role_accountant = QLabel(self.centralwidget)
        self.label_role_accountant.setObjectName(u"label_role_accountant")
        self.label_role_accountant.setGeometry(QRect(10, 100, 281, 31))
        font = QFont()
        font.setPointSize(16)
        self.label_role_accountant.setFont(font)
        self.label_surname_accountant = QLabel(self.centralwidget)
        self.label_surname_accountant.setObjectName(u"label_surname_accountant")
        self.label_surname_accountant.setGeometry(QRect(10, 50, 281, 31))
        self.label_surname_accountant.setFont(font)
        self.image_laborant_accountant = QLabel(self.centralwidget)
        self.image_laborant_accountant.setObjectName(u"image_laborant_accountant")
        self.image_laborant_accountant.setGeometry(QRect(366, 32, 181, 241))
        self.label_name_accountant = QLabel(self.centralwidget)
        self.label_name_accountant.setObjectName(u"label_name_accountant")
        self.label_name_accountant.setGeometry(QRect(10, 0, 281, 31))
        self.label_name_accountant.setFont(font)
        MainWindow_accountant.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_accountant)

        QMetaObject.connectSlotsByName(MainWindow_accountant)
    # setupUi

    def retranslateUi(self, MainWindow_accountant):
        MainWindow_accountant.setWindowTitle(QCoreApplication.translate("MainWindow_accountant", u"MainWindow", None))
        self.label_role_accountant.setText(QCoreApplication.translate("MainWindow_accountant", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0420\u043e\u043b\u044c</span></p></body></html>", None))
        self.label_surname_accountant.setText(QCoreApplication.translate("MainWindow_accountant", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0424\u0430\u043c\u0438\u043b\u0438\u044f</span></p></body></html>", None))
        self.image_laborant_accountant.setText(QCoreApplication.translate("MainWindow_accountant", u"<html><head/><body><p>img</p></body></html>", None))
        self.label_name_accountant.setText(QCoreApplication.translate("MainWindow_accountant", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0418\u043c\u044f</span></p></body></html>", None))
    # retranslateUi

