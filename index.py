import os
import sys
sys.path.append(r'F:\code\flask_test\main\core')
from Q import Q

q = Q(1,2)

url = './local/trash/docxs'
# q.toCsv(url)

url_1 = "./local/trash/json/乡镇分配试剂-泰安_1.json"
# data_3 = q.readCsv(url_1)
# q_table = 'students'
# q_sql = 'insert into %s'%q_table

sql_1 = 'INSERT INTO docxs (DocxName, Attribution, Town, Industry, MainProduct, Product, Area, Productivity, RiskPoints) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);'

data_1 = {
    "file_name": "乡镇分配试剂-泰安", 
    "city_and_area": "泰安市市泰山区!", 
    "town": "省庄镇", 
    "industry": "种植业", 
    "main_product": "主导产业品种 1", 
    "product": "茶叶", 
    "area": "8000", 
    "productivity": "560", 
    "risk_points": "甲拌磷、三氯杀螨醇、氰戊菊酯"
    }

data_2 = [
    ("乡镇分配试剂5","泰安市泰山区拉拉","省庄镇","种植业","主要治理产品","甲拌磷、三氯杀螨醇、氰戊菊酯","韭菜","88000","7500"),
    ("乡镇分配试剂6","泰安市泰山区lala@","王庄","种植业","主要治理产品","甲拌磷、三氯杀螨醇、氰戊菊酯","小麦","81600","70000")
]


data_3 = q.readCsv(url_1)
print(data_3)
# print(data_3)
# print(type(data_3))
# q.goDatabase(sql_1,data_3)
# q.create_table()


# q.connect_sql()