import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="BLEJAJO",
    password="BLEJAJO",
    database="flight_game",
    autocommit=True,
)
