# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_adminJivRiK.ui'
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
        MainWindow_admin.resize(582, 306)
        icon = QIcon()
        icon.addFile(u"../../Resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow_admin.setWindowIcon(icon)
        MainWindow_admin.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow_admin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name_admin = QLabel(self.centralwidget)
        self.label_name_admin.setObjectName(u"label_name_admin")
        font = QFont()
        font.setPointSize(16)
        self.label_name_admin.setFont(font)

        self.verticalLayout.addWidget(self.label_name_admin)

        self.label_role_admin = QLabel(self.centralwidget)
        self.label_role_admin.setObjectName(u"label_role_admin")
        self.label_role_admin.setFont(font)

        self.verticalLayout.addWidget(self.label_role_admin)

        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(0, 150))

        self.verticalLayout.addWidget(self.label_logo)

        self.btn_view = QPushButton(self.centralwidget)
        self.btn_view.setObjectName(u"btn_view")
        self.btn_view.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(73,140,81);\n"
"}")

        self.verticalLayout.addWidget(self.btn_view)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.image_laborant_admin = QLabel(self.centralwidget)
        self.image_laborant_admin.setObjectName(u"image_laborant_admin")

        self.horizontalLayout.addWidget(self.image_laborant_admin)

        MainWindow_admin.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_admin)

        QMetaObject.connectSlotsByName(MainWindow_admin)
    # setupUi

    def retranslateUi(self, MainWindow_admin):
        MainWindow_admin.setWindowTitle(QCoreApplication.translate("MainWindow_admin", u"MainWindow", None))
        self.label_name_admin.setText(QCoreApplication.translate("MainWindow_admin", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0418\u043c\u044f</span></p></body></html>", None))
        self.label_role_admin.setText(QCoreApplication.translate("MainWindow_admin", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0420\u043e\u043b\u044c</span></p></body></html>", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow_admin", u"TextLabel", None))
        self.btn_view.setText(QCoreApplication.translate("MainWindow_admin", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.image_laborant_admin.setText(QCoreApplication.translate("MainWindow_admin", u"<html><head/><body><p>img</p></body></html>", None))
    # retranslateUi

