import pygame

def gerer_physique(joueur, obstacles, keys):
    """
    Étape 3 : Gérer la gravité, le saut et les collisions verticales.
    """
    
    # on fait ça en deux
    # comment avoir un effet de gravité
    ?
    # actualiser les coordonnés
    ?

    # on fait ça en trois
    for block in obstacles:
        # colisions sur l'axe Y
        ?

        # attention il y aura surement un probleme si vous ne réinitialisé pas y_speed

    # fait ça en premier 
    if keys[?] and joueur.jump_cooldown == 0:
        joueur.jump_cooldown = 15
        # modifier la valeur de y_speed
        ?

    if joueur.jump_cooldown > 0:
        joueur.jump_cooldown -= 1
