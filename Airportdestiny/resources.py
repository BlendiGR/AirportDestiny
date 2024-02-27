import mysql.connector
import random


# Yhteys funktio tekee yhteyden tietokantaan.
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

# satunnaiset maat funktio valitsee tietokannasta 20 EU:n suurta lentokenttää ja tekee niistä listan.
def satunnaiset_maat(sql_yhteys):

# Valitaan tietokannasta kaikki EU:n suuret lentokentät
    cursor = sql_yhteys.cursor()
    sql = ("""select airport.name from airport, country
    where airport.iso_country=country.iso_country 
    and country.continent = 'EU' 
    and type = 'large_airport';""")
    cursor.execute(sql)
    result = cursor.fetchall()


    # tehdään tyhjä lista valituille maille
    pelilauta = []
# random.sample varmistaa, että satunnaisesti valitut luvut eivät toistu
    satunnainen_luku = random.sample(range(len(result)), 10)
# lisätään jokaista lukua vastaava maa tietokannasta listaan
    for num in satunnainen_luku:
        maa = result[num][0]
        pelilauta.append(maa)

# printataan jokainen maa
    for n in pelilauta:
        print(n)
    return pelilauta

#kutsutaan funktiot
sql_yhteys = yhteys()
pelilauta = satunnaiset_maat(sql_yhteys)