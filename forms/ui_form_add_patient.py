# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_add_patientraGvaO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogAddPatient(object):
    def setupUi(self, DialogAddPatient):
        if not DialogAddPatient.objectName():
            DialogAddPatient.setObjectName(u"DialogAddPatient")
        DialogAddPatient.resize(570, 390)
        self.btn_req = QPushButton(DialogAddPatient)
        self.btn_req.setObjectName(u"btn_req")
        self.btn_req.setGeometry(QRect(460, 340, 101, 41))
        self.cbox_type_policy = QComboBox(DialogAddPatient)
        self.cbox_type_policy.setObjectName(u"cbox_type_policy")
        self.cbox_type_policy.setGeometry(QRect(300, 240, 261, 31))
        self.cbox_name_company = QComboBox(DialogAddPatient)
        self.cbox_name_company.setObjectName(u"cbox_name_company")
        self.cbox_name_company.setGeometry(QRect(10, 320, 261, 31))
        self.le_surname = QLineEdit(DialogAddPatient)
        self.le_surname.setObjectName(u"le_surname")
        self.le_surname.setGeometry(QRect(10, 20, 261, 31))
        self.le_name = QLineEdit(DialogAddPatient)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setGeometry(QRect(10, 70, 261, 31))
        self.le_middle_name = QLineEdit(DialogAddPatient)
        self.le_middle_name.setObjectName(u"le_middle_name")
        self.le_middle_name.setGeometry(QRect(10, 120, 261, 31))
        self.le_b_day = QLineEdit(DialogAddPatient)
        self.le_b_day.setObjectName(u"le_b_day")
        self.le_b_day.setGeometry(QRect(300, 20, 261, 31))
        self.le_passport_series = QLineEdit(DialogAddPatient)
        self.le_passport_series.setObjectName(u"le_passport_series")
        self.le_passport_series.setGeometry(QRect(300, 70, 261, 31))
        self.le_passport_number = QLineEdit(DialogAddPatient)
        self.le_passport_number.setObjectName(u"le_passport_number")
        self.le_passport_number.setGeometry(QRect(300, 120, 261, 31))
        self.le_phone = QLineEdit(DialogAddPatient)
        self.le_phone.setObjectName(u"le_phone")
        self.le_phone.setGeometry(QRect(10, 200, 261, 31))
        self.le_email = QLineEdit(DialogAddPatient)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setGeometry(QRect(10, 240, 261, 31))
        self.le_policy_number = QLineEdit(DialogAddPatient)
        self.le_policy_number.setObjectName(u"le_policy_number")
        self.le_policy_number.setGeometry(QRect(300, 200, 261, 31))

        self.retranslateUi(DialogAddPatient)

        QMetaObject.connectSlotsByName(DialogAddPatient)
    # setupUi

    def retranslateUi(self, DialogAddPatient):
        DialogAddPatient.setWindowTitle(QCoreApplication.translate("DialogAddPatient", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.btn_req.setText(QCoreApplication.translate("DialogAddPatient", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cbox_type_policy.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u0422\u0438\u043f \u0441\u0442\u0440\u0430\u0445\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u0438\u0441\u0430", None))
        self.cbox_name_company.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0440\u0430\u0445\u043e\u0432\u043e\u0439 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.le_surname.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.le_name.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u0418\u043c\u044f", None))
        self.le_middle_name.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.le_b_day.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.le_passport_series.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u0421\u0435\u0440\u0438\u044f \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.le_passport_number.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.le_email.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"e-mail", None))
        self.le_policy_number.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u041d\u043e\u043c\u0435\u0440 \u0441\u0442\u0440\u0430\u0445\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u0438\u0441\u0430", None))
    # retranslateUi

