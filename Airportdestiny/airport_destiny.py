from musiikki import musat
from tietokanta import *
from lentokoneet import *
from noppa import *
from apuvalikko import help_menu
import time
from varit import *
import random
from easter_egg import *


def esittely():
    example = BLUE + r'''
         _    _                       _     ____            _   _             
        / \  (_)_ __ _ __   ___  _ __| |_  |  _ \  ___  ___| |_(_)_ __  _   _ 
       / _ \ | | '__| '_ \ / _ \| '__| __| | | | |/ _ \/ __| __| | '_ \| | | |
      / ___ \| | |  | |_) | (_) | |  | |_  | |_| |  __/\__ \ |_| | | | | |_| |
     /_/   \_\_|_|  | .__/ \___/|_|   \__| |____/ \___||___/\__|_|_| |_|\__, |
                    |_|                                                 |___/ 
    ''' + RESET
    for char in example:
        print(char, end='', flush=True)
        time.sleep(0.003)
    musat()
    input(
        f"\n{BLUE}Tervetuloa Airport Destiny peliin! {RESET}Peliä voi pelata 1 - 4 henkilöä. Peli arpoo satunnaisesti 10 lentoaseman reitin euroopan suurimmista lentokentistä."
        f" \nVähäisimillä päästöillä kohdemaahan saapunut pelaaja voittaa pelin. \nVuorojen määrä vaikuttaa pisteiden lopputulokseen, joten mieti fiksusti kuinka pääset mahdollisimman nopeasti viimeiseen matkakohteesen."
        f" \nEuroopan maissa toimii tämänhetkisesti yhteinen valuutta nimeltään: 'raha'."
        f" {GREEN}\n(Paina ENTER jatkaaksesi)\n{RESET}")

# PELAAJAN MÄÄRÄ ---------------------------------------------------------------------------------------------------
def määrä_määrittely():
    while True:
        try:
            määrä = int(input("\nMontako pelaajaa? (Max 4) : "))
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
            nimi = input(f"Mikä on pelaajan {i} nimi: ").strip()
            if nimi not in nimet:
                pelaajat.append([nimi, 0, 0, 0, 1]) #NIMI, RAHA, PÄÄSTÖT, PAIKKA 0 - 10, VUOROT#################################################################
                nimet.add(nimi)
                break
            else:
                if not nimi:
                    print("Nimi ei voi olla tyhjä. Yritä uudelleen.")
                else:
                    print("Nimi on jo käytössä. Anna eri nimi.")
    return pelaajat

##REITTIEN KERTOMINEN JA LENTOKONE VAIHTOEHDOT ----------------------------------------------------------------------
def intro_tekstit():
    print("\nReitti on seuraavanlainen : ")
    #PRINTATAAN REITIT NUMEROJÄRJESTYKESSÄ ALKAEN NRO 1 -------------------------------------------------------------------
    for i, lentoasema in enumerate(pelilauta, start=1):
        print(f"{i} -{GREEN} {lentoasema}{RESET}")

    input(f"Tavoitteena on lentää {pelilauta[-1]}:iin mahdolisimman vähäisillä päästöillä ja vuoroilla, koska vuorojen määrä vaikuttaa pisteisiin. {GREEN} Paina ENTER jatkaaksesi\n{RESET}")
    input(f"1 nopan silmäluku vastaa 1000€. Mitä kalliimpi lento, sitä ympäristöystävällisempi se on.{GREEN}  Paina ENTER {BLUE}nähdäksesi lentokone vaihtoehdot : {RESET}\n")
    for lentokone in lentokone_esittely:
        for char in lentokone:
            print(char, end='', flush=True)
            time.sleep(0.008)

    input(f"{GREEN}Paina ENTER jatkaaksesi{RESET}\n")
    input(f"Aloitamme pelin {GREEN}{pelilauta[0]}:issa {RESET}, seuraava kohde on: {GREEN}{pelilauta[1]}{RESET}. {GREEN}Paina ENTER jatkaaksesi : \n{RESET}")


# PELIN PÄÄFUNKTIO, JOKA KUTSUU HEITTÄÄ_NOPPAA JA EASTER_EGG FUNKTIOT. SISÄLTÄÄ JOKA VUOROLLA TEHDYT PELAAJIEN VALINNAT.
def main(heittää_noppaa, easter_egg): #MAIN FUNKTIO JOKA PYÖRITTÄÄ PELIÄ---------------------------------------------
    heittojen_tulostus(pelaajat)
    for pelaaja in pelaajat:
        easter_egg(pelaaja)
        while True:
            try:
                vastaus2 = int(input(f"\n{BLUE}{pelaaja[0]}{RESET} {YELLOW}-Saldo: {pelaaja[1]} rahaa-{RESET} Haluatko ostaa lennon toiseen maahan {BLUE}(1){RESET}, heittää noppaa uudelleen {BLUE}(2){RESET} vai kompensoida päästöjä? {BLUE}(3) : {RESET} \n"))
                print(f"            {YELLOW}{pelaaja[4]}. Vuoro!{RESET}")
                if vastaus2 == 1:
                    if pelaaja[1] < 1000:
                        input(f'Pidä huoli, että sinulla on tarpeeksi rahulia lentoihin. Huonosta rahan hallinnasta menetit vuorosi.{GREEN} Paina ENTER  jatkaaksesi : {RESET}\n')
                    elif pelaaja[1] >= 1000:
                        lento(pelaaja, pelilauta)
                elif vastaus2 == 2:
                    noppa = heittää_noppaa()
                    input(f"{BLUE}{pelaaja[0]}{RESET} Heitti silmäluvun {GREEN}{noppa}{RESET}! {GREEN} Paina ENTER jatkaaksesi :  {RESET}\n")
                    pelaaja[1] += noppa * 1000
                    input(f"{BLUE}{pelaaja[0]}{RESET} sai {noppa * 1000} lisää rahaa! Saldo nyt : {pelaaja[1]}. {GREEN} Paina ENTER jatkaaksesi : {RESET}\n")
                elif vastaus2 == 3:
                    if pelaaja[1] < 1000:
                        print(f"{RED} Sinulla ei ole tarpeeksi rahaa.{RESET}")
                    print("Kompensoidaan päästöjä.\n")
                    input(f"Päästöjen kompensointi maksaa 1000 rahaa ja kompensoi 10% niistä. {GREEN} Paina ENTER jatkaaksesi : {RESET} \n")
                    pelaaja[1] -= 1000
                    pelaaja[2] *= 0.9
                    int(pelaaja[2])
                    print(f"{BLUE}{pelaaja[0]}{RESET}{GREEN} Päästöt kompensoitu!\n{RESET}")
                pelaaja[4] += 1
                break

            except ValueError:
                print(f"{RED}Väärä komento!{RESET}")


#LENTOKONEVALINNAT- LASKEE TUOTETUT PÄÄSTÖT JA PÄIVITTÄÄ PELAAJAN RAHA/PÄÄSTÖTILANTEEN/SIJAINNIN.
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
            lentovalinta = int(input(f"{BLUE}{pelaaja[0]}{RESET} Valitse lentokone{BLUE} (1 - 6){RESET}{GREEN} (Saldo : {pelaaja[1]}, Päästöt {pelaaja[2]}) : {RESET} "))

            for i in range(len(lentokoneet)):
                if i == lentovalinta - 1:
                    if pelaaja[1] >= lentokoneet[i][0]:
                        pelaaja[1] -= lentokoneet[i][0]
                        print(f"Saldosi nyt {GREEN}{pelaaja[1]}{RESET}.")
                        print(f"Valittu lentokone : {GREEN}{lentokoneet_esittely_stripped[i]}{RESET}")
                        input(f"{GREEN}Paina ENTER jatkaaksesi : \n {RESET}")
                        if pelaaja[3] < len(pelilauta):
                            kilometrit = maiden_välinenpituus(pelaaja[3], pelaaja[3] + 1)
                            print(f"Matkan välinen etäisyys : {GREEN}{round((kilometrit), 0)}{RESET} km")
                            tulos = kilometrit * lentokoneet[i][1]
                            roundedtulos = round(tulos, 0)
                            pelaaja[3] += 1
                            print(f"Olet saapunut lentokenttään{GREEN}  {pelaaja[3]+1}. {pelilauta[pelaaja[3]]}{RESET}!")
                            print(f"Tuotetut päästöt {GREEN}{roundedtulos}{RESET} kg")
                            komento = input(f"{GREEN}Paina ENTER jatkaaksesi tai kirjoita 'help' nähdääksesi apukomennot : \n {RESET}").lower().strip()
                            if komento == "help":
                                help_menu(komento, pelaajat)
                            pelaaja[2] += roundedtulos

                        oikea_inputti = True


                    else:
                        print(f"Sinulla ei riitä raha valitse toinen lentokone.")

        except ValueError:
            print(f"Väärä valinta. Valitse lentokone {BLUE} (0 - 6){RESET}{GREEN}!")


#FUNKTIO PELIN LOPETTAMISEEN: LASKEE PELAAJAN/PELAAJIEN PISTEET
def pelinaloittaja(main, easter_egg):
    maali = []
    kun_kaikki_saapuu = False
    while not kun_kaikki_saapuu:
        main(heittää_noppaa, easter_egg)
        poistettavat = [pelaaja for pelaaja in pelaajat if pelaaja[3] >= 9]
        maali.extend(poistettavat)
        for pelaaja in poistettavat:
            pelaajat.remove(pelaaja)
        if not pelaajat:
            input(f"Kaikki ovat päässeet maaliin!{GREEN} Paina ENTER nähdääksesi pisteet : {RESET} \n")
            print(f"{YELLOW} Mitä pienempi luku, sitä parempi tulos.{RESET}")
            voittaja_lista = []
            for voittaja in maali:
                nimi, raha, päästöt, paikka, vuorot = voittaja
                pisteet = vuorot / päästöt
                voittaja_lista.append((nimi, pisteet * 10000))
            for nimi, pisteet in voittaja_lista:
                print(f" - {BLUE}Onneksi olkoon pelin läpäisemisestä!! {nimi}{RESET}, pisteet {GREEN}{pisteet:.1f}{RESET} ! ")

            kun_kaikki_saapuu = True


#ALOITETAAN PELI ----------------------------------------------------------------------------------------------------


tietokanta_alustus(sql_yhteys)
esittely()
tulokset = []
määrä = määrä_määrittely()
pelaajat = pelaaja_nimi(määrä)
intro_tekstit()
pelinaloittaja(main,easter_egg)


