import random
def heittää_noppaa():
    return random.randint(1, 6)

def heittojen_tulostus(pelaajat):
    for pelaaja in pelaajat:
        input(f"Pelaaja {pelaaja[0]}, paina Enter heittääksesi noppaa...")
        tulos = heittää_noppaa()
        pelaaja['rahat'] += tulos * 1000
        print(f"Pelaaja {pelaaja['nimi']} heitti {tulos}. Hänellä on nyt {pelaaja[1]} rahaa.")
    print("Kaikki pelaajat ovat heittäneet noppaa.")


heittää_noppaa()
heittojen_tulostus()


