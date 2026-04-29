import pygame

def gerer_collision_x(joueur, obstacles, dx):
    """
    Étape 2 : Empêcher le joueur de traverser les murs horizontalement.
    """
    for block in obstacles:
        if joueur.corp.colliderect(block):
            # collision entre coté droit du joueur et coté gauche du muret ...
            if dx > 0:
                joueur.corp.? = block.?
            
            # de même pour l'autre coté
            ?
