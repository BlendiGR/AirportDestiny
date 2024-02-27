import asetukset
from resources import pelilauta
from lentokoneet import lentokone_esittely
import random
#VÄRIKOODIT ----------------------------------------------------------------------
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
input(f"{BLUE} Tervetuloa Airport Destiny peliin! {RESET} Peliä voi pelata 1 - 4 henkilöä. Peli arpoaa satunnaisesti 10 lentoaseman reitin. \n Vähäisimillä päästöillä kohdemaahan saapunut pelaaja voittaa pelin. {GREEN} (Paina ENTER jatkaaksesi){RESET}")

# PELAAJAN MÄÄRÄ -----------------------------------------------------------------
def määrä_määrittely():
    while True:
        try:
            määrä = int(input("Montako pelaajaa? (Max 4) : "))
            if määrä <= 0 or määrä > 4:
                print("Sallittu pelaajien määrä on 1 - 4.")

            elif määrä > 0 and määrä <=4:
                return min(määrä, 4)
                break


        except ValueError:
            print("Virheellinen syöttö")

#PELAAJIEN NIMET ------------------------------------------------------------------------------
def pelaaja_nimi(määrä):
    pelaajat = []
    nimet = set()
    for i in range(1, määrä + 1):
        while True:
            name = input(f" Mikä on pelaajan {i} nimi: ").strip()
            if name and name not in nimet:
                pelaajat.append([name, 0])
                nimet.add(name)
                break
            else:
                if not name:
                    print("Nimi ei voi olla tyhjä. Yritä uudelleen.")
                else:
                    print("Nimi on jo käytössä. Anna eri nimi.")
    return pelaajat

määrä = määrä_määrittely()
pelaajat = pelaaja_nimi(määrä)



#REITTIEN KERTOMINEN JA LENTOKONE VAIHTOEHDOT --------------------------------------------------------------
print("Reitti on seuraavanlainen : ")

for i, lentoasema in enumerate(pelilauta, start=1):
    print(f"{i} -{GREEN} {lentoasema}{RESET}")

input(f"Aloitus summa on 1000€ ja tavoitteena on lentää {pelilauta[-1]}:iin mahdolisimman vähäisillä päästöillä. {GREEN} Paina ENTER jatkaaksesi{RESET}")
input(f"1 nopan silmäluku vastaa 1000€ ja kalliimat lentokoneet päästävät vähiten. {GREEN} Paina ENTER nähdääksesi vaihtoehdot.{RESET}")
for lentokone in lentokone_esittely:
    print(lentokone)

input(f"{GREEN}Paina ENTER jatkaaksesi{RESET}")

for i in pelaajat:
    pelaajat.append(pelilauta[0])

input(f"Aloitamme pelin {GREEN}{pelilauta[0]}:issa {RESET} ja seuraavana pysäkkinä on {GREEN}{pelilauta[1]}{RESET}. {GREEN}(Paina ENTER jatkaaksesi){RESET}")

print(pelaajat)