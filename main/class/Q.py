import sys

sys.path.append(r'F:\code\flask_test\main\funcs')
from jsontodb import go

class Q(object):
    def __init__(self, a, b) -> None:
        if a == None or b == None:
            print("omething's not right")
            raise ValueError("something's not right")
        else:
            self.a = a
            self.b = b

    def toCsv(self,url):
        print('转换数据')
        go(url)
        
    def createdb(self,dbName):
        print("创建了新的datebase")

    def create_table(self,tableName):
        print("创建了新的table")

    def goDatabase(self,data,table,sql):
        print('数据入库')


    