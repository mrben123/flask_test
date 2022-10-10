import mysql.connector

mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gloomy528!@#"
)

cursor = mysql_connection.cursor()
cursor.execute("CREATE DATABASE javascripts")