import mysql.connector
import random
from geopy.distance import geodesic

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
    sql = ("""select airport.name, country.name from airport, country
    where airport.iso_country=country.iso_country 
    and country.continent = 'EU' 
    and type = 'large_airport';""")
    cursor.execute(sql)
    result = cursor.fetchall()


    # random.sample varmistaa, että luvut eivät toistu
    pelilauta = []

    satunnainen_luku = random.sample(range(len(result)), 10)
    for num in satunnainen_luku:
        maa = result[num][0]
        pelilauta.append(maa)

    for n in pelilauta:
        return pelilauta


def maiden_välinenpituus():
    cursor = sql_yhteys.cursor()
    sql = (f"SELECT latitude_deg, longitude_deg FROM airport WHERE name = '{pelilauta[pelaajat[0][1]]}'")
    sql2 = (f"SELECT latitude_deg, longitude_deg FROM airport WHERE name = '{pelilauta[pelaajat[0][1]-1]}'")
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    matka = geodesic(result[0], result2[0]).kilometers
    return matka
pelaajat = [["matti", 0, 0, 0], ["pekka", 0, 0, 1], ["joni", 0, 0, 4]]
sql_yhteys = yhteys()
pelilauta = satunnaiset_maat(sql_yhteys)
matka = maiden_välinenpituus()
print(matka)