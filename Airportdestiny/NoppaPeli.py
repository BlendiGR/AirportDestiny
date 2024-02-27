import random
def heittää_noppaa():
    return random.randint(1, 6)

def heittojen_tulostus(pelaajat):
    for pelaaja in pelaajat:
        input(f"Pelaaja {pelaaja['nimi']}, paina Enter heittääksesi noppaa...")
        tulos = heittää_noppaa()
        pelaaja['rahat'] += tulos * 100
        print(f"Pelaaja {pelaaja['nimi']} heitti {tulos}. Hänellä on nyt {pelaaja['rahat']} rahaa.")
    print("Kaikki pelaajat ovat heittäneet noppaa.")

pelaajat = aloitus()
pelaajat_lista = pelaajien_syöttö_listaan()
heittojen_tulostus(pelaajat_lista)