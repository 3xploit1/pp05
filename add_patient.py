import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from forms.ui_form_add_patient import * 
from database.db import *

class AddPatient(QDialog, DataBase): 
    '''
    Класс AddPatient описывает логику работы добавления новых пациентов
    
    Атрибуты
    --------
        company : list
            Список компаний
        type_policy : list 
            Список типов страхового полиса
    
    Методы
    ------
        make_patient()
            Добавляет пользователя в БД
    '''
    
    def __init__(self) :
        super(AddPatient, self).__init__()
        self.ui = Ui_DialogAddPatient()
        self.ui.setupUi(self)
        self.set_connect()
        self.ui.btn_req.clicked.connect(self.make_patient)
        company = [
            'company1',
            'company2',
            'company3',
        ]
        type_policy = [
            'Бумажный',
            'Электронный',
            'Универсальный'
        ]
        
        self.ui.cbox_name_company.addItems(company)
        self.ui.cbox_type_policy.addItems(type_policy)
            
    def make_patient(self): 
        name = self.ui.le_name.text()
        surname = self.ui.le_surname.text()
        middle_name = self.ui.le_middle_name.text()
        bday = self.ui.le_b_day.text()
        pas_series = self.ui.le_passport_series.text()
        pas_number = self.ui.le_passport_number.text()
        phone = self.ui.le_phone.text()
        email = self.ui.le_email.text()
        policy_number = self.ui.le_policy_number.text()
        type_policy = self.ui.cbox_type_policy.currentText()
        name_company = self.ui.cbox_name_company.currentText()
        
        try: 
            if (name != '' and surname != '' and middle_name != '' and 
                bday != '' and pas_series != '' and pas_number != '' and 
                phone != '' and email != '' and policy_number != '' and 
                type_policy != '' and name_company != ''): 
                self.add_patient(
                    name,
                    surname,
                    middle_name, 
                    bday,
                    pas_series,
                    pas_number,
                    phone,
                    email,
                    policy_number,
                    type_policy, 
                    name_company
                )
                QMessageBox.information(QMessageBox(), 'Успешно','Пользователь добавлен')
                self.accept()
            else:
                raise TypeError
        except TypeError: 
            QMessageBox.warning(QMessageBox(), 'Ошибка','Заполните все поля')

