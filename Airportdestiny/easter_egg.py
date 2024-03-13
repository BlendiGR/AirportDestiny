import random
from musiikki import *
from varit import *
def kivi_paperi_sakset(pelaaja):
    kivi_paperi_sakset_musa()
    print(f"{BLUE}{pelaaja[0]}{RESET}{YELLOW} olet joutunut kaksinkamppailuun pelissä kivi, paperi, sakset!{RESET}\n"
          f"- Voitto = saat 3x omaisuutesi määrän\n"
          f"- Tasapeli = et menetä mitään\n"
          f"- Häviö = menetät 50% omaisuudestasi.")


    kivi = GREEN+ '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)''' +RESET

    paperi =GREEN+ '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)''' +RESET

    sakset = GREEN+ '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)''' +RESET

    paperi1 = BLUE+ ''' 
            _______
      ____(____   `---
     (______          
    (_______
     (_______
      (__________.---''' +RESET
    kivi1 = BLUE+ ''' 
         _____
       _/__   `---
      (_
     (__
      (__         
       (______.---''' + RESET
    sakset1 = BLUE+ '''
               _______
         ____(____    '---
        (______
        (__________
             (____)
              (___)__.---''' +RESET


    kuvat = [kivi, paperi, sakset]
    kuvat_tietokone = [kivi1, paperi1, sakset1]
    käyttäjä_valinta = int(input("Mikä valintasi? Syötä: (0) = kivi, (1) = paperi (2) = sakset \n"))
    if käyttäjä_valinta >= 3 or käyttäjä_valinta < 0:
        print("Virheellinen syöte! Peli jatkuu....")
    else:
        tietokoneen_valinta = random.randint(0, 2)
        print("Valitsit:")
        print(f"{kuvat[käyttäjä_valinta]} \n        Tietokone valitsi:                 {kuvat_tietokone[tietokoneen_valinta]}")
        if käyttäjä_valinta == 0 and tietokoneen_valinta == 2:
            pelaaja[1] *= 3
            print("Voitit!")
        elif tietokoneen_valinta == 0 and käyttäjä_valinta == 2:
            pelaaja[1] *= 0.5
            print("Hävisit!")
        elif tietokoneen_valinta > käyttäjä_valinta:
            pelaaja[1] *= 0.5
            print("Hävisit!")
        elif käyttäjä_valinta > tietokoneen_valinta:
            pelaaja[1] *= 3
            print("Voitit!")
        elif tietokoneen_valinta == käyttäjä_valinta:
            print("Tasapeli!")
    print(f"Rahatilanne pelaaja {pelaaja[0]}: {GREEN}{pelaaja[1]}{RESET}")
    lopeta_musa()
    musat()

def easter_egg(pelaaja):
    luku = random.randint(1, 30)
    return easter_egg1(pelaaja, luku, kivi_paperi_sakset)

def easter_egg1(pelaaja, luku, kivi_sakset_paperi):
    if luku == 1:
        lopeta_musa()
        rahanippu()
        input(f'{pelaaja[0]}:{BLUE} Löysi 10 000 rahanipun lentokentältä.{RESET}{GREEN} Paina ENTER jatkaaksesi : {RESET}')
        pelaaja[1] += 10000
        print(f'Pelaaja {BLUE}{pelaaja[0]}{RESET} saldo on{GREEN} {pelaaja[1]}{RESET}')
        return lopeta_musa(), musat()
    if luku == 2:
        lopeta_musa()
        kivi_sakset_paperi(pelaaja)
    if luku == 3:
        rahatpois()
        input(f'{BLUE}{pelaaja[0]}. {RED}Osa rahoistasi varastettiin... menetit {GREEN}1000 rahaa.{GREEN} Paina ENTER jatkaaksesi : {RESET}')
        if pelaaja[1] <= 1000:
            print('...Mutta olet valmiiksi niin köyhä niin saat rahasi takaisin')
        else:
            pelaaja[1] -= 1000
        print(f'Pelaaja {pelaaja[0]} saldo on{GREEN} {pelaaja[1]}{RESET}')
        lopeta_musa()
        musat()
