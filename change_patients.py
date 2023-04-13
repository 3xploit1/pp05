from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from forms.ui_form_change import *
from database.db import * 


class ChangePatients(QDialog, DataBase): 
    def __init__(self) :
        super(ChangePatients, self).__init__()
        self.ui = Ui_DialogChange()
        self.ui.setupUi(self)
        self.set_connect()
        self.setWindowIcon(QIcon('resources\/logo.ico'))
        pix = QPixmap('resources\/logo.png')
        self.completion_view()
        self.ui.label_logo.setPixmap(pix)
        self.ui.label_logo.setScaledContents(True)
        self.ui.lstView_patients.setHorizontalHeaderLabels(['id', 'full', 'login', 'pwd', 'email', 'social_sec_number', 'ein', 'social_type', 'phone', 'passport_s', 'passport_n', 'bday', 'id_inscurance'])
        
        self.ui.btn_load.clicked.connect(self.completion_line_ed)
        self.ui.btn_req_change.clicked.connect(self.update_pateints)
        
        buffer = []
        for service in self.get_name_company(): 
            buffer.append(service[0])
            
        self.ui.cbox_insurance.addItems(buffer)

    
    def completion_view(self): 
        patients = self.all_patients()
        products_rows = len(patients)
        products_columns = len(patients[0])
        self.ui.lstView_patients.setRowCount(products_rows)
        self.ui.lstView_patients.setColumnCount(products_columns)
        self.ui.lstView_patients.selectedItems()
        for i in range(products_rows): 
            for j in range(products_columns): 
                item = QTableWidgetItem(f"{patients[i][j]}")
                self.ui.lstView_patients.setItem(i, j, item) 
                
        QTimer.singleShot(10000, self.completion_view)

    def completion_line_ed(self):
        self.id = self.ui.lstView_patients.item(self.ui.lstView_patients.currentRow(), self.ui.lstView_patients.currentColumn()).text() 
        data = self.get_patients(self.id)
        self.ui.le_full.setText(data[0])
        self.ui.le_login.setText(data[1])
        self.ui.le_pwd.setText(data[2])
        self.ui.le_socia_sec_number.setText(data[3])
        self.ui.le_ein.setText(data[4])
        self.ui.len_social_type.setText(data[5])
        self.ui.le_passport_s.setText(data[6])
        self.ui.le_passport_n.setText(data[7])
        self.ui.le_bday.setText(data[8])
        name_company = self.get_name_company_by_id(data[9])
        self.ui.cbox_insurance.setCurrentText(name_company[0])

    def update_pateints(self): 
        id_company = self.get_id_company(self.ui.cbox_insurance.currentText())
        self.up_pateints(
            self.id,
            self.ui.le_full.text(),
            self.ui.le_login.text(),
            self.ui.le_pwd.text(),
            self.ui.le_socia_sec_number.text(),
            self.ui.le_ein.text(),
            self.ui.len_social_type.text(),
            self.ui.le_passport_s.text(),
            self.ui.le_passport_n.text(),
            self.ui.le_bday.text(),
            id_company[0]
        )
        QMessageBox.information(QMessageBox(), 'Успешно','Пользователь обновлен')

