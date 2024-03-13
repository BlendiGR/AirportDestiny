



#LENTOKONEVALINNAT- LASKEE TUOTETUT PÄÄSTÖT JA PÄIVITTÄÄ PELAAJAN RAHA/PÄÄSTÖTILANTEEN/SIJAINNIN.
def lento(pelaaja, pelilauta):
    print('''
    1. Sähkölentokone, Hinta 6000, päästöt 0.25kg/km
    2. Hybridi helikopteri, Hinta 5000, päästöt 0,30kg/km
    3. Sähköliitokone, Hinta 4000, päästöt 0,35kg/km
    4. Biodiesel Jet, Hinta 3000, päästöt 0,40kg/km
    5. Sähköhelikopteri, Hinta 2000, päästöt 0,45kg/km
    6. Aurinkovoimaraketti, Hinta 1000, päästöt 0,50kg/km
    ''')
    oikea_inputti = False
    while not oikea_inputti:
        try:
            lentovalinta = int(input(f"{pelaaja[0]} Valitse lentokone{BLUE} (1 - 6){RESET}{GREEN} (Saldo : {pelaaja[1]}, Päästöt {pelaaja[2]}) : {RESET} "))

            for i in range(len(lentokoneet)):
                if i == lentovalinta - 1:
                    if pelaaja[1] >= lentokoneet[i][0]:
                        pelaaja[1] -= lentokoneet[i][0]
                        print(f"Saldosi nyt {GREEN}{pelaaja[1]}{RESET}.")
                        print(f"Valittu lentokone : {GREEN}{lentokoneet_esittely_stripped[i]}{RESET}")
                        input(f"{GREEN}Paina ENTER jatkaaksesi {RESET}")
                        if pelaaja[3] < len(pelilauta):
                            kilometrit = maiden_välinenpituus(pelaaja[3], pelaaja[3] + 1)
                            print(f"Matkan välinen etäisyys : {GREEN}{round((kilometrit), 0)}{RESET} km")
                            tulos = kilometrit * lentokoneet[i][1]
                            roundedtulos = round(tulos, 0)
                            pelaaja[3] += 1
                            print(f"Olet saapunut lentokenttään{GREEN} {pelilauta[pelaaja[3]]}{RESET}!")
                            print(f"Tuotetut päästöt {GREEN}{roundedtulos}{RESET} kg")
                            komento = input(f"{GREEN}Paina ENTER jatkaaksesi tai kirjoita 'help' nähdääksesi apukomennot {RESET}")
                            if komento == "help":
                                help_menu(komento, pelaajat)
                            pelaaja[2] += roundedtulos

                        oikea_inputti = True


                    else:
                        print(f"Sinulla ei riitä raha valitse toinen lentokone.")

        except ValueError:
            print(f"Väärä valinta. Valitse lentokone {BLUE} (0 - 6){RESET}{GREEN}!")
