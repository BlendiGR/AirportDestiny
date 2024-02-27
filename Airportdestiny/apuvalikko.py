RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
import sys

def help_komento():
    print(f"{YELLOW}HELP MENU{RESET}")
    print("Tässä on kommennot mitkä voit käyttää : ")
    print(f"{GREEN}help{RESET} - Näytä tämä menu")
    print(f"{GREEN}näytä positiot{RESET} - Näytä pelaajien nykyiset positiot ja reitti")
    print(f"{GREEN}lentokoneet{RESET} - Näytä nykyiset lentokoneet ja niiden ominaisuudet")
    print(f"{GREEN}quit{RESET} - Lopeta peli")
    print("Kirjoita 'help' saadaksesi apua \n")

def main():
    while True:
        komento = input("Kirjoita komento 'help' nähdääksesi vaihtoehdot").lower()
        if komento == "help":
            help_komento()
        elif komento == "quit":
            print("Kiitos, että pelasit!")
            sys.exit()
        elif komento == "rullaa":
            break
        elif komento == "näytä positiot":
            break
        elif komento == "lentokoneet":
            break

        else:
            print("Tuntematon komento.")

help_komento()