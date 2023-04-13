import os
import random
import matplotlib.pyplot as plt
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
        self.setWindowIcon(QIcon('resources\/logo.ico'))
        pix = QPixmap('resources\/logo.png')
        self.ui.label_logo.setPixmap(pix)
        self.ui.label_logo.setScaledContents(True)
        self.ui.btn_req_report.clicked.connect(self.make_report)
        self.ui.btn_req_graph.clicked.connect(self.make_custom_report)
        self.user = user
        self.set_connect()
        self.load()
    
    def load(self): 
        data = self.get_data_user(self.user)
        if (len(data) == 1 ): 
            self.ui.label_name_accountant.setText(data[0])
            self.ui.label_role_accountant.setText('Бухгалтер')
            pix = QPixmap('resources\/laborant_1.jpeg')
            self.ui.image_laborant_accountant.setPixmap(pix)
    
    def make_report(self): 
        with open(name_file := 'storage\/' + 'report'+ str(random.randint(1000000, 9999999)) + '.txt', 'w' ) as file:
            for item in self.get_serv_full():  
                file.write(f"{item[0]} | {item[1]} | {item[2]}")
        self.rename_file(name_file)    
    
    def make_custom_report(self): 
        data = self.count_by_day()
        day = []
        counts = []
        for i in data: 
            day.append(i[0])
            counts.append(i[1])
        plt.bar(day, counts)
        plt.title("Количество по дням")
        plt.xlabel("День")
        plt.ylabel("Количество")
        plt.show()
    
    def rename_file(self, file): 
        base = os.path.splitext(file)[0]
        os.rename(file, base + '.pdf')
        