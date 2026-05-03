######## ajout des mouvement horizontaux ###########

import pygame
from pygame.locals import *
from sys import exit


from menu import Menu
Menu("start")

pygame.init()
screen = pygame.display.set_mode((920, 500))
clock = pygame.time.Clock() 

# Fonction pour charger les images
def load_img(chemin, size=None):
    img = pygame.image.load(chemin).convert_alpha()
    if size:
        img = pygame.transform.scale(img, size)
    return img

# Nos images dans le jeu
background_img = load_img("./Image/sky.png", (920, 500))
sol_img        = load_img("./Image/ground.png", (920, 20))
plafond_img    = load_img("./Image/plafond.png", (920, 20))
obs_img        = load_img("./Image/plateforme1.png")
Vie_plein_img  = load_img("./Image/Life_points.png", (30, 30))
Vie_vide_img   = load_img("./Image/Life_point_vide.png", (30, 30))

class Player:
    def __init__(self, x, y, couleur, key_gauche, key_droite, nom):
        self.corp = pygame.Rect(x, y, 20, 20)
        self.nom = nom
        self.couleur = couleur
        self.vitesse_verticale = 0  
        self.vitesse_marche = 5
        self.key_gauche = key_gauche
        self.key_droite = key_droite

    def draw(self, surface):
        pygame.draw.rect(surface, self.couleur, self.corp)

# Nos joueurs
joueur1 = Player(100, 460, (255, 0, 0), K_q, K_d, "Player 1")
joueur2 = Player(800, 460, (0, 0, 255), K_LEFT, K_RIGHT, "Player 2")

joueurs = [joueur1, joueur2]

# emplacement des obstacles
obstacles = [
    pygame.Rect(0, 480, 920, 20),    # Le sol
    pygame.Rect(0, 0, 920, 20),    # Le plafond
    pygame.Rect(250, 450, 60, 20),   # Plateforme 1
    pygame.Rect(400, 400, 100, 20)   # Plateforme 2
]

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

        if keys[joueur.key_gauche] and (joueur.corp.x != -joueur.corp.height /2 ):
            dx = -joueur.vitesse_marche

        if keys[joueur.key_droite] and (joueur.corp.x != 920 -joueur.corp.height /2 ):
            dx = joueur.vitesse_marche

        joueur.corp.x += dx

################################ on ajoute #####################################

        for block in obstacles:
            if joueur.corp.colliderect(block):
                if dx > 0:
                    joueur.corp.right = block.left
                if dx < 0:
                    joueur.corp.left = block.right

#################################################################################


    for joueur in joueurs:
        joueur.draw(screen)

    for block in obstacles:
        if block.y == 0: 
            screen.blit(plafond_img, block)
        elif block.y == 480:
            screen.blit(sol_img, block)
        else:
            img_temp = pygame.transform.scale(obs_img, (block.width, block.height))
            screen.blit(img_temp, block)


    pygame.display.update()