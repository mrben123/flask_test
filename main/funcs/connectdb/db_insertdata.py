import mysql.connector

sql = "INSERT INTO docxs (DocxName, Attribution, Town, Industry, MainProduct, RiskPoints, Product, Area, Productivity) VALUES (%s ,%s, %s ,%s, %s ,%s, %s ,%s, %s )" 


def main(data):
    mysql_connection = mysql.connector.connect(
        user="root",
        password="gloomy528!@#",
        host="localhost",
        database="pythondb"
    )
    cursor = mysql_connection.cursor()

    for d in data:
        cursor.execute(sql,d)



arg_data = {
    'file_name':'乡镇分配试剂',
    'city_and_area':'泰安市泰山区',
    'town':'省庄镇',
    'industry':'种植业',
    'main_product':'主要治理产品',
    'risk_points':'甲拌磷、三氯杀螨醇、氰戊菊酯',
    'product':'韭菜',
    'area':'8000',
    'productivity':'560',
}