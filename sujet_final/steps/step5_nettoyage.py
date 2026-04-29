import pygame

def nettoyer_balles(bullets, obstacles):
    """
    Étape 5 : Faire disparaître les balles qui touchent un mur.
    """
    # On utilise [:] pour pouvoir supprimer des éléments de la liste sans erreur
    for bullet in bullets[:]:
        for block in obstacles:
            # colision bullet / block
            ?
               ? # (enlever la balle de la liste)
