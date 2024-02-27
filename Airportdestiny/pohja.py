import asetukset
# import resources
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'


example = r'''
     _    _                       _     ____            _   _             
    / \  (_)_ __ _ __   ___  _ __| |_  |  _ \  ___  ___| |_(_)_ __  _   _ 
   / _ \ | | '__| '_ \ / _ \| '__| __| | | | |/ _ \/ __| __| | '_ \| | | |
  / ___ \| | |  | |_) | (_) | |  | |_  | |_| |  __/\__ \ |_| | | | | |_| |
 /_/   \_\_|_|  | .__/ \___/|_|   \__| |____/ \___||___/\__|_|_| |_|\__, |
                |_|                                                 |___/ 
'''
print(example)

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

