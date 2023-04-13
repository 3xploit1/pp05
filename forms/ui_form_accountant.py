# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_accountantbYLTJo.ui'
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
        MainWindow_accountant.resize(577, 324)
        icon = QIcon()
        icon.addFile(u"../../Resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow_accountant.setWindowIcon(icon)
        MainWindow_accountant.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow_accountant)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name_accountant = QLabel(self.centralwidget)
        self.label_name_accountant.setObjectName(u"label_name_accountant")
        font = QFont()
        font.setPointSize(16)
        self.label_name_accountant.setFont(font)

        self.verticalLayout.addWidget(self.label_name_accountant)

        self.label_role_accountant = QLabel(self.centralwidget)
        self.label_role_accountant.setObjectName(u"label_role_accountant")
        self.label_role_accountant.setFont(font)

        self.verticalLayout.addWidget(self.label_role_accountant)

        self.btn_req_report = QPushButton(self.centralwidget)
        self.btn_req_report.setObjectName(u"btn_req_report")
        self.btn_req_report.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(73,140,81);\n"
"}")

        self.verticalLayout.addWidget(self.btn_req_report)

        self.btn_req_graph = QPushButton(self.centralwidget)
        self.btn_req_graph.setObjectName(u"btn_req_graph")
        self.btn_req_graph.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(73,140,81);\n"
"}")

        self.verticalLayout.addWidget(self.btn_req_graph)

        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(0, 150))

        self.verticalLayout.addWidget(self.label_logo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.image_laborant_accountant = QLabel(self.centralwidget)
        self.image_laborant_accountant.setObjectName(u"image_laborant_accountant")

        self.horizontalLayout.addWidget(self.image_laborant_accountant)

        MainWindow_accountant.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_accountant)

        QMetaObject.connectSlotsByName(MainWindow_accountant)
    # setupUi

    def retranslateUi(self, MainWindow_accountant):
        MainWindow_accountant.setWindowTitle(QCoreApplication.translate("MainWindow_accountant", u"MainWindow", None))
        self.label_name_accountant.setText(QCoreApplication.translate("MainWindow_accountant", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0418\u043c\u044f</span></p></body></html>", None))
        self.label_role_accountant.setText(QCoreApplication.translate("MainWindow_accountant", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0420\u043e\u043b\u044c</span></p></body></html>", None))
        self.btn_req_report.setText(QCoreApplication.translate("MainWindow_accountant", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.btn_req_graph.setText(QCoreApplication.translate("MainWindow_accountant", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow_accountant", u"TextLabel", None))
        self.image_laborant_accountant.setText(QCoreApplication.translate("MainWindow_accountant", u"<html><head/><body><p>img</p></body></html>", None))
    # retranslateUi

