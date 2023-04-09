# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_adminkMbdfT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow_admin(object):
    def setupUi(self, MainWindow_admin):
        if not MainWindow_admin.objectName():
            MainWindow_admin.setObjectName(u"MainWindow_admin")
        MainWindow_admin.resize(584, 306)
        self.centralwidget = QWidget(MainWindow_admin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_name_admin = QLabel(self.centralwidget)
        self.label_name_admin.setObjectName(u"label_name_admin")
        self.label_name_admin.setGeometry(QRect(10, 0, 281, 31))
        font = QFont()
        font.setPointSize(16)
        self.label_name_admin.setFont(font)
        self.label_surname_admin = QLabel(self.centralwidget)
        self.label_surname_admin.setObjectName(u"label_surname_admin")
        self.label_surname_admin.setGeometry(QRect(10, 50, 281, 31))
        self.label_surname_admin.setFont(font)
        self.image_laborant_admin = QLabel(self.centralwidget)
        self.image_laborant_admin.setObjectName(u"image_laborant_admin")
        self.image_laborant_admin.setGeometry(QRect(366, 22, 181, 251))
        self.label_role_admin = QLabel(self.centralwidget)
        self.label_role_admin.setObjectName(u"label_role_admin")
        self.label_role_admin.setGeometry(QRect(10, 100, 281, 31))
        self.label_role_admin.setFont(font)
        MainWindow_admin.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_admin)

        QMetaObject.connectSlotsByName(MainWindow_admin)
    # setupUi

    def retranslateUi(self, MainWindow_admin):
        MainWindow_admin.setWindowTitle(QCoreApplication.translate("MainWindow_admin", u"MainWindow", None))
        self.label_name_admin.setText(QCoreApplication.translate("MainWindow_admin", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0418\u043c\u044f</span></p></body></html>", None))
        self.label_surname_admin.setText(QCoreApplication.translate("MainWindow_admin", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0424\u0430\u043c\u0438\u043b\u0438\u044f</span></p></body></html>", None))
        self.image_laborant_admin.setText(QCoreApplication.translate("MainWindow_admin", u"<html><head/><body><p>img</p></body></html>", None))
        self.label_role_admin.setText(QCoreApplication.translate("MainWindow_admin", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0420\u043e\u043b\u044c</span></p></body></html>", None))
    # retranslateUi

