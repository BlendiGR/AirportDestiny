import random

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

heittojen_tulostus(pelaajat)

