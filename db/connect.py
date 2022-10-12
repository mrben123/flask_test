import mysql.connector

mysql_connection = mysql.connector.connect(
        user="root",
        password="gloomy528!@#",
        host="localhost",
        database="pythondb"
    )

print('connect to db with role of root...\n')