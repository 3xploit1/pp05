import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from forms.ui_form_admin import * 
from database.db import DataBase


class Admin(QMainWindow, DataBase): 
    '''
    Класс Admin описывает логику работы администратора 
    
    Атрибуты
    --------
        user : str 
            Логин пользователя 
    
    Методы
    ------
        load()
            Загружает данные пользователя
    '''
    def __init__(self, user, parent=None):
        super(Admin, self).__init__(parent)
        self.ui = Ui_MainWindow_admin()
        self.ui.setupUi(self)
        self.setWindowTitle('Администратор')
        self.user = user 
        self.set_connect()
        self.load()

    def load(self): 
        data = self.get_data_user(self.user)
        if (len(data) > 2 ): 
            self.ui.label_name_admin.setText(data[0])
            self.ui.label_surname_admin.setText(data[1])
            self.ui.label_role_admin.setText(data[2])
            pix = QPixmap()
            if pix.loadFromData(data[3]):
                self.ui.image_laborant_admin.setPixmap(pix)

        


    