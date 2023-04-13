# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_changeymnGRm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogChange(object):
    def setupUi(self, DialogChange):
        if not DialogChange.objectName():
            DialogChange.setObjectName(u"DialogChange")
        DialogChange.resize(648, 383)
        self.horizontalLayout = QHBoxLayout(DialogChange)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_logo = QLabel(DialogChange)
        self.label_logo.setObjectName(u"label_logo")

        self.verticalLayout.addWidget(self.label_logo)

        self.le_full = QLineEdit(DialogChange)
        self.le_full.setObjectName(u"le_full")

        self.verticalLayout.addWidget(self.le_full)

        self.le_login = QLineEdit(DialogChange)
        self.le_login.setObjectName(u"le_login")

        self.verticalLayout.addWidget(self.le_login)

        self.le_pwd = QLineEdit(DialogChange)
        self.le_pwd.setObjectName(u"le_pwd")

        self.verticalLayout.addWidget(self.le_pwd)

        self.le_socia_sec_number = QLineEdit(DialogChange)
        self.le_socia_sec_number.setObjectName(u"le_socia_sec_number")

        self.verticalLayout.addWidget(self.le_socia_sec_number)

        self.le_ein = QLineEdit(DialogChange)
        self.le_ein.setObjectName(u"le_ein")

        self.verticalLayout.addWidget(self.le_ein)

        self.len_social_type = QLineEdit(DialogChange)
        self.len_social_type.setObjectName(u"len_social_type")

        self.verticalLayout.addWidget(self.len_social_type)

        self.le_passport_s = QLineEdit(DialogChange)
        self.le_passport_s.setObjectName(u"le_passport_s")

        self.verticalLayout.addWidget(self.le_passport_s)

        self.le_passport_n = QLineEdit(DialogChange)
        self.le_passport_n.setObjectName(u"le_passport_n")

        self.verticalLayout.addWidget(self.le_passport_n)

        self.le_bday = QLineEdit(DialogChange)
        self.le_bday.setObjectName(u"le_bday")

        self.verticalLayout.addWidget(self.le_bday)

        self.cbox_insurance = QComboBox(DialogChange)
        self.cbox_insurance.setObjectName(u"cbox_insurance")

        self.verticalLayout.addWidget(self.cbox_insurance)

        self.btn_load = QPushButton(DialogChange)
        self.btn_load.setObjectName(u"btn_load")

        self.verticalLayout.addWidget(self.btn_load)

        self.btn_req_change = QPushButton(DialogChange)
        self.btn_req_change.setObjectName(u"btn_req_change")

        self.verticalLayout.addWidget(self.btn_req_change)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lstView_patients = QTableWidget(DialogChange)
        self.lstView_patients.setObjectName(u"lstView_patients")
        self.lstView_patients.setMinimumSize(QSize(450, 0))

        self.verticalLayout_2.addWidget(self.lstView_patients)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(DialogChange)

        QMetaObject.connectSlotsByName(DialogChange)
    # setupUi

    def retranslateUi(self, DialogChange):
        DialogChange.setWindowTitle(QCoreApplication.translate("DialogChange", u"Dialog", None))
        self.label_logo.setText(QCoreApplication.translate("DialogChange", u"TextLabel", None))
        self.btn_load.setText(QCoreApplication.translate("DialogChange", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.btn_req_change.setText(QCoreApplication.translate("DialogChange", u"\u041e\u041a", None))
    # retranslateUi

