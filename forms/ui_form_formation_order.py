# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_formation_orderWtcTxY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_order_formation(object):
    def setupUi(self, Dialog_order_formation):
        if not Dialog_order_formation.objectName():
            Dialog_order_formation.setObjectName(u"Dialog_order_formation")
        Dialog_order_formation.resize(346, 311)
        self.btn_req = QPushButton(Dialog_order_formation)
        self.btn_req.setObjectName(u"btn_req")
        self.btn_req.setGeometry(QRect(120, 260, 101, 41))
        self.le_code = QLineEdit(Dialog_order_formation)
        self.le_code.setObjectName(u"le_code")
        self.le_code.setGeometry(QRect(12, 10, 321, 31))
        self.le_surname = QLineEdit(Dialog_order_formation)
        self.le_surname.setObjectName(u"le_surname")
        self.le_surname.setGeometry(QRect(10, 60, 321, 31))
        self.le_name = QLineEdit(Dialog_order_formation)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setGeometry(QRect(10, 110, 321, 31))
        self.le_middle_name = QLineEdit(Dialog_order_formation)
        self.le_middle_name.setObjectName(u"le_middle_name")
        self.le_middle_name.setGeometry(QRect(10, 160, 321, 31))
        self.le_service = QLineEdit(Dialog_order_formation)
        self.le_service.setObjectName(u"le_service")
        self.le_service.setGeometry(QRect(10, 210, 321, 31))

        self.retranslateUi(Dialog_order_formation)

        QMetaObject.connectSlotsByName(Dialog_order_formation)
    # setupUi

    def retranslateUi(self, Dialog_order_formation):
        Dialog_order_formation.setWindowTitle(QCoreApplication.translate("Dialog_order_formation", u"\u0424\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.btn_req.setText(QCoreApplication.translate("Dialog_order_formation", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.le_code.setPlaceholderText(QCoreApplication.translate("Dialog_order_formation", u"\u041a\u043e\u0434 \u043f\u0440\u043e\u0431\u0438\u0440\u043a\u0438", None))
        self.le_surname.setPlaceholderText(QCoreApplication.translate("Dialog_order_formation", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.le_name.setPlaceholderText(QCoreApplication.translate("Dialog_order_formation", u"\u0418\u043c\u044f", None))
        self.le_middle_name.setPlaceholderText(QCoreApplication.translate("Dialog_order_formation", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.le_service.setPlaceholderText(QCoreApplication.translate("Dialog_order_formation", u"\u0423\u0441\u043b\u0443\u0433\u0430", None))
    # retranslateUi

