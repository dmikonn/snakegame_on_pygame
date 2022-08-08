import pygame

def play_sound(dx, dy):
    deadsrc = pygame.mixer.Sound("audio/dead.mp3")
    eatsrc = pygame.mixer.Sound("audio/eat.mp3")
    upsrc = pygame.mixer.Sound("audio/up.mp3")
    leftsrc = pygame.mixer.Sound("audio/left.mp3")
    rightsrc = pygame.mixer.Sound("audio/right.mp3")
    downsrc = pygame.mixer.Sound("audio/down.mp3")

    if dx == 0 and dy == -1:
        pygame.mixer.Sound.play(upsrc)
    if dx == 0 and dy == 1:
        pygame.mixer.Sound.play(downsrc)
    if dx == 1:
        pygame.mixer.Sound.play(leftsrc)
    if dx == -1:
        pygame.mixer.Sound.play(rightsrc)
    if dx == 2:
        pygame.mixer.Sound.play(eatsrc)
    if dx == 3:
        pygame.mixer.Sound.play(deadsrc)

