# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_challengeepSKWO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Main_challenge(object):
    def setupUi(self, Main_challenge):
        if not Main_challenge.objectName():
            Main_challenge.setObjectName(u"Main_challenge")
        Main_challenge.resize(364, 234)
        self.centralwidget = QWidget(Main_challenge)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, 0, 371, 231))
        self.lab_captcha = QLabel(self.centralwidget)
        self.lab_captcha.setObjectName(u"lab_captcha")
        self.lab_captcha.setGeometry(QRect(16, 22, 331, 101))
        self.btn_request = QPushButton(self.centralwidget)
        self.btn_request.setObjectName(u"btn_request")
        self.btn_request.setGeometry(QRect(220, 180, 71, 41))
        self.lineEdit_code_captcha = QLineEdit(self.centralwidget)
        self.lineEdit_code_captcha.setObjectName(u"lineEdit_code_captcha")
        self.lineEdit_code_captcha.setGeometry(QRect(40, 130, 251, 31))
        font = QFont()
        font.setPointSize(16)
        self.lineEdit_code_captcha.setFont(font)
        self.btn_reload_img = QPushButton(self.centralwidget)
        self.btn_reload_img.setObjectName(u"btn_reload_img")
        self.btn_reload_img.setGeometry(QRect(40, 180, 71, 41))
        self.statusbar = QStatusBar(Main_challenge)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 18))

        self.retranslateUi(Main_challenge)

        QMetaObject.connectSlotsByName(Main_challenge)
    # setupUi

    def retranslateUi(self, Main_challenge):
        Main_challenge.setWindowTitle(QCoreApplication.translate("Main_challenge", u"MainWindow", None))
        self.lab_captcha.setText(QCoreApplication.translate("Main_challenge", u"TextLabel", None))
        self.btn_request.setText(QCoreApplication.translate("Main_challenge", u"\u041e\u043a", None))
        self.btn_reload_img.setText(QCoreApplication.translate("Main_challenge", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

