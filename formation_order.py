import datetime 
import random
import keyboard
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from forms.ui_form_formation_order import * 
from database.db import * 
from add_patient import * 
from change_patients import * 
# docs2pdf  


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
        self.setWindowIcon(QIcon('resources\/logo.ico'))
        pix = QPixmap('resources\/logo.png')
        self.ui.label_logo.setPixmap(pix)
        self.ui.label_logo.setScaledContents(True)
        self.ui.btn_req.clicked.connect(self.make_order)
        self.ui.btn_update_user.clicked.connect(self.move_change)
        self.current_code = 1 
        self.barcode = ''
        self.name_file = ''
        buffer = []
        self.now = datetime.datetime.now()
        
        for service in self.get_name_service(): 
            buffer.append(service[0])
        self.ui.cbox_serv.addItems(buffer)
        
        if self.get_last_code() != None: 
            self.current_code = int(self.get_last_code()[0]) + 1 
        self.ui.le_code.setToolTip(f"Код пробирки {self.current_code}.\nПодтвердите нажатием клавиши Enter")

    def move_change(self): 
        captcha = ChangePatients()
        captcha.show()
        captcha.exec_()

    def make_order(self): 
        
        if keyboard.is_pressed('enter'): 
            self.ui.le_code.setText(str(self.current_code))
            
        self.code = self.ui.le_code.text()
        self.fio = self.ui.le_fio.text()
        self.pas_n = self.ui.li_pas_num.text()
        self.service = self.get_id_service(self.ui.cbox_serv.currentText())
        
        # предусмотреть возможность рандомных значений. Реализовать кнопку анализатор 
        try: 
            if self.code != '' and self.fio != '' and self.pas_n != '' and self.service != '': 
                if self.exist_patient(self.fio, self.pas_n) == True: 
                    self.name_file = self.code + str(self.now.day) + str(self.now.month) + str(self.now.year) + str(uniq_code := random.randint(1000000, 9999999))
                    self.barcode = f"{self.code} {self.now.day} {self.now.month} {self.now.year} {str(uniq_code)}"
                    self.add_order(self.code, self.barcode, str(self.now.day) + str(self.now.month) + str(self.now.year), self.fio, self.pas_n, self.service)
                    self.make_file_barcode() 
                    self.make_file_order() 
                    QMessageBox.information(QMessageBox(), 'Успешно',f'Штрихкод: {self.barcode}')
                    self.accept()
                else: 
                    self.ui.le_code.clear()
                    self.ui.le_fio.clear()
                    self.ui.li_pas_num.clear()
                    QMessageBox.warning(QMessageBox(), 'Ошибка','Пользователя не существует')
                    order = AddPatient()
                    order.show()
                    order.exec_()
        #     else: 
        #         raise TypeError
        except Exception: 
            QMessageBox.warning(QMessageBox(), 'Ошибка',f'{Exception}')
    
    def make_file_barcode(self): 
        with open(name_file_bacode := 'storage\/' + self.name_file + '.txt', 'w') as file: 
            file.write(self.barcode)
        
        self.rename_file(name_file_bacode)
            
    def make_file_order(self): 
        with open(name_file := 'storage\/' + 'order' + str(random.randint(1000000, 9999999)) + '.txt', 'w' ) as file:
            file.write(
                f'Дата: {str(datetime.datetime.now())}'
                f'ФИО: {self.fio}\n'  
                f'Услуга: {self.service}\n'
            )
        self.rename_file(name_file) 
             
    def rename_file(self, file): 
        base = os.path.splitext(file)[0]
        os.rename(file, base + '.pdf')

    


        
        
        
        