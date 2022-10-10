import numpy as np
import pandas as pd
import json

import sys
sys.path.append(r'F:\code\flask_test\class')
sys.path.append(r'F:\code\flask_test\funcs\connectdb')
from Q import Q
import db_insertdata as W

word = Q(1,2)
word.toCsv()

file_1_url = "./local/trash/json/乡镇分配试剂-泰安_1.json"
load_data_1 = None
load_data_2 = None

def main():

    with open(file_1_url,'rb') as f:
        load_data = json.load(f)
        
        load_data_1 = np.array(load_data)
        print('数据形状: ',load_data_1.shape)
        print('数据维度： ',load_data_1.ndim)
        print('数据类型',load_data_1.dtype)
        print('数据长度', load_data_1.size)
        print(pd.DataFrame(load_data).iloc[[100,101,105]])

main()