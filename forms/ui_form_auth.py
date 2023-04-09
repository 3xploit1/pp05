# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_autheBzidn.ui'
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
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QSize(400, 300))
        Dialog.setMaximumSize(QSize(400, 300))
        self.line_login = QLineEdit(Dialog)
        self.line_login.setObjectName(u"line_login")
        self.line_login.setGeometry(QRect(60, 100, 291, 31))
        self.line_password = QLineEdit(Dialog)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setGeometry(QRect(60, 150, 291, 31))
        self.btn_auth = QPushButton(Dialog)
        self.btn_auth.setObjectName(u"btn_auth")
        self.btn_auth.setGeometry(QRect(140, 200, 91, 41))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 341, 71))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.line_login.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.line_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_auth.setText(QCoreApplication.translate("Dialog", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f</span></p></body></html>", None))
    # retranslateUi

