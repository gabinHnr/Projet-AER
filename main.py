import pygame
from pygame.locals import *
from sys import exit
import importlib

#=======================# Importation de nos modules  #==============================#
from Utilitaire import SCREEN_WIDTH, SCREEN_HEIGHT, load_img
from Class import Player, Bullet
from Niveau import generer_niveau, dessiner_niveau

# Fonction pour charger un module sans faire crasher le jeu
def import_securiser(module_path):
    try:
        return importlib.import_module(module_path)
    except Exception:
        return None

# Chargement des etapes
step1 = import_securiser("steps.step1_mouvement")
step2 = import_securiser("steps.step2_collision_x")
step3 = import_securiser("steps.step3_physique")
step4 = import_securiser("steps.step4_tir")
step5 = import_securiser("steps.step5_nettoyage")
step6 = import_securiser("steps.step6_sante")

#====================================================================================#


# Initialisation Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()



#==========================#  Chargement des images  #===============================#

background_img = load_img("./Image/BG.jpg", (SCREEN_WIDTH, SCREEN_HEIGHT))
vie_plein_img = load_img("./Image/Life_points.png", (30, 30), colorkey=(255, 255, 255))
vie_vide_img  = load_img("./Image/Life_point_vide.png", (30, 30), colorkey=(255, 255, 255))

#====================================================================================#

# Création des joueurs
# On les place un peu plus haut pour qu'ils ne soient pas coincés dans le sol
joueur1 = Player(100, 400, (255, 0, 0), {}, "Player 1")
joueur2 = Player(800, 400, (0, 0, 255), {}, "Player 2")

joueurs = [joueur1, joueur2]
minition = []

#==========================# Définition des obstacles #=========================#

# On génère les objets de décor et on extrait leurs rectangles pour la physique
objets_niveau = generer_niveau()
obstacles = [obj.rect for obj in objets_niveau]

#===============================================================================#





# Boucle principale
while True:
    clock.tick(30)
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    for joueur in joueurs:
        deplacement_x = 0
        # execution des modules si pas d'erreur
        if step1:
            deplacement_x = step1.gerer_mouvement(joueur, keys)
        if step2:
            step2.gerer_collision_x(joueur, obstacles, deplacement_x)
        if step3:
            step3.gerer_physique(joueur, obstacles, keys)
        if step4:
            step4.gerer_tir(joueur, keys, minition)

    if step5:
        step5.nettoyer_balles(minition, obstacles)
    
    if step6:
        step6.gerer_degats(minition, joueurs)

    #==========================# AFFICHAGE #==========================#
    
    # 1. Le décor de fond (toujours en premier)
    screen.blit(background_img, (0, 0))

    # 2. Le niveau (sol, plateformes, obstacles)
    dessiner_niveau(screen, objets_niveau)

    # 3. Les joueurs (devant le décor)
    for joueur in joueurs:
        joueur.draw(screen)

    # 4. Les munitions
    for bullet in minition:
        bullet.draw(screen)

    # 5. L'interface (vies) - toujours au dessus de tout
    if step6:
        step6.afficher_interface(screen, joueurs, vie_plein_img, vie_vide_img)

    #=================================================================#

    # Vérification si un joueur a perdu
    for i, joueur in enumerate(joueurs):
        if joueur.vie <= 0:
            from menu import Menu
            Menu("end", joueurs[1-i].nom)
            pygame.quit()
            exit()

    pygame.display.update()
