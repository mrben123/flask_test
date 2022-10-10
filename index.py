import os
import sys
sys.path.append(r'F:\code\flask_test\main\class')
from Q import Q

q = Q(1,2)

url = './local/trash/docxs'
q.toCsv(url)

# q_table = 'students'
# q_sql = 'insert into %s'%q_table

# q.goDatabase()
# q.create_table()

sql_1 = 'INSERT INTO docxs (DocxName, Attribution, Town, Industry, MainProduct, RiskPoints, Product, Area, Productivity) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);'
# q.connect_sql()