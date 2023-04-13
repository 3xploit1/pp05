# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_challengeKmkSQn.ui'
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
        Main_challenge.resize(364, 318)
        icon = QIcon()
        icon.addFile(u"../../Resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Main_challenge.setWindowIcon(icon)
        Main_challenge.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_5 = QVBoxLayout(Main_challenge)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lab_captcha = QLabel(Main_challenge)
        self.lab_captcha.setObjectName(u"lab_captcha")

        self.verticalLayout.addWidget(self.lab_captcha)

        self.lineEdit_code_captcha = QLineEdit(Main_challenge)
        self.lineEdit_code_captcha.setObjectName(u"lineEdit_code_captcha")
        font = QFont()
        font.setPointSize(16)
        self.lineEdit_code_captcha.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit_code_captcha)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.centralwidget = QWidget(Main_challenge)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_request = QPushButton(self.centralwidget)
        self.btn_request.setObjectName(u"btn_request")
        self.btn_request.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(73,140,81);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_request)

        self.btn_reload_img = QPushButton(self.centralwidget)
        self.btn_reload_img.setObjectName(u"btn_reload_img")
        self.btn_reload_img.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(73,140,81);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_reload_img)

        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")

        self.verticalLayout_3.addWidget(self.label_logo)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addWidget(self.centralwidget)


        self.retranslateUi(Main_challenge)

        QMetaObject.connectSlotsByName(Main_challenge)
    # setupUi

    def retranslateUi(self, Main_challenge):
        Main_challenge.setWindowTitle(QCoreApplication.translate("Main_challenge", u"MainWindow", None))
        self.lab_captcha.setText(QCoreApplication.translate("Main_challenge", u"TextLabel", None))
        self.btn_request.setText(QCoreApplication.translate("Main_challenge", u"\u041e\u043a", None))
        self.btn_reload_img.setText(QCoreApplication.translate("Main_challenge", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_logo.setText(QCoreApplication.translate("Main_challenge", u"TextLabel", None))
    # retranslateUi

