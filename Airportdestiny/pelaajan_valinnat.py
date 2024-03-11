import random
from Musiikki import musat, kivi_paperi_sakset_musa, lopeta_musa

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'




def kivi_paperi_sakset(pelaaja):
    kivi_paperi_sakset_musa()
    print(f"{pelaaja[0]} olet joutunut kaksinkamppailuun pelissä kivi, paperi, sakset\n"
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
        print("Virheellinen syöte, hävisit!")
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

