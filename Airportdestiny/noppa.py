import random
from varit import *
#
def heittää_noppaa():
    return random.randint(1, 6)

def heittojen_tulostus(pelaajat):
    for pelaaja in pelaajat:
        input(f"{BLUE}{pelaaja[0]}{RESET}, paina {GREEN}ENTER{RESET} heittääksesi noppaa! : \n ")
        tulos = heittää_noppaa()
        pelaaja[1] += tulos * 1000
        print(f"{BLUE}{pelaaja[0]}{RESET} heitti {tulos}. Saldo on nyt {GREEN}{pelaaja[1]}{RESET} rahaa! \n")
    print(f"{YELLOW}Kaikki pelaajat ovat heittäneet noppaa.{RESET}")
    return pelaajat
