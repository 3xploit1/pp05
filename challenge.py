import random
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from forms.ui_form_challenge import *


class Challenge(QDialog): 
    '''
    Класс Challenge описывает логику работы капчи 
    
    Атрибуты 
    --------
        captcha_pack : dict
            словарь ссылок на png, где ключем является правильный код для решения,
            а значением ссылка на png
        code : str
            текущий правильный код

    Методы 
    ------
        load_img()
            Смена картинки на случайное значение из словаря captcha_pack, 
            смена правильного кода 
        
        process()
            Процесс решения капчи. Если ответ верный форма Challenge закрывается, 
            иначе блокировка кнопок на 10 секунд, очищение поля ввода 
    '''
    
    def __init__(self): 
        super(Challenge, self).__init__()
        self.ui = Ui_Main_challenge()
        self.ui.setupUi(self)
        self.ui.btn_reload_img.clicked.connect(self.load_img)
        self.ui.btn_request.clicked.connect(self.process)
        self.captcha_pack = {
            '4235' : 'resources\\cap_1.png',
            '3bc4' : 'resources\\cap_2.png',
            '269e' : 'resources\\cap_3.png'            
        }
        data = random.choice(list(self.captcha_pack.items()))
        self.ui.lab_captcha.setPixmap(QPixmap(data[1]))
        self.ui.lab_captcha.setScaledContents(True)
        self.code = data[0]
        
    def load_img(self): 
        '''
        Смена капчи 
        '''
        data = random.choice(list(self.captcha_pack.items()))
        self.ui.lab_captcha.setPixmap(QPixmap(data[1]))
        self.ui.lab_captcha.setScaledContents(True)
        self.code = data[0]
    
    def process(self): 
        '''
        Процесс решения капчи
        '''
        if (self.ui.lineEdit_code_captcha.text() != ''): 
            if (self.ui.lineEdit_code_captcha.text() == self.code): 
                self.accept()
            else: 
                self.ui.btn_reload_img.setEnabled(False)
                self.ui.btn_request.setEnabled(False)
                self.ui.lineEdit_code_captcha.clear()
                QTimer.singleShot(10000, lambda: self.ui.btn_reload_img.setDisabled(False))
                QTimer.singleShot(10000, lambda: self.ui.btn_request.setDisabled(False))
        
        
            