import pygame
from pygame.locals import *
from sys import exit
import importlib

#=======================# Importation de nos modules  #==============================#
from utils import SCREEN_WIDTH, SCREEN_HEIGHT, load_img
from entities import Player, Bullet

# Fonction pour charger un module sans faire crasher le jeu
def safe_import(module_path):
    try:
        return importlib.import_module(module_path)
    except Exception:
        return None

# Chargement des etapes
step1 = safe_import("steps.step1_mouvement")
step2 = safe_import("steps.step2_collision_x")
step3 = safe_import("steps.step3_physique")
step4 = safe_import("steps.step4_tir")
step5 = safe_import("steps.step5_nettoyage")
step6 = safe_import("steps.step6_sante")

#====================================================================================#


# Initialisation Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()



#==========================#  Chargement des images  #===============================#

background_img = load_img("./Image/BG.jpg", (SCREEN_WIDTH, SCREEN_HEIGHT))
sol_img = load_img("./Image/ground.png", (SCREEN_WIDTH, 20))
obs_img = load_img("./Image/satone.png")
vie_plein_img = load_img("./Image/Life_points.png", (30, 30))
vie_vide_img  = load_img("./Image/Life_point_vide.png", (30, 30))

#====================================================================================#


# Création des joueurs
joueur1 = Player(100, 460, (255, 0, 0), {'left': K_q, 'right': K_d, 'jump': K_z, 'shoot': K_a}, "Player 1")
joueur2 = Player(800, 460, (0, 0, 255), {'left': K_LEFT, 'right': K_RIGHT, 'jump': K_UP, 'shoot': K_DOWN}, "Player 2")

joueurs = [joueur1, joueur2]
bullets = []




#==========================# Définition des obstacles #=========================#
obstacles = [
    pygame.Rect(0, 480, 920, 20),    # Le sol
    pygame.Rect(10, 0, 920, 20),     # Le plafond
]

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
        dx = 0
        # execution des modules si pas d'erreur
        if step1:
            dx = step1.gerer_mouvement(joueur, keys)
        if step2:
            step2.gerer_collision_x(joueur, obstacles, dx)
        if step3:
            step3.gerer_physique(joueur, obstacles, keys)
        if step4:
            step4.gerer_tir(joueur, keys, bullets)

    if step5:
        step5.nettoyer_balles(bullets, obstacles)
    
    if step6:
        step6.gerer_degats(bullets, joueurs)
        step6.afficher_interface(screen, joueurs, vie_plein_img, vie_vide_img)



    # Vérification si un joueur a perdu
    for joueur in joueurs:
        if joueur.vie <= 0:
            print(f"GAME OVER : Le {joueur.name} a perdu !")
            pygame.quit()
            exit()



    # Affichage

    # joueur
    for joueur in joueurs:
        joueur.draw(screen)

    # munition
    for bullet in bullets:
        bullet.draw(screen)

    # obstacles
    for block in obstacles:
        if block.width == 920: 
            screen.blit(sol_img, block)
        else:
            img_temp = pygame.transform.scale(obs_img, (block.width, block.height))
            screen.blit(img_temp, block)

    pygame.display.update()
