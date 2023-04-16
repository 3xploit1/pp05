import configparser
import psycopg2

config = configparser.ConfigParser()
config.read('config\/config.ini')


class DataBase(): 
    '''
    Класс взаимодействия с БД 
    '''        
    
    def set_connect(self): 
        self.conn = psycopg2.connect(
            database=config['database']['dbname'],
            user=config['database']['user'],
            password=config['database']['password'],
            host=config['database']['host'],
            port=config['database']['port']
    )

        self.cur = self.conn.cursor()
    
    
    def set_auth(self, user_login, user_password):
        '''
        Выполняет запрос на выборку пользователя по логину и паролю 
        Возвращает список записей
        '''
        
        data = self.cur.execute(f"""SELECT login, password, type FROM users" 
                                "WHERE login='{user_login}' and password='{user_password}'""") 

        data = self.cur.fetchone()
        return data
    
    def get_data_user(self, user):
        '''
        Выполняет запрос на выборку пользователя по его логину
        '''
        
        data = self.cur.execute(f"""SELECT name FROM users"
                                    "WHERE login='{user}'""")
        data = self.cur.fetchone()
        return data

    def add_order(
        self, 
        id,
        barcode, 
        date, 
        patient, 
        id_services
    ):
        '''
        Выполняет запрос на добавление в таблицу main_order
        '''
 
        self.cur.execute(f"INSERT INTO main_order (id, barcode, date, patient, id_services) VALUES ('{id}','{barcode}','{date}','{patient}','{id_services}')")
        self.conn.commit()

    def exist_patient(self, full, passport_n) -> bool:  
        data = self.cur.execute(f"SELECT full_n, passport_n FROM patients WHERE full_n='{full}' and passport_n='{passport_n}'")
        data = self.cur.fetchone()
        return True if (data != None) and (len(data) == 2) else False
    
    def get_id_patients(self, full):
        data = self.cur.execute(f"SELECT id FROM patients WHERE full_n='{full}'")
        data = self.cur.fetchone()
        return data 
    
    def get_name_company(self): 
        '''
        Запрос на выборку всех наименований страховых компаний
        '''
        data = self.cur.execute(f"SELECT insurance_name FROM insurance_company")
        data = self.cur.fetchall()
        return data
    
    def get_name_service(self): 
        '''
        Запрос на выборку всех названий услуг
        '''
        data = self.cur.execute(f"SELECT service_name FROM services")
        data = self.cur.fetchall()
        return data
    
    def add_patient(
        self,
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
    ): 
        self.cur.execute(f"""INSERT INTO patients (full_n, login, pwd, email, social_sec_number, ein, social_type, phone, passport_s, passport_n, birthdate_timestamp, id_insurance)
                            VALUES ('{full}','{login}','{pwd}','{email}','{social_sec_number}','{ein}','{social_type}','{phone}','{passport_s}','{passport_n}','{birthdate_timestamp}','{id_insurance}')
                         """)
        self.conn.commit()
    
    def get_id_service(self, service): 
        data = self.cur.execute(f"SELECT code FROM services WHERE service_name='{service}'")
        data = self.cur.fetchone()
        return data 
    
    def get_id_company(self, company): 
        data = self.cur.execute(f"SELECT insurance_company.id FROM insurance_company WHERE insurance_name='{company}'")
        data = self.cur.fetchone()
        return data

    def get_name_company_by_id(self, id):
        data = self.cur.execute(f"SELECT insurance_name FROM insurance_company WHERE id='{id}'")
        data = self.cur.fetchone()
        return data
    
    def get_last_code(self): 
        '''
        Возвращает последний id из таблицы main_order
        '''
        data = self.cur.execute(f"SELECT * FROM main_order ORDER BY id DESC LIMIT 1")
        data = self.cur.fetchone()
        return data 
    
    def get_serv_full(self): 
        data = self.cur.execute("select (pa.full_n), (serv.service_name), (serv.price) FROM service_rendered se INNER JOIN patients pa ON (se.user_id) = (pa.id) INNER JOIN services serv ON (serv.code) = (se.service)")
        data = self.cur.fetchall()
        return data

    def count_by_day(self): 
        data = self.cur.execute("SELECT date AS date, COUNT(*) AS users_count FROM main_order GROUP BY date ORDER BY date")
        data = self.cur.fetchall()
        return data

    def all_patients(self): 
        data = self.cur.execute("SELECT * FROM patients")
        data = self.cur.fetchall()
        return data

    def get_patients(self, id): 
        data = self.cur.execute(f"SELECT patients.full_n, login, pwd, email, phone, social_sec_number, ein, social_type, passport_s, passport_n, birthdate_timestamp, id_insurance FROM patients WHERE id='{id}'")
        data = self.cur.fetchone()
        return data

    def up_pateints(
        self,
        id,
        full,
        login,
        pwd,
        social_sec_number,
        ein,
        social_type,
        passport_s,
        passport_n,
        bday,
        id_insurance
    ): 
        self.cur.execute(
            f"UPDATE patients SET full_n='{full}', login='{login}', pwd='{pwd}', social_sec_number='{social_sec_number}', ein='{ein}', social_type='{social_type}', passport_s='{passport_s}', passport_n='{passport_n}', birthdate_timestamp='{bday}', id_insurance='{id_insurance}' WHERE id='{id}'"
        )
        self.conn.commit()
    
    def get_visits(self): 
        data = self.cur.execute(f"SELECT name, lastenter FROM users")
        data = self.cur.fetchall()
        return data