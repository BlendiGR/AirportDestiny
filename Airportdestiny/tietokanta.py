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

def tietokanta_alustus(sql_yhteys):
    cursor = sql_yhteys.cursor()
    sql2 = "drop table if exists game, goal_reached, goal;"
    cursor.execute(sql2)

def satunnaiset_maat(sql_yhteys):

    cursor = sql_yhteys.cursor()
    sql = ("""select airport.name, country.name from airport, country
    where airport.iso_country=country.iso_country 
    and country.continent = 'EU' 
    and type = 'large_airport';""")
    cursor.execute(sql)
    result = cursor.fetchall()
    for airport, country in result:
        if "Azur" in airport:
            sqld = ("delete from airport where airport.ident = 'LFMN'")
            cursor.execute(sqld)
    result = result

    # random.sample varmistaa, että luvut eivät toistu
    pelilauta = []

    satunnainen_luku = random.sample(range(len(result)), 10)
    for num in satunnainen_luku:
        maa = result[num][0]
        pelilauta.append(maa)

    for n in pelilauta:
        return pelilauta


def maiden_välinenpituus(entinen, nykyinen):
    cursor = sql_yhteys.cursor()
    sql = (f"SELECT latitude_deg, longitude_deg FROM airport WHERE name = '{pelilauta[entinen]}'")
    sql2 = (f"SELECT latitude_deg, longitude_deg FROM airport WHERE name = '{pelilauta[nykyinen]}'")
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    matka = geodesic(result[0], result2[0]).kilometers
    return matka

sql_yhteys = yhteys()
pelilauta = satunnaiset_maat(sql_yhteys)

