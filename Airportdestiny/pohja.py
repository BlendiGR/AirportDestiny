# import asetukset
# import resources


example = r'''
     _    _                       _     ____            _   _             
    / \  (_)_ __ _ __   ___  _ __| |_  |  _ \  ___  ___| |_(_)_ __  _   _ 
   / _ \ | | '__| '_ \ / _ \| '__| __| | | | |/ _ \/ __| __| | '_ \| | | |
  / ___ \| | |  | |_) | (_) | |  | |_  | |_| |  __/\__ \ |_| | | | | |_| |
 /_/   \_\_|_|  | .__/ \___/|_|   \__| |____/ \___||___/\__|_|_| |_|\__, |
                |_|                                                 |___/ 
'''
print(example)
def aloitus():
    count = int(input("Montako pelaajaa? (Max 4): "))
    return min(count,4)
def pelaajien_syöttö_listaan():
    pelaajat1 = []
    for i in range(pelaajat):
        nimi = input(f"Anna pelaajan {i+1} nimi: ")
        pelaajat1.append(nimi)
        print(f"Pelaaaja {nimi} syötetty")
    print(pelaajat1)
    return pelaajat1

pelaajat = aloitus()
tulos = pelaajien_syöttö_listaan()
print(f"{pelaajat} pelaajaa valittu")