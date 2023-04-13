# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_view_visitsOFVoCF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogView(object):
    def setupUi(self, DialogView):
        if not DialogView.objectName():
            DialogView.setObjectName(u"DialogView")
        DialogView.resize(487, 352)
        DialogView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(DialogView)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_logo = QLabel(DialogView)
        self.label_logo.setObjectName(u"label_logo")

        self.verticalLayout_2.addWidget(self.label_logo)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget_view = QTableWidget(DialogView)
        self.tableWidget_view.setObjectName(u"tableWidget_view")

        self.verticalLayout.addWidget(self.tableWidget_view)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(DialogView)

        QMetaObject.connectSlotsByName(DialogView)
    # setupUi

    def retranslateUi(self, DialogView):
        DialogView.setWindowTitle(QCoreApplication.translate("DialogView", u"Dialog", None))
        self.label_logo.setText(QCoreApplication.translate("DialogView", u"TextLabel", None))
    # retranslateUi

