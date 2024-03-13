import random
from easter_egg_2 import kivi_paperi_sakset
from musiikki import lopeta_musa, rahanippu, musat


RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
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
                pelaajat.append([name, 0])
                nimet.add(name)
                break
            else:
                if not name:
                    print("Nimi ei voi olla tyhjä. Yritä uudelleen.")
                else:
                    print("Nimi on jo käytössä. Anna eri nimi.")
    return pelaajat
def heittää_noppaa():
    return random.randint(1, 6)

def heittojen_tulostus(pelaajat):
    for pelaaja in pelaajat:
        input(f"{pelaaja[0]}, paina {GREEN}ENTER{RESET} heittääksesi noppaa! : \n ")
        tulos = heittää_noppaa()
        pelaaja[1] += tulos * 1000
        print(f"{pelaaja[0]} heitti {tulos}. Saldo on nyt {GREEN}{pelaaja[1]}{RESET} rahaa! \n")
    print(f"{YELLOW}Kaikki pelaajat ovat heittäneet noppaa.{RESET}")
    return pelaajat

def easter_egg(pelaaja):
    luku = random.randint(1, 100)
    return easter_egg1(pelaaja, luku, kivi_paperi_sakset)

def easter_egg1(pelaaja, luku, kivi_sakset_paperi):
    if luku == 1:
        lopeta_musa()
        rahanippu()
        input(f'{pelaaja[0]}:{BLUE} Löysi 10 000 rahanipun lentokentältä.{RESET}{GREEN} Paina ENTER jatkaaksesi...{RESET}')
        pelaaja[1] += 10000
        print(f'Pelaaja {pelaaja[0]} saldo on{GREEN} {pelaaja[1]}{RESET}')
        return lopeta_musa(), musat()
    if luku == 2:
        lopeta_musa()
        kivi_sakset_paperi(pelaaja)
    if luku == 3:
        input(f'{pelaaja[0]}: Osa rahoistasi varastettiin... menetit {GREEN}1000{RESET} rahaa.{GREEN} Paina ENTER jatkaaksesi...{RESET}')
        if pelaaja[1] <= 1000:
            print('...Mutta olet valmiiksi niin köyhä niin saat rahasi takaisin')
        else:
            pelaaja[1] -= 1000
        print(f'Pelaaja {pelaaja[0]} saldo on{GREEN} {pelaaja[1]}{RESET}')



