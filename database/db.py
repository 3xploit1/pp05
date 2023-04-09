import sqlite3 


class DataBase(): 
    '''
    Класс взаимодействия с БД 
    '''        
    
    def set_connect(self): 
        self.connection = sqlite3.connect('database\/blood_service.db')
        self.cur = self.connection.cursor()
    
    def set_auth(self, user_login, user_password):
        '''
        Выполняет запрос на выборку пользователя по логину и паролю 
        Возвращает список записей
        '''
        
        data = self.cur.execute(f"""SELECT login, password, role FROM users" 
                                "WHERE login='{user_login}' and password='{user_password}'""") 

        data = self.cur.fetchone()
        return data
    
    def get_data_user(self, user):
        '''
        Выполняет запрос на выборку пользователя по его логину
        '''
        
        data = self.cur.execute(f"""SELECT name, surname, role, image FROM users"
                                    "WHERE login='{user}'""")
        data = self.cur.fetchone()
        return data

    def add_order(
        self, 
        code,
        surname, 
        name, 
        middle_name, 
        service
    ):
        '''
        Выполняет запрос на добавление в таблицу order
        '''
        # code оповещение 
        self.cur.execute(f"INSERT INTO patient_order (id_order, surname, name, middle_name, service) VALUES ('{code}','{surname}','{name}','{middle_name}','{service}')")
        self.connection.commit()

    def exist_patient(self, surname, name, middle_name) -> bool:  
        data = self.cur.execute(f"SELECT name, surname, middle_name FROM patient WHERE name='{name}' and surname='{surname}' and middle_name='{middle_name}'")
        data = self.cur.fetchone()
        return True if (data != None) and (len(data) == 3) else False
    
    def add_patient(
        self,
        name, 
        surname,
        middle_name,
        bday,
        passport_series, 
        passport_number,
        phone,
        email,
        policy_number,
        type_policy,
        name_company
    ): 
        self.cur.execute(f"""INSERT INTO patient (name, surname, middle_name, bday, passport_series, passport_number, phone, email, policy_number, type_policy, name_company)
                            VALUES ('{name}','{surname}','{middle_name}','{bday}','{passport_series}','{passport_number}','{phone}','{email}','{policy_number}','{type_policy}','{name_company}')
                         """)
        self.connection.commit()