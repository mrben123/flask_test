# Lists of mysql operation 

## Connect to db 
mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gloomy528!@#"
)

## Create database
cursor = mysql_connection.cursor()
cursor.execute("CREATE DATABASE javascripts")

## Create table
_sql = CREATE TABLE docxs(
    DocxID INT PRIMARY KEY,
    DocxName VARCHAR(255),
    Attribution VARCHAR(255),
    Town VARCHAR(255),
    Industry VARCHAR(255),
    MainProduct VARCHAR(255),
    RiskPoints VARCHAR(255),
    Product VARCHAR(255),
    Area VARCHAR(255),
    Productivity VARCHAR(255)
)
cursor.execute(_sql)

## Insert
_sql = "INSERT INTO docxs (DocxName, Attribution, Town, Industry, MainProduct, RiskPoints, Product, Area, Productivity) VALUES (%s ,%s, %s ,%s, %s ,%s, %s ,%s, %s )" 

cursor = mysql_connection.cursor()
cursor.execute(sql,d)
mysql_connection.commit()

## Alter
ALTER TABLE docxs change DocxName XXX VARCHAR(255)

## Select