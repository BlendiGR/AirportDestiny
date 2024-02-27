import mysql.connector
import random


def yhteys():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="BLEJAJO",
        password="BLEJAJO",
        database="flight_game",
        autocommit=True,
    )
    return connection


def satunnaiset_maat(sql_yhteys):

    cursor = sql_yhteys.cursor()
    sql = ("""select airport.name from airport, country
    where airport.iso_country=country.iso_country 
    and country.continent = 'EU' 
    and type = 'large_airport';""")
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    print(len(result))

    # random.sample varmistaa, että luvut eivät toistu
    pelilauta = []

    satunnainen_luku = random.sample(range(len(result)), 20)
    for num in satunnainen_luku:
        maa = result[num][0]
        pelilauta.append(maa)

    for n in pelilauta:
        print(n)
    return pelilauta

sql_yhteys = yhteys()
pelilauta = satunnaiset_maat(sql_yhteys)