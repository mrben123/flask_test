from calendar import day_abbr
from distutils.log import error
from multiprocessing import connection
from shutil import which
import string
import sys
import mysql.connector
import numpy as np
import pandas as pd
import json

sys.path.append(r'F:\code\flask_test\main\apps')
from jsontodb import go

class Q(object):
    def __init__(self, a=None, b=None) -> None:
        self.a = a
        self.b = b
        
    def _read(self,_file,_type):
        #读取文件
        if(_type == 1):
            pass
        if(_type == 2):
            pass
        if(_type == 3):
            pass
        if(_type == 4):
            pass
        return
    
    def _export(self,_dir,_type):
        #导出文件
        if(_type == 1):
            pass
        if(_type == 2):
            pass
        if(_type == 3):
            pass
        if(_type == 4):
            pass
        return

    def _excute_sql(self,_sql):
        #执行sql语句、入数据库

        #调用一下封装过的db，connect
        #传入sql给db实例
        pass
            
    def connect_sql(self):
        print("准备链接数据库：》》》")
        # self.mysql_connection = mysql.connector.connect(
        #     user="root",
        #     password="gloomy528!@#",
        #     host="localhost",
        #     database="pythondb"
        # )
        # self.cursor = self.mysql_connection.cursor()

    def toCsv(self,url=None):
        # self.connect_sql()
        print('转换数据')
        # go(url)

    def readCsv(self,file_url):
        arr = []
        with open(file_url,'rb') as f:
            load_data = json.load(f)
            print('打印数据:>>>\n')
            f = np.array(load_data)

            
            for item in load_data:
                # print(type(item))
                # print(item)
                temp = []
                for i in item:
                    # print(item[i])
                    temp.append(item[i])

                # print(temp)    
                arr.append(tuple(temp))

            return arr

        load_data_1 = np.array(load_data)
        load_data_2 = pd.DataFrame(load_data)
        
    def createdb(self,dbName):
        print("start to create database...")
        print('You successfully called the database!')

    def create_table(self,sql=string):
        print("start to creat table...")
        print('You successfully create a table！')

    def goDatabase(self,sql=None,data=None,table=None):
        print('数据准备入库。。。')
        mysql_connection = mysql.connector.connect(
            user="root",
            password="gloomy528!@#",
            host="localhost",
            database="pythondb"
        )
        cursor = mysql_connection.cursor()

        for list_data in data:
            try:
                print('in try: ')
                cursor.execute(sql,list_data)
                mysql_connection.commit()
            except Exception as e:
                print(e)

        print('成功入库 - -！')


    