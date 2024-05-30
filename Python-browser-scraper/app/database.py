import pyodbc

#db_conn_string="DRIVER={ODBC Driver 17 for SQL Server};SERVER=LOCALHOST;DATABASE=db_name;"
db_conn_string="DRIVER={ODBC Driver 17 for SQL Server};SERVER=tyres.database.windows.net;DATABASE=Tyres_QA;UID=McGladdery;PWD=Iyangatw?ga1"

class Database():

    def __init__(self) -> None:
        try:
            self.conn = pyodbc.connect(db_conn_string, autocommit=True)
        except Exception as e:
            print("--- Could not open connection to db:", e)

    def select(self, sql: str) -> pyodbc.Cursor:
        try:
            self.conn = pyodbc.connect(db_conn_string, autocommit=True)
            cursor = self.conn.cursor()
            data = cursor.execute(sql)       
                 
            return data
        except Exception as e:
            print("--- Error from Database().select:", e)
            raise e

    def execute(self, sql: str) -> None:
        try:
            self.conn = pyodbc.connect(db_conn_string, autocommit=True)
            cursor = self.conn.cursor()
            cursor.execute(sql)             
            
        except Exception as e:
            print("--- Error from Database().execute:", e)
            raise e 
        
    def insert(self,sql: str) -> int:
        try:
            self.conn = pyodbc.connect(db_conn_string, autocommit=True)
            cursor = self.conn.cursor()
            cursor.execute(sql)
            record_id = cursor.execute('SELECT @@IDENTITY AS id;').fetchone()[0]
            
            return(record_id)
        except Exception as e:
            print("--- Error from Database().Insert:", e)
            raise e 
         
    def get_cursor(self):
        try:
            return self.conn.cursor()                                
        except Exception as e:
            print("--- Error from Database().execute:", e)
            raise e 
    
    def __del__(self):
        try:
            self.conn.close()
        except Exception as e:
            print("DATABASE MAIN - DISPOSE", e)
            raise(e)

db = Database()