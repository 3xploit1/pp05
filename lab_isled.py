from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from forms.ui_form_laborant_is import * 
from database.db import DataBase

SESSION_SEC = 500

class LabIsled(QMainWindow, DataBase): 
    '''
    Класс LabAssistant описывает логику работы лаборанта
    
    Константы
    ---------
        SESSION_SEC : время сессии в секундах 
    
    Атрибуты
    --------
        user : str 
            Логин пользователя 
    
    Методы
    ------
        load()
            Загружает данные пользователя
        
        message()
            Сообщение о скором завершении сессии 
        
        startTimer()
        timerTimeout()
        update_gui()
            Логика работы таймера
    '''
    
    def __init__(self, user, parent=None):
        super(LabIsled, self).__init__(parent)
        self.ui = Ui_MainWindow_laborant_is()
        self.ui.setupUi(self)
        self.setWindowTitle('Лаборант-исследователь')
        self.setWindowIcon(QIcon('resources\/logo.ico'))
        pix = QPixmap('resources\/logo.png')
        self.ui.label_logo.setPixmap(pix)
        self.ui.label_logo.setScaledContents(True)
        QTimer.singleShot(SESSION_SEC * 1000 , self.close) # 600000
        QTimer.singleShot((SESSION_SEC * 1000 / 2) , self.message)
        self.user = user
        self.set_connect()
        self.load()
        self.startTimer()
    
    def load(self): 
        data = self.get_data_user(self.user)
        if (len(data) == 1 ): 
            self.ui.label_name_is.setText(data[0])
            self.ui.label_role_is.setText('Лаборант-исследователь')
            pix = QPixmap('resources\/laborant_2.png')
            self.ui.image_laborant_is.setPixmap(pix)
    
    def message(self): 
        QMessageBox.warning(QMessageBox(), 'Информация', f"У вас осталось {(SESSION_SEC / 2)} секунд")
    
    def startTimer(self):
        self.time_left_int = SESSION_SEC
        self.myTimer = QTimer(self)
        self.myTimer.timeout.connect(self.timerTimeout)
        self.myTimer.start(1000)

    def timerTimeout(self):
        self.time_left_int -= 1

        if self.time_left_int == 0:
            self.time_left_int = SESSION_SEC

        self.update_gui()

    def update_gui(self):
        self.ui.label_timer.setText(str(self.time_left_int))
        


    