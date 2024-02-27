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
sql = ("""select airport.name from airport, country
where airport.iso_country=country.iso_country 
and country.continent = 'EU' 
and type = 'large_airport';""")

cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(len(result))
