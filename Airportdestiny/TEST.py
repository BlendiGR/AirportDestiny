RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

pelaajat = [["Blendi", 1000, 500000, 9, 285],["Jarkko", 50000000, 1000, 9, 21]]




def pelinaloittaja():
    maali = []
    kun_kaikki_saapuu = False
    while not kun_kaikki_saapuu:
        for pelaaja in pelaajat:
            if pelaaja[3] == 9:
                maali.append(pelaaja)
                pelaajat.remove(pelaaja)
        if not pelaajat:
            input(f"Kaikki ovat päässeet maaliin!{GREEN} Paina ENTER nähdääksesi pisteet {RESET} \n")
            for voittaja in maali:
                voittaja_lista = []
                nimi, raha, päästöt, paikka, vuorot = voittaja
                pisteet = vuorot / päästöt
                voittaja_lista.append((nimi, pisteet * 10000))
                for nimi, pisteet in voittaja_lista:
                    print(f" - {nimi}, pisteet {GREEN}{pisteet}{RESET} ! ")

            kun_kaikki_saapuu = True

pelinaloittaja()