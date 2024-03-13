import pygame
def musat():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("musa.mp3")
    pygame.mixer.music.set_volume(0.10)
    pygame.mixer.music.play()

def lopeta_musa():
    pygame.mixer.music.stop()
def kivi_paperi_sakset_musa():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("kivipaperisakset_musa.mp3")
    pygame.mixer.music.set_volume(0.10)
    pygame.mixer.music.play()

def rahanippu():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("rahanippu.mp3")
    pygame.mixer.music.set_volume(0.10)
    pygame.mixer.music.play()

