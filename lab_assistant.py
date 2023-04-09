from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from forms.ui_form_laborant import * 
from database.db import DataBase
from formation_order import * 


SESSION_SEC = 500

class LabAssistant(QMainWindow, DataBase): 
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
        
        formation_order()
            Создание экземпляра класса FormationOrder, описывающего логику работы формирования заказа
    '''
    
    def __init__(self, user, parent=None):
        super(LabAssistant, self).__init__(parent)
        self.ui = Ui_MainWindow_laborant()
        self.ui.setupUi(self)
        self.setWindowTitle('Лаборант')
        QTimer.singleShot(SESSION_SEC * 1000 , self.close) # 600000
        QTimer.singleShot((SESSION_SEC * 1000 / 2) , self.message)
        self.ui.btn_req_order.clicked.connect(self.formation_order)
        
        self.user = user
        self.set_connect()
        self.load()
        self.startTimer()
    
    def load(self): 
        data = self.get_data_user(self.user)
        if (len(data) > 2 ): 
            self.ui.label_name.setText(data[0])
            self.ui.label_surname.setText(data[1])
            self.ui.label_role.setText(data[2])
            pix = QPixmap()
            if pix.loadFromData(data[3]):
                self.ui.image_laborant.setPixmap(pix)

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

    def formation_order(self): 
        order = FormationOrder()
        order.show()
        order.exec_()