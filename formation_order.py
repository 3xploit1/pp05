import datetime 
import random
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from forms.ui_form_formation_order import * 
from database.db import * 
from add_patient import * 

class FormationOrder(QDialog, DataBase): 
    '''
    Класс FormationOrder описывает логику работы формирования заказа 
    
    Методы
    ------
        make_order()
            Проверяет наличие пользователя в БД если да, то формирует заказ, 
            иначе создает экземпляр класса AddPatient, описывающий логику добавления 
            пациента 
        
        make_file_barcode()
            Формирует название файла и штрих-код. Производит запись штрих кода. 
            Изменяет расширения с txt на pdf 
        
        make_file_order()
            Формирует название файла и очет. Производит запись отчета. 
            Изменяет расширения с txt на pdf 
        
        rename_file()
            Изменяет расширение
    '''
    
    def __init__(self):
        super(FormationOrder, self).__init__()
        self.ui = Ui_Dialog_order_formation()
        self.ui.setupUi(self)
        self.set_connect()
        self.ui.btn_req.clicked.connect(self.make_order)
        # self.code = ''

    def make_order(self): 
        self.code = self.ui.le_code.text()
        self.surname = self.ui.le_surname.text()
        self.name = self.ui.le_name.text()
        self.middle_name = self.ui.le_middle_name.text()
        self.service = self.ui.le_service.text()
        
        # try: 
        if self.code != '' and self.surname != '' and self.name != '' and self.middle_name != '' and  self.service != '': 
            if self.exist_patient(self.surname, self.name, self.middle_name) == True: 
                self.add_order(self.code, self.surname, self.name, self.middle_name, self.service)
                self.make_file_barcode()
                self.make_file_order()
                QMessageBox.information(QMessageBox(), 'Успешно','Заказ сформирован')
                self.accept()
            else: 
                QMessageBox.warning(QMessageBox(), 'Ошибка','Пользователя не существует')
                order = AddPatient()
                order.show()
                order.exec_()
        #     else: 
        #         raise TypeError
        # except TypeError: 
        #     QMessageBox.warning(QMessageBox(), 'Ошибка','Введены не все поля')
    
    def make_file_barcode(self): 
        now = datetime.datetime.now()
        with open(name_file_bacode := 'storage\/' + self.code + str(now.day) + str(now.month) + str(now.year) + str(uniq_code := random.randint(1000000, 9999999)) + '.txt', 'w') as file: 
            file.write(f"{self.code} {now.day} {now.month} {now.year} {str(uniq_code)}")
        
        self.rename_file(name_file_bacode)
            
    def make_file_order(self): 
        with open(name_file := 'storage\/' + str(random.randint(1000000, 9999999)) + '.txt', 'w' ) as file:
            file.write(
                f'Дата: {str(datetime.datetime.now())}'
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Отчество: {self.middle_name}\n'
                f'Услуга: {self.service}\n'
            )
        self.rename_file(name_file) 
             
    def rename_file(self, file): 
        base = os.path.splitext(file)[0]
        os.rename(file, base + '.pdf')

    


        
        
        
        