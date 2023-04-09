import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from forms.ui_form_auth import * 
from lab_assistant import * 
from lab_isled import * 
from accountant import * 
from admin import *
from challenge import * 
from database.db import DataBase


class Dialog(QDialog, DataBase):
    '''
    Класс Dialog описывает логику работы авторизации 
    
    Методы 
    ------
        move_laborant()
            Создание экземпляра класса LabAssistant, описывающего логику работы лаборанта
    
        move_laborant_isled()
            Создание экземпляра класса LabIsled, описывающего логику работы лаборанта-исследователя
       
       move_accountant()
            Создание экземпляра класса Accountant, описывающего логику работы бухгалтера
       
       move_admin()
            Создание экземпляра класса Accountant, описывающего логику работы бухгалтера
    
        captcha()
            Создание экземпляра класса Challenge, описывающего логику работы капчи
            
        process_auth()
            Процесс авторизации
    '''
    
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self)
        self.set_connect()
        self.ui.btn_auth.clicked.connect(self.process_auth)

    def move_laborant(self): 
        self.accept()
        window = LabAssistant(self.ui.line_login.text())
        window.show()
        window.exec_()
    
    def move_laborant_isled(self): 
        self.accept()
        laborant_isled = LabIsled(self.ui.line_login.text())
        laborant_isled.show()
        laborant_isled.exec_()
    
    def move_accountant(self): 
        self.accept()
        accountant = Accountant(self.ui.line_login.text())
        accountant.show()
        accountant.exec_()
    
    def move_admin(self): 
        self.accept()
        admin = Admin(self.ui.line_login.text())
        admin.show()
        admin.exec_()
    
    def captcha(self):
        captcha = Challenge()
        captcha.show()
        captcha.exec_()

    def process_auth(self): 
        usr_log, usr_pas = self.ui.line_login.text(), self.ui.line_password.text()
        try: 
            if (usr_log != '') and (usr_pas != ''): 
                data = self.set_auth(usr_log, usr_pas)
                if (len(data) == 3): 
                    if (data[0] == usr_log) and (data[1] == usr_pas) and (data[2] == 'Лаборант' ): 
                        self.move_laborant()
                    elif (data[0] == usr_log) and (data[1] == usr_pas) and (data[2] == 'Лаборант-исследователь' ): 
                        self.move_laborant_isled()
                    elif (data[0] == usr_log) and (data[1] == usr_pas) and (data[2] == 'Бухгалтер' ): 
                        self.move_accountant()
                    elif (data[0] == usr_log) and (data[1] == usr_pas) and (data[2] == 'Администратор' ): 
                        self.move_admin() 
            else: 
                raise TypeError
        except TypeError: 
            self.captcha()
            # QMessageBox.warning(QMessageBox(), 'Ошибка','Такого пользователя не существует, либо пароль не вверный')
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dialog()
    window.show()
    sys.exit(app.exec_())