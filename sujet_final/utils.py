import pygame
from sys import exit

# Configuration de l'écran, taille en pixel
SCREEN_WIDTH = 920
SCREEN_HEIGHT = 500

def load_img(chemin, size=None):
    img = pygame.image.load(chemin).convert_alpha()
    if size:
        img = pygame.transform.scale(img, size)
    return img
