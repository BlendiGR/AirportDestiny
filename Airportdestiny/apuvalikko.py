from lentokoneet import lentokone_esittely, lentokoneet, lentokoneet_esittely_stripped
from resources import pelilauta
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
import sys



import sys

# Määritellään ANSI-värikoodit
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m'
RED = '\033[91m'

def help_menu(komento_input, pelaajat):
    musiikit_pois = False

    if komento_input == "help":
        print(f"{YELLOW}\n---------------HELP MENU---------------{RESET}")
        print("\nTässä on komentoja, joita voit käyttää :\n")
        print(f"{GREEN}palaa{RESET} - Jatkaaksesi peliä")
        print(f"{GREEN}positiot{RESET} - Näytä pelaajien tämänhetkiset sijainnit")
        print(f"{GREEN}lentokoneet{RESET} - Näytä nykyiset lentokoneet ja niiden ominaisuudet")
        print(f"{GREEN}quit{RESET} - Lopettaa pelin")
        print(f"{GREEN}musiikit_pois{RESET} - Sammuttaa musiikit")

        while True:
            try:
                komento = input(f"\n {GREEN}Kirjoita komento: {RESET}")
                if komento == "quit":
                    print("Kiitos, että pelasit!")
                    sys.exit()
                elif komento == "palaa":
                    break
                elif komento == "musiikit_pois":
                    musiikit_pois = True
                    return musiikit_pois
                elif komento == "positiot":
                    for pelaaja in pelaajat:
                        print(f"Pelaajan {pelaaja[0]} sijainti: {GREEN}{pelilauta[pelaaja[3]]}{RESET}")
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
