import random

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
        input(f"Pelaaja {pelaaja[0]}, paina Enter heittääksesi noppaa...")
        tulos = heittää_noppaa()
        pelaaja[1] += tulos * 1000
        print(f"Pelaaja {pelaaja[0]} heitti {tulos}. Hänellä on nyt {pelaaja[1]} rahaa.")
    print("Kaikki pelaajat ovat heittäneet noppaa.")
    return pelaajat
määrä = määrä_määrittely()
pelaajat = pelaaja_nimi(määrä)
heittojen_tulostus(pelaajat)

