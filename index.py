import sys
sys.path.append(r'F:\code\flask_test\main\class')
from Q import Q

q = Q(1,2)

url = './local/trash/docxs'
q.toCsv(url)

# q_data = {}
# q_table = 'students'
# q_sql = 'insert into %s'%q_table
# print(q_sql)
# q.goDatabase(q_data,q_table,q_sql)
