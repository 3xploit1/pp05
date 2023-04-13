# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_authcRIFnF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(395, 316)
        Dialog.setMinimumSize(QSize(0, 0))
        Dialog.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"../../Resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_logo = QLabel(Dialog)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(0, 150))
        self.label_logo.setPixmap(QPixmap(u"../../Resources/logo.ico"))

        self.verticalLayout.addWidget(self.label_logo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.line_login = QLineEdit(Dialog)
        self.line_login.setObjectName(u"line_login")

        self.verticalLayout.addWidget(self.line_login)

        self.line_password = QLineEdit(Dialog)
        self.line_password.setObjectName(u"line_password")

        self.verticalLayout.addWidget(self.line_password)

        self.btn_auth = QPushButton(Dialog)
        self.btn_auth.setObjectName(u"btn_auth")
        self.btn_auth.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(73,140,81);\n"
"}")

        self.verticalLayout.addWidget(self.btn_auth)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f</span></p></body></html>", None))
        self.label_logo.setText("")
        self.line_login.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.line_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_auth.setText(QCoreApplication.translate("Dialog", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
    # retranslateUi

