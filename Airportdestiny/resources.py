import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="flight_game",
    autocommit=True,
)

cur = connection.cursor()

