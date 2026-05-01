import pygame

def nettoyer_balles(minition, obstacles):
    """
    Étape 5 : Faire disparaître les balles qui touchent un mur.
    """
    # On utilise [:] pour pouvoir supprimer des éléments de la liste sans erreur
    for bullet in minition[:]:
        for block in obstacles:
            # colision bullet / block
            ?
               ? # (enlever la balle de la liste)
 