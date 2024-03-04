import random

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
    print("Kaikki pelaajat ovat heittäneet noppaa.")
    return pelaajat

def easter_egg(pelaaja):
    luku = random.randint(1, 200)
    return easter_egg1(pelaaja, luku)


def easter_egg1(pelaaja, luku): #Pelaaja löytää rahaa
    if luku == 1:
        input(f'{pelaaja[0]}: Löysi 1000 rahanipun lentokentältä.{GREEN} Paina ENTER jatkaaksesi...{RESET}')
        pelaaja[1] += 1000
        print(f'Pelaaja {pelaaja[0]} saldo on{GREEN} {pelaaja[1]}{RESET}')
        return
    if luku == 2:
        input(f'')