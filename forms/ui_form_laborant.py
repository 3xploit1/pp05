# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_laborantVPJsLh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow_laborant(object):
    def setupUi(self, MainWindow_laborant):
        if not MainWindow_laborant.objectName():
            MainWindow_laborant.setObjectName(u"MainWindow_laborant")
        MainWindow_laborant.resize(573, 306)
        self.centralwidget = QWidget(MainWindow_laborant)
        self.centralwidget.setObjectName(u"centralwidget")
        self.image_laborant = QLabel(self.centralwidget)
        self.image_laborant.setObjectName(u"image_laborant")
        self.image_laborant.setGeometry(QRect(356, 32, 181, 241))
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(10, 0, 281, 31))
        font = QFont()
        font.setPointSize(16)
        self.label_name.setFont(font)
        self.label_surname = QLabel(self.centralwidget)
        self.label_surname.setObjectName(u"label_surname")
        self.label_surname.setGeometry(QRect(10, 50, 281, 31))
        self.label_surname.setFont(font)
        self.label_role = QLabel(self.centralwidget)
        self.label_role.setObjectName(u"label_role")
        self.label_role.setGeometry(QRect(10, 100, 281, 31))
        self.label_role.setFont(font)
        self.label_timer = QLabel(self.centralwidget)
        self.label_timer.setObjectName(u"label_timer")
        self.label_timer.setGeometry(QRect(6, 263, 101, 31))
        self.btn_req_order = QPushButton(self.centralwidget)
        self.btn_req_order.setObjectName(u"btn_req_order")
        self.btn_req_order.setGeometry(QRect(14, 172, 111, 41))
        MainWindow_laborant.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_laborant)

        QMetaObject.connectSlotsByName(MainWindow_laborant)
    # setupUi

    def retranslateUi(self, MainWindow_laborant):
        MainWindow_laborant.setWindowTitle(QCoreApplication.translate("MainWindow_laborant", u"MainWindow", None))
        self.image_laborant.setText(QCoreApplication.translate("MainWindow_laborant", u"<html><head/><body><p>img</p></body></html>", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow_laborant", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0418\u043c\u044f</span></p></body></html>", None))
        self.label_surname.setText(QCoreApplication.translate("MainWindow_laborant", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0424\u0430\u043c\u0438\u043b\u0438\u044f</span></p></body></html>", None))
        self.label_role.setText(QCoreApplication.translate("MainWindow_laborant", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0420\u043e\u043b\u044c</span></p></body></html>", None))
        self.label_timer.setText(QCoreApplication.translate("MainWindow_laborant", u"TextLabel", None))
        self.btn_req_order.setText(QCoreApplication.translate("MainWindow_laborant", u"C\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c\n"
"\u0437\u0430\u043a\u0430\u0437", None))
    # retranslateUi

