from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from forms.ui_form_view_visits import *
from database.db import *


class ViewUsers(QDialog, DataBase): 
    def __init__(self) :
        super(ViewUsers, self).__init__()
        self.ui = Ui_DialogView()
        self.ui.setupUi(self)
        self.set_connect()
        self.setWindowIcon(QIcon('resources\/logo.ico'))
        pix = QPixmap('resources\/logo.png')
        self.ui.label_logo.setPixmap(pix)
        self.ui.label_logo.setScaledContents(True)
        self.load()
    
    def load(self): 
        patients = self.get_visits()
        products_rows = len(patients)
        products_columns = len(patients[0])
        self.ui.tableWidget_view.setRowCount(products_rows)
        self.ui.tableWidget_view.setColumnCount(products_columns)
        self.ui.tableWidget_view.selectedItems()
        for i in range(products_rows): 
            for j in range(products_columns): 
                item = QTableWidgetItem(f"{patients[i][j]}")
                self.ui.tableWidget_view.setItem(i, j, item) 