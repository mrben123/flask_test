import string
import sys
import mysql.connector

sys.path.append(r'F:\code\flask_test\main\funcs')
from jsontodb import go

sys.path.append(r'F:\code\flask_test\db')
from db_insertdata import insert_data

mysql_connection = mysql.connector.connect(
    user="root",
    password="gloomy528!@#",
    host="localhost",
    database="pythondb"
)
cursor = mysql_connection.cursor()

class Q(object):
    def __init__(self, a=None, b=None) -> None:
        self.a = a
        self.b = b

    def connect_sql(self):
        print(mysql_connection)

    def toCsv(self,url=None):
        print('转换数据')
        go(url)

    def readCsv(self):
        print('读取数据')
        
    def createdb(self,dbName):
        print("创建了新的datebase")

    def create_table(self,sql=string):
        print("start to creat table...")
        cursor.execute(sql)
        mysql_connection.commit()
        print('success to create a table！')

    def goDatabase(self,data=None,table=None,sql=None):
        print('数据入库')
        insert_data(data)


    