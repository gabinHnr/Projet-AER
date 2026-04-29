import pygame

def gerer_mouvement(joueur, keys):
    """
    Étape 1 : Gérer le déplacement horizontal du joueur.
    """
    # comment capter les touches du clavier (get_pressed)
    # ?
    
    dx = 0
    
    # Si la touche gauche est pressée
    if keys[joueur.key_left] and (joueur.corp.x != -joueur.corp.height /2 ):
        dx = -joueur.x_speed
        joueur.direction = -1
        
    # pour aller à droite
    # ?
    
    # on actualise les coordonnées du joueur
    # ?
    
    return dx
