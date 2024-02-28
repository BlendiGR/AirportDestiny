import asetukset
from Musiikki import musat
from resources import pelilauta
from lentokoneet import lentokone_esittely, lentokoneet, lentokoneet_esittely_stripped
from NoppaPeli import heittää_noppaa, heittojen_tulostus


import random
# VÄRIKOODIT ----------------------------------------------------------------------
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

#INTRO-----------------------------------------------------------------------------
example = BLUE + r'''
     _    _                       _     ____            _   _             
    / \  (_)_ __ _ __   ___  _ __| |_  |  _ \  ___  ___| |_(_)_ __  _   _ 
   / _ \ | | '__| '_ \ / _ \| '__| __| | | | |/ _ \/ __| __| | '_ \| | | |
  / ___ \| | |  | |_) | (_) | |  | |_  | |_| |  __/\__ \ |_| | | | | |_| |
 /_/   \_\_|_|  | .__/ \___/|_|   \__| |____/ \___||___/\__|_|_| |_|\__, |
                |_|                                                 |___/ 
''' + RESET
print(example)
musat()
input(f"{BLUE} Tervetuloa Airport Destiny peliin! {RESET} Peliä voi pelata 1 - 4 henkilöä. Peli arpoaa satunnaisesti 10 lentoaseman reitin. \n Vähäisimillä päästöillä kohdemaahan saapunut pelaaja voittaa pelin. {GREEN} (Paina ENTER jatkaaksesi){RESET}")

# PELAAJAN MÄÄRÄ -----------------------------------------------------------------
def määrä_määrittely():
    while True:
        try:
            määrä = int(input("Montako pelaajaa? (Max 4) : "))
            if määrä <= 0 or määrä > 4:
                print("Sallittu pelaajien määrä on 1 - 4.")

            elif määrä > 0 and määrä <=4: #KATOTAAN ONKO SYÖTTÄMÄ MÄÄRÄ 1 - 4
                return min(määrä, 4)
                break


        except ValueError:
            print("Virheellinen syöttö")

#PELAAJIEN NIMET ---------------------------------------------------------------------------------------------------
def pelaaja_nimi(määrä):
    pelaajat = []
    nimet = set()
    for i in range(1, määrä + 1):
        while True:
            name = input(f" Mikä on pelaajan {i} nimi: ").strip()
            if name and name not in nimet:
                pelaajat.append([name, 0, 0, 0]) #NIMI, RAHA, PÄÄSTÖT, PAIKKA 0 - 10
                nimet.add(name)
                break
            else:
                if not name:
                    print("Nimi ei voi olla tyhjä. Yritä uudelleen.")
                else:
                    print("Nimi on jo käytössä. Anna eri nimi.")
    return pelaajat

#REITTIEN KERTOMINEN JA LENTOKONE VAIHTOEHDOT -----------------------------------------------------------------------
def intro_tekstit():
    print("Reitti on seuraavanlainen : ")
    #PRINTATAAN REITIT NUMEROJÄRJESTYKESSÄ ALKAEN NRO 1 -------------------------------------------------------------------
    for i, lentoasema in enumerate(pelilauta, start=1):
        print(f"{i} -{GREEN} {lentoasema}{RESET}")

    input(f"Aloitus summa on 1000€ ja tavoitteena on lentää {pelilauta[-1]}:iin mahdolisimman vähäisillä päästöillä. {GREEN} Paina ENTER jatkaaksesi{RESET}")
    input(f"1 nopan silmäluku vastaa 1000€ ja kalliimat lentokoneet päästävät vähiten. {GREEN} Paina ENTER nähdääksesi vaihtoehdot.{RESET}")
    for lentokone in lentokone_esittely:
        print(lentokone)

    input(f"{GREEN}Paina ENTER jatkaaksesi{RESET}")
    input(f"Aloitamme pelin {GREEN}{pelilauta[0]}:issa {RESET} ja seuraavana pysäkkinä on {GREEN}{pelilauta[1]}{RESET}. {GREEN}(Paina ENTER jatkaaksesi){RESET}")


määrä = määrä_määrittely()
pelaajat = pelaaja_nimi(määrä)
intro_tekstit()
#ALOITETAAN PELI ----------------------------------------------------------------------------------------------------



tulokset = []
def main(heittää_noppaa):
    heittojen_tulostus(pelaajat)
    for pelaaja in pelaajat:
        vastaus2 = int(input(f"{pelaaja[0]} Haluatko ostaa lennon toiseen maahan {BLUE}(1){RESET}, heittää noppaa uudelleen {BLUE}(2){RESET} vai kompensoida päästöjä? {BLUE}(3){RESET}"))
        if vastaus2 == 1:
            lento(pelaaja, pelilauta)
            print("lenttää")
        elif vastaus2 == 2:
            noppa = heittää_noppaa()
            print(f"pelaajan {pelaaja[0]} silmäluku on {noppa}")
        elif vastaus2 == 3:
            print("kompensoida päästöjä")

def lento(pelaaja, pelilauta):
    print('''
    1. Sähkölentokone, Hinta 6000, päästöt 0.25kg/km
    2. Hybridi helikopteri, Hinta 5000, päästöt 0,30kg/km
    3. Sähköliitokone, Hinta 4000, päästöt 0,35kg/km
    4. Biodiesel Jet, Hinta 3000, päästöt 0,40kg/km
    5. Sähköhelikopteri, Hinta 2000, päästöt 0,45kg/km
    6. Aurinkovoimaraketti, Hinta 1000, päästöt 0,50kg/km
    ''')
    oikea_inputti = False
    while not oikea_inputti:
        try:
            lentovalinta = int(input(f"{pelaaja[0]} Valitse lentokone{BLUE} (0 - 6){RESET}{GREEN} (Saldo : {pelaaja[1]}, Päästöt {pelaaja[2]}) : {RESET} "))

            for i in range(len(lentokoneet)):
                if i == lentovalinta - 1:
                    if pelaaja[1] >= lentokoneet[i][0]:
                        pelaaja[1] -= lentokoneet[i][0]
                        print(f"Saldosi nyt {GREEN}{pelaaja[1]}{RESET}.")
                        print(f"Valittu lentokone : {lentokoneet_esittely_stripped[i]}")
                        if pelaaja[3] < len(pelilauta):
                            pelaaja[3] += 1
                        oikea_inputti = True


                    else:
                        print(f"Sinulla ei riitä raha valitse toinen lentokone.")

        except ValueError:
            print(f"Väärä valinta. Valitse lentokone {BLUE} (0 - 6){RESET}{GREEN}!")



main(heittää_noppaa)
print(tulokset)
print(pelaajat)

