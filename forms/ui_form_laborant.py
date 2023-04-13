# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_laborantpJGxUX.ui'
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
        icon = QIcon()
        icon.addFile(u"../../Resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow_laborant.setWindowIcon(icon)
        MainWindow_laborant.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow_laborant)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        font = QFont()
        font.setPointSize(16)
        self.label_name.setFont(font)

        self.verticalLayout.addWidget(self.label_name)

        self.label_role = QLabel(self.centralwidget)
        self.label_role.setObjectName(u"label_role")
        self.label_role.setFont(font)

        self.verticalLayout.addWidget(self.label_role)

        self.btn_req_order = QPushButton(self.centralwidget)
        self.btn_req_order.setObjectName(u"btn_req_order")
        self.btn_req_order.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(73,140,81);\n"
"}")

        self.verticalLayout.addWidget(self.btn_req_order)

        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")

        self.verticalLayout.addWidget(self.label_logo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_timer = QLabel(self.centralwidget)
        self.label_timer.setObjectName(u"label_timer")

        self.verticalLayout.addWidget(self.label_timer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.image_laborant = QLabel(self.centralwidget)
        self.image_laborant.setObjectName(u"image_laborant")

        self.horizontalLayout.addWidget(self.image_laborant)

        MainWindow_laborant.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_laborant)

        QMetaObject.connectSlotsByName(MainWindow_laborant)
    # setupUi

    def retranslateUi(self, MainWindow_laborant):
        MainWindow_laborant.setWindowTitle(QCoreApplication.translate("MainWindow_laborant", u"MainWindow", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow_laborant", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0418\u043c\u044f</span></p></body></html>", None))
        self.label_role.setText(QCoreApplication.translate("MainWindow_laborant", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0420\u043e\u043b\u044c</span></p></body></html>", None))
        self.btn_req_order.setText(QCoreApplication.translate("MainWindow_laborant", u"C\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c\n"
"\u0437\u0430\u043a\u0430\u0437", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow_laborant", u"TextLabel", None))
        self.label_timer.setText(QCoreApplication.translate("MainWindow_laborant", u"TextLabel", None))
        self.image_laborant.setText(QCoreApplication.translate("MainWindow_laborant", u"<html><head/><body><p>img</p></body></html>", None))
    # retranslateUi

