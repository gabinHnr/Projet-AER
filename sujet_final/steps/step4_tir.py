from entities import Bullet

def gerer_tir(joueur, keys, bullets):
    """
    Étape 4 : Créer une balle quand on appuie sur la touche de tir.
    """
    if ? and joueur.shoot_cooldown == 0:

        new_bullet = Bullet(?) # s'aider de la class Bullet dans entities.py
        bullets.append(new_bullet)

        # ça tire rapidement non??
        ?
        
    if joueur.shoot_cooldown > 0:
        joueur.shoot_cooldown -= 1
