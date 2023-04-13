# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_formation_orderxrFBlF.ui'
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
        Dialog_order_formation.resize(278, 244)
        icon = QIcon()
        icon.addFile(u"../../Resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_order_formation.setWindowIcon(icon)
        Dialog_order_formation.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QVBoxLayout(Dialog_order_formation)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.le_code = QLineEdit(Dialog_order_formation)
        self.le_code.setObjectName(u"le_code")

        self.verticalLayout_2.addWidget(self.le_code)

        self.le_fio = QLineEdit(Dialog_order_formation)
        self.le_fio.setObjectName(u"le_fio")

        self.verticalLayout_2.addWidget(self.le_fio)

        self.li_pas_num = QLineEdit(Dialog_order_formation)
        self.li_pas_num.setObjectName(u"li_pas_num")

        self.verticalLayout_2.addWidget(self.li_pas_num)

        self.cbox_serv = QComboBox(Dialog_order_formation)
        self.cbox_serv.setObjectName(u"cbox_serv")

        self.verticalLayout_2.addWidget(self.cbox_serv)

        self.label_logo = QLabel(Dialog_order_formation)
        self.label_logo.setObjectName(u"label_logo")

        self.verticalLayout_2.addWidget(self.label_logo)

        self.btn_req = QPushButton(Dialog_order_formation)
        self.btn_req.setObjectName(u"btn_req")
        self.btn_req.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(73,140,81);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_req)

        self.btn_update_user = QPushButton(Dialog_order_formation)
        self.btn_update_user.setObjectName(u"btn_update_user")
        self.btn_update_user.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(73,140,81);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_update_user)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog_order_formation)

        QMetaObject.connectSlotsByName(Dialog_order_formation)
    # setupUi

    def retranslateUi(self, Dialog_order_formation):
        Dialog_order_formation.setWindowTitle(QCoreApplication.translate("Dialog_order_formation", u"\u0424\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.le_code.setPlaceholderText(QCoreApplication.translate("Dialog_order_formation", u"\u041a\u043e\u0434 \u043f\u0440\u043e\u0431\u0438\u0440\u043a\u0438", None))
        self.le_fio.setPlaceholderText(QCoreApplication.translate("Dialog_order_formation", u"\u0424\u0418\u041e", None))
        self.li_pas_num.setPlaceholderText(QCoreApplication.translate("Dialog_order_formation", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.cbox_serv.setPlaceholderText(QCoreApplication.translate("Dialog_order_formation", u"\u0423\u0441\u043b\u0443\u0433\u0430", None))
        self.label_logo.setText(QCoreApplication.translate("Dialog_order_formation", u"TextLabel", None))
        self.btn_req.setText(QCoreApplication.translate("Dialog_order_formation", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btn_update_user.setText(QCoreApplication.translate("Dialog_order_formation", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
    # retranslateUi

