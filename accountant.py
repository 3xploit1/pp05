import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from forms.ui_form_accountant import * 
from database.db import DataBase


class Accountant(QMainWindow, DataBase): 
    '''
    Класс Accountant описывает логику работы бухгалтера
    
    Атрибуты
    --------
        user : str 
            Логин пользователя 
    
    Методы
    ------
        load()
            Загружает данные пользователя
    '''
    
    def __init__(self, user ,parent=None):
        super(Accountant, self).__init__(parent)
        self.ui = Ui_MainWindow_accountant()
        self.ui.setupUi(self)
        self.setWindowTitle('Бухгалтер')
        self.user = user
        self.set_connect()
        self.load()
    
    def load(self): 
        data = self.get_data_user(self.user)
        if (len(data) > 2 ): 
            self.ui.label_name_accountant.setText(data[0])
            self.ui.label_surname_accountant.setText(data[1])
            self.ui.label_role_accountant.setText(data[2])
            pix = QPixmap()
            if pix.loadFromData(data[3]):
                self.ui.image_laborant_accountant.setPixmap(pix)