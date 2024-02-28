import pygame
def musat():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("musa.mp3")
    pygame.mixer.music.set_volume(0.10)
    pygame.mixer.music.play()

