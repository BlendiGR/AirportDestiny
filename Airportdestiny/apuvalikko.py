from lentokoneet import lentokone_esittely, lentokoneet, lentokoneet_esittely_stripped
from tietokanta import pelilauta
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
import sys
#


import sys

# Määritellään ANSI-värikoodit
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m'
RED = '\033[91m'
#Help menu
def help_menu(komento_input, pelaajat):

    if komento_input == "help":
        print(f"""
           {YELLOW}---------------HELP MENU---------------{RESET}
             \n           Tässä on komentoja, joita voit käyttää :\n
        {GREEN}palaa{RESET} - Jatkaaksesi peliä
        {GREEN}positiot{RESET} - Näytä pelaajien tämänhetkiset sijainnit
        {GREEN}lentokoneet{RESET} - Näytä nykyiset lentokoneet ja niiden ominaisuudet
        {GREEN}quit{RESET} - Lopettaa pelin
        """)

        while True:
            try:
                komento = input(f"\n {GREEN}Kirjoita komento: {RESET}")
                if komento == "quit":
                    print("Kiitos, että pelasit!")
                    sys.exit()
                elif komento == "palaa":
                    break
                elif komento == "positiot":
                    for pelaaja in pelaajat:
                        print(f"Pelaajan {BLUE}{pelaaja[0]}{RESET} sijainti: {GREEN} {pelaaja[3]+1}. {pelilauta[pelaaja[3]]}{RESET}")
                elif komento == "lentokoneet":
                        print(f"""
                        1. Sähkölentokone, Hinta 6000, päästöt 0.25kg/km
                        2. Hybridi helikopteri, Hinta 5000, päästöt 0,30kg/km
                        3. Sähköliitokone, Hinta 4000, päästöt 0,35kg/km
                        4. Biodiesel Jet, Hinta 3000, päästöt 0,40kg/km
                        5. Sähköhelikopteri, Hinta 2000, päästöt 0,45kg/km
                        6. Aurinkovoimaraketti, Hinta 1000, päästöt 0,50kg/km
                        """)
                else:
                    print(f"{RED}Tuntematon komento.{RESET}")
            except ValueError:
                print(f"{RED}Tuntematon komento.{RESET}")



