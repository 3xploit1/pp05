import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from forms.ui_form_admin import * 
from database.db import DataBase
from view_visits import *


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
    def __init__(self,parent=None):
        super(Admin, self).__init__(parent)
        self.ui = Ui_MainWindow_admin()
        self.ui.setupUi(self)
        self.setWindowTitle('Администратор')
        self.setWindowIcon(QIcon('resources\/logo.ico'))
        pix = QPixmap('resources\/logo.png')
        self.ui.label_logo.setPixmap(pix)
        self.ui.label_logo.setScaledContents(True)
        self.ui.btn_view.clicked.connect(self.move_view)
        self.set_connect()
        self.load()
        
    def load(self): 
        self.ui.label_name_admin.setText('Администратор')
        self.ui.label_role_admin.setText('Администратор')
        pix = QPixmap('resources\/Администратор.png')
        self.ui.image_laborant_admin.setPixmap(pix)
        self.ui.image_laborant_admin.setScaledContents(True)
    
    def move_view(self):
        view = ViewUsers()
        view.show()
        view.exec_()

        


    