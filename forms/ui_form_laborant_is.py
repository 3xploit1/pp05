# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_laborant_isQtcGRF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow_laborant_is(object):
    def setupUi(self, MainWindow_laborant_is):
        if not MainWindow_laborant_is.objectName():
            MainWindow_laborant_is.setObjectName(u"MainWindow_laborant_is")
        MainWindow_laborant_is.resize(577, 305)
        icon = QIcon()
        icon.addFile(u"../../Resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow_laborant_is.setWindowIcon(icon)
        MainWindow_laborant_is.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow_laborant_is)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name_is = QLabel(self.centralwidget)
        self.label_name_is.setObjectName(u"label_name_is")
        font = QFont()
        font.setPointSize(16)
        self.label_name_is.setFont(font)

        self.verticalLayout.addWidget(self.label_name_is)

        self.label_role_is = QLabel(self.centralwidget)
        self.label_role_is.setObjectName(u"label_role_is")
        self.label_role_is.setFont(font)

        self.verticalLayout.addWidget(self.label_role_is)

        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")

        self.verticalLayout.addWidget(self.label_logo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_timer = QLabel(self.centralwidget)
        self.label_timer.setObjectName(u"label_timer")

        self.verticalLayout.addWidget(self.label_timer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.image_laborant_is = QLabel(self.centralwidget)
        self.image_laborant_is.setObjectName(u"image_laborant_is")

        self.horizontalLayout.addWidget(self.image_laborant_is)

        MainWindow_laborant_is.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_laborant_is)

        QMetaObject.connectSlotsByName(MainWindow_laborant_is)
    # setupUi

    def retranslateUi(self, MainWindow_laborant_is):
        MainWindow_laborant_is.setWindowTitle(QCoreApplication.translate("MainWindow_laborant_is", u"MainWindow", None))
        self.label_name_is.setText(QCoreApplication.translate("MainWindow_laborant_is", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0418\u043c\u044f</span></p></body></html>", None))
        self.label_role_is.setText(QCoreApplication.translate("MainWindow_laborant_is", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0420\u043e\u043b\u044c</span></p></body></html>", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow_laborant_is", u"TextLabel", None))
        self.label_timer.setText(QCoreApplication.translate("MainWindow_laborant_is", u"TextLabel", None))
        self.image_laborant_is.setText(QCoreApplication.translate("MainWindow_laborant_is", u"<html><head/><body><p>img</p></body></html>", None))
    # retranslateUi

