import random
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

while pelikerrat < 2:
    print("\nPelikerta", pelikerrat + 1)
    tulos = kivi_sakset_paperi(pelaaja)
    if tulos != "virhe":
        pelikerrat += 1