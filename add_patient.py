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
        self.setWindowIcon(QIcon('resources\/logo.ico'))
        pix = QPixmap('resources\/logo.png')
        self.ui.label_logo.setPixmap(pix)
        self.ui.label_logo.setScaledContents(True)
        self.ui.btn_req.clicked.connect(self.make_patient)
        
        type_policy = [
            'oms',
            'dms',
        ]
        
        self.ui.cbox_name_company.addItems(self.get_name_company())
        self.ui.cbox_type_policy.addItems(type_policy)
            
    def make_patient(self): 
        full = self.ui.le_fio.text()
        login = self.ui.le_login.text()
        pwd = self.ui.le_password.text()
        email = self.ui.le_email.text()
        social_sec_number = self.ui.le_policy_number.text()
        ein = self.ui.le_ein.text()
        social_type = self.ui.cbox_type_policy.currentText()
        phone = self.ui.le_phone.text()
        passport_s = self.ui.le_passport_series.text()
        passport_n = self.ui.le_passport_number.text()
        birthdate_timestamp = self.ui.le_b_day.text()
        id_insurance = self.get_id_company(self.ui.cbox_name_company.currentText())
        
        try: 
            if (full != '' and login != '' and pwd != '' and 
                email != '' and social_sec_number != '' and social_sec_number != '' and 
                ein != '' and social_type != '' and phone != '' and 
                passport_s != '' and passport_n != '' and birthdate_timestamp != '' and id_insurance != ''): 
                self.add_patient(
                    full,
                    login,
                    pwd, 
                    email,
                    social_sec_number,
                    ein,
                    social_type,
                    phone,
                    passport_s,
                    passport_n, 
                    birthdate_timestamp,
                    id_insurance
                )
                QMessageBox.information(QMessageBox(), 'Успешно','Пользователь добавлен')
                self.accept()
            else:
                raise TypeError
        except TypeError: 
            QMessageBox.warning(QMessageBox(), 'Ошибка','Заполните все поля')
