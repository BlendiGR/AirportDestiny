import random

def määrä_määrittely():
    # PELAAJAN MÄÄRÄ -----------------------------------------------------
    while True:
        try:
            määrä = int(input("Montako pelaajaa? (Max 4) : "))
            if määrä <= 0 or määrä > 4:
                print("Sallittu pelaajien määrä on 1 - 4.")

            elif määrä > 0 and määrä <=4:
                return min(määrä, 4)
                break


        except ValueError:
            print("Virheellinen syöttö")

def pelaaja_nimi(määrä):
    pelaajat = []
    for i in range(1, määrä + 1):
        name = input(f" Mikä on pelaajan {i} nimi: ")
        pelaajat.append([name, 0])
    return pelaajat

määrä = määrä_määrittely()

pelaaja_nimi(määrä)
def heittää_noppaa():
    return random.randint(1, 6)

#def heittojen_tulostus(pelaajat):
#    for pelaaja in pelaajat:
#        input(f"Pelaaja {pelaaja[0]}, paina Enter heittääksesi noppaa...")
#        tulos = heittää_noppaa()
#        pelaaja[1] += tulos * 1000
#        print(f"Pelaaja {pelaaja['nimi']} heitti {tulos}. Hänellä on nyt {pelaaja[1]} rahaa.")
#    print("Kaikki pelaajat ovat heittäneet noppaa.")

def heittojen_tulostus(pelaajat):
    for pelaaja in pelaajat:
        input(f"Pelaaja {pelaaja[0]}, paina Enter heittääksesi noppaa...")
        tulos = heittää_noppaa()
        pelaaja['rahat'] += tulos * 1000
        print(f"Pelaaja {pelaaja['nimi']} heitti {tulos}. Hänellä on nyt {pelaaja[1]} rahaa.")
    print("Kaikki pelaajat ovat heittäneet noppaa.")

heittojen_tulostus()


