import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="BLEJAJO",
    password="BLEJAJO",
    database="flight_game",
    autocommit=True,
)
cursor = connection.cursor()
sql = f"SELECT * FROM airport WHERE ident ='EFHK'"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
