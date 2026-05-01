import pygame
from sys import exit

# Configuration de l'écran, taille en pixel
SCREEN_WIDTH = 920
SCREEN_HEIGHT = 500

def load_img(chemin, size=None, colorkey=None):
    """
    Charge une image et gère la transparence.
    Si colorkey=(255,255,255), le blanc devient transparent.
    """
    img = pygame.image.load(chemin)
    
    # Si on demande de supprimer une couleur spécifique (ex: le blanc)
    if colorkey:
        if colorkey == -1: # -1 veut dire : prend la couleur du premier pixel en haut à gauche
            colorkey = img.get_at((0,0))
        img.set_colorkey(colorkey)
        img = img.convert() # convert() est mieux pour les colorkeys simples
    else:
        img = img.convert_alpha() # convert_alpha() est mieux pour la vraie transparence PNG
        
    if size:
        img = pygame.transform.scale(img, size)
    return img
