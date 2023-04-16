# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_add_patientqFXEAh.ui'
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
        DialogAddPatient.resize(235, 515)
        icon = QIcon()
        icon.addFile(u"../../Resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        DialogAddPatient.setWindowIcon(icon)
        DialogAddPatient.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_6 = QVBoxLayout(DialogAddPatient)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_logo = QLabel(DialogAddPatient)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(0, 150))

        self.verticalLayout_4.addWidget(self.label_logo)

        self.le_fio = QLineEdit(DialogAddPatient)
        self.le_fio.setObjectName(u"le_fio")

        self.verticalLayout_4.addWidget(self.le_fio)

        self.le_login = QLineEdit(DialogAddPatient)
        self.le_login.setObjectName(u"le_login")

        self.verticalLayout_4.addWidget(self.le_login)

        self.le_password = QLineEdit(DialogAddPatient)
        self.le_password.setObjectName(u"le_password")

        self.verticalLayout_4.addWidget(self.le_password)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.le_b_day = QLineEdit(DialogAddPatient)
        self.le_b_day.setObjectName(u"le_b_day")

        self.verticalLayout_5.addWidget(self.le_b_day)

        self.le_passport_series = QLineEdit(DialogAddPatient)
        self.le_passport_series.setObjectName(u"le_passport_series")

        self.verticalLayout_5.addWidget(self.le_passport_series)

        self.le_passport_number = QLineEdit(DialogAddPatient)
        self.le_passport_number.setObjectName(u"le_passport_number")

        self.verticalLayout_5.addWidget(self.le_passport_number)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.le_ein = QLineEdit(DialogAddPatient)
        self.le_ein.setObjectName(u"le_ein")

        self.verticalLayout_2.addWidget(self.le_ein)

        self.le_policy_number = QLineEdit(DialogAddPatient)
        self.le_policy_number.setObjectName(u"le_policy_number")

        self.verticalLayout_2.addWidget(self.le_policy_number)

        self.cbox_type_policy = QComboBox(DialogAddPatient)
        self.cbox_type_policy.setObjectName(u"cbox_type_policy")

        self.verticalLayout_2.addWidget(self.cbox_type_policy)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.le_phone = QLineEdit(DialogAddPatient)
        self.le_phone.setObjectName(u"le_phone")

        self.verticalLayout.addWidget(self.le_phone)

        self.le_email = QLineEdit(DialogAddPatient)
        self.le_email.setObjectName(u"le_email")

        self.verticalLayout.addWidget(self.le_email)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cbox_name_company = QComboBox(DialogAddPatient)
        self.cbox_name_company.setObjectName(u"cbox_name_company")

        self.verticalLayout_3.addWidget(self.cbox_name_company)

        self.btn_req = QPushButton(DialogAddPatient)
        self.btn_req.setObjectName(u"btn_req")
        self.btn_req.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgb(73,140,81);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_req)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)


        self.retranslateUi(DialogAddPatient)

        QMetaObject.connectSlotsByName(DialogAddPatient)
    # setupUi

    def retranslateUi(self, DialogAddPatient):
        DialogAddPatient.setWindowTitle(QCoreApplication.translate("DialogAddPatient", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_logo.setText(QCoreApplication.translate("DialogAddPatient", u"TextLabel", None))
        self.le_fio.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u0424\u0418\u041e", None))
        self.le_login.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.le_password.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.le_b_day.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.le_passport_series.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u0421\u0435\u0440\u0438\u044f \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.le_passport_number.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.le_ein.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"ein", None))
        self.le_policy_number.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u041d\u043e\u043c\u0435\u0440 \u0441\u0442\u0440\u0430\u0445\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u0438\u0441\u0430", None))
        self.cbox_type_policy.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u0422\u0438\u043f \u0441\u0442\u0440\u0430\u0445\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u0438\u0441\u0430", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.le_email.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"e-mail", None))
        self.cbox_name_company.setPlaceholderText(QCoreApplication.translate("DialogAddPatient", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0440\u0430\u0445\u043e\u0432\u043e\u0439 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.btn_req.setText(QCoreApplication.translate("DialogAddPatient", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

