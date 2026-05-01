import pygame
from Utilitaire import load_img, SCREEN_WIDTH, SCREEN_HEIGHT

# On prépare un dictionnaire vide pour les images
IMAGES_DECOR = {}

def charger_images():
    """
    On charge les images seulement apres l'initialisation de pygame
    """
    global IMAGES_DECOR
    IMAGES_DECOR = {
        "sol":       load_img("./Image/ground.png", (SCREEN_WIDTH, 20)),
        "plafond":   load_img("./Image/plafond.png", (SCREEN_WIDTH, 20)),
        "plateforme": load_img("./Image/plateforme1.png", (150, 30)),
        "pierre":    load_img("./Image/satone.png", (50, 50), colorkey=(255, 255, 255)),
        "arbre":     load_img("./Image/tree.png", (100, 150), colorkey=(255, 255, 255)),
        "mur":       load_img("./Image/wall1.png", (40, 120), colorkey=(255, 255, 255))
    }

class Obstacle:
    def __init__(self, x, y, type_decor):
        self.type = type_decor
        self.rect = self.obtenir_rect_initial(x, y)

    def obtenir_rect_initial(self, x, y):
        # On definit les tailles par defaut des collisions avant l'affichage des images
        tailles = {
            "sol": (SCREEN_WIDTH, 20),
            "plafond": (SCREEN_WIDTH, 20),
            "plateforme": (50, 20),
            "pierre": (50, 50),
            "arbre": (100, 150),
            "mur": (40, 120)
        }
        w, h = tailles.get(self.type, (50, 50))
        return pygame.Rect(x, y, w, h)

def generer_niveau():
    """
    C'est ici que vous allez pouvoir custom votre niveau !
    """
    # On s'assure que les images sont charges si c'est pas deja fait
    if not IMAGES_DECOR:
        charger_images()

#==================================================================================================#
    # ICI c'est la liste de vos objets dans la map

    # Vous aves le choix des elements, au dessus se trouvent dans `tailles` la liste des images a votre disposition pour creer votre niveau

    liste_objets = [
        Obstacle(0, 480, "sol"),        # sol correspond ici a l'image importe juste au dessus
        Obstacle(0, 0, "plafond"),         # idem pour plafond elle est importee au dessus
    ]
    
    return liste_objets


#==================================================================================================#


def dessiner_niveau(screen, liste_objets):
    for obj in liste_objets:
        image = IMAGES_DECOR.get(obj.type)
        if image:
            screen.blit(image, obj.rect)
        else:
            pygame.draw.rect(screen, (100, 100, 100), obj.rect)
