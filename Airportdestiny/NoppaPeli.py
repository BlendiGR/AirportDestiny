import random
from pelaajan_valinnat import kivi_sakset_paperi
kivi = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paperi = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

sakset = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [kivi, paperi, sakset]

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
    return easter_egg1(pelaaja, luku, kivi_sakset_paperi)




### KESKEN t: LEEVI:)
def kivi_sakset_paperi(pelaaja):
    print(f"Valitsit kaksinkamppailun pelissä kivi, sakset, paperi\n"
          f"- Voitto = saat 3x omaisuutesi määrän\n"
          f"- Tasapeli = et menetä mitään mutta voit yrittää uudestaan\n"
          f"- Häviö = menetät 50% omaisuudestasi.")

    valinnat = ['kivi', 'sakset', 'paperi']

    while True:
        pelaajan_valinta = input("Valitse kivi, sakset tai paperi: ").lower()
        tietokoneen_valinta = random.choice(valinnat)
        print("Tietokone valitsi:", tietokoneen_valinta)
        if pelaajan_valinta in valinnat:
            if pelaajan_valinta == tietokoneen_valinta:
                print("Tasapeli!")
                break
            elif (pelaajan_valinta == 'kivi' and tietokoneen_valinta == 'sakset') or \
                    (pelaajan_valinta == 'sakset' and tietokoneen_valinta == 'paperi') or \
                    (pelaajan_valinta == 'paperi' and tietokoneen_valinta == 'kivi'):
                print("Voitit!")
                pelaaja[1] *= 3
                break
            else:
                print("Hävisit! Joudut luovuttamaan 50% omaisuudestasi")
                pelaaja[1] *= 0.5

                break
        elif pelaajan_valinta != valinnat:
            print("Virheellinen syöte")


pelikerrat = 0
pelaaja = [0, 1]

while pelikerrat < 2:
    print("\nPelikerta", pelikerrat + 1)
    tulos = kivi_sakset_paperi(pelaaja)
    if tulos != "virhe":
        pelikerrat += 1


def easter_egg1(pelaaja, luku, kivi_sakset_paperi):
    if luku == 1:
        input(f'{pelaaja[0]}: Löysi 1000 rahanipun lentokentältä.{GREEN} Paina ENTER jatkaaksesi...{RESET}')
        pelaaja[1] += 1000
        print(f'Pelaaja {pelaaja[0]} saldo on{GREEN} {pelaaja[1]}{RESET}')
        return
    if luku == 2:
        kivi_sakset_paperi(pelaaja)

print('moi')