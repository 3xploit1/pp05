import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_forms.ui_form_auth import *  
from db_manager.db import DataBase

class Dialog(QDialog, DataBase):
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.set_connect()


    def auth_details(self): 
        return self.ui.line_login.text(), self.ui.line_password.text()


    def move(self, flag): 
        '''
        Редирект к функционалу: 
        0 - лаборант
        1 - лаборант-исследователь
        2 - бухгалтер
        3 - администратор
        '''
        
        ... 

    def captcha(self):
        ...  

    def process_auth(self): 
        '''
        Процесс авторизации
        '''
        usr_log, usr_pas = self.auth_details()
        try: 
            if (usr_log != '') and (usr_pas != ''): 
                data = self.set_auth()
                if (data[0] == usr_log) and (data[1] == usr_pas) and (data[4] == 'лаборант' ): # проверять возвращаемую роль
                    self.move(0)
                elif (data[0] == usr_log) and (data[1] == usr_pas) and (data[4] == 'лаборант-исследователь' ): # проверять возвращаемую роль
                    self.move(1)
                elif (data[0] == usr_log) and (data[1] == usr_pas) and (data[4] == 'бухгалтер' ): # проверять возвращаемую роль
                    self.move(2)   
                elif (data[0] == usr_log) and (data[1] == usr_pas) and (data[4] == 'администратор' ): # проверять возвращаемую роль
                    self.move(3)
        except TypeError: 
            QMessageBox.warning(QMessageBox(), 'Ошибка','Такого пользователя не существует, либо пароль не вверный')
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dialog()
    
    window.show()
    sys.exit(app.exec_())