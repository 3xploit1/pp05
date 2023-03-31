import sqlite3 


class DataBase(): 
    '''
    Класс взаимодействия с БД 
    '''
    
    def set_connect(self): 
        self.connection = sqlite3.connect('inf_system.db')
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, login TEXT, password TEXT, name TEXT, surname TEXT, role TEXT, PRIMARY KEY (id) )")

    
    def set_auth(self, user_login, user_password):
        '''
        Выполняет запрос на выборку пользователя по логину и паролю 
        Возвращает список записей
        '''
        
        data = self.cur.execute("""
                                SELECT 
                                """) 
    
        return self.cur.fetchone()
    
    def get_data_user(self, ):
        ... 