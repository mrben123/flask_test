import mysql.connector

def excuteSql(_sqls,_data,_amount = 'one'):
    mysql_connection = mysql.connector.connect(
        user="root",
        password="gloomy528!@#",
        host="localhost",
        database="qduniversity"
    )

    print('Connect to db successfully with role of root...\n')

    cursor = mysql_connection.cursor()
    if _amount == 'one':
        try:
            cursor.execute(_sqls,_data)
        except:
            raise ValueError("something's not right")

    else :
        try:
            cursor.executemany(_sqls,_data)
        except:
            print('执行多条出错')

    mysql_connection.commit()