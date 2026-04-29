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
background_img = load_img("./Image/BG.jpg", (920, 500))
sol_img        = load_img("./Image/ground.png", (920, 20))
obs_img        = load_img("./Image/satone.png")
Vie_plein_img  = load_img("./Image/Life_points.png", (30, 30))
Vie_vide_img   = load_img("./Image/Life_point_vide.png", (30, 30))

class Player:
    def __init__(self, x, y, color, key_left, key_right, key_jump, name):
        self.corp = pygame.Rect(x, y, 20, 20)
        self.name = name
        self.color = color
        self.y_speed = 0  
        self.x_speed = 5
        self.key_left = key_left
        self.key_right = key_right
###################### on ajoute #####################

        self.key_jump = key_jump
        self.jump_cooldown = 0

######################################################

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.corp)

# Nos joueurs
#################### on modifie ######################

joueur1 = Player(100, 460, (255, 0, 0), K_q, K_d, K_z, "Player 1")       
joueur2 = Player(800, 460, (0, 0, 255), K_LEFT, K_RIGHT, K_UP, "Player 2") 

######################################################

joueurs = [joueur1, joueur2]

# emplacement des obstacles
obstacles = [
    pygame.Rect(0, 480, 920, 20),    # Le sol
    pygame.Rect(10, 0, 920, 20),    # Le plafond
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

################################ mouvement en x #####################################

        if keys[joueur.key_left] and (joueur.corp.x != -joueur.corp.height /2 ):
            dx = -joueur.x_speed

        if keys[joueur.key_right] and (joueur.corp.x != 920 -joueur.corp.height /2 ):
            dx = joueur.x_speed

        joueur.corp.x += dx

        for block in obstacles:
            if joueur.corp.colliderect(block):
                if dx > 0:
                    joueur.corp.right = block.left
                if dx < 0:
                    joueur.corp.left = block.right

#####################################################################################

################################### on ajoute #######################################

        # on fait ca en deux
        joueur.y_speed += 0.5 
        joueur.corp.y += joueur.y_speed

        # on fait en trois
        for block in obstacles:
            if joueur.corp.colliderect(block):
                if joueur.y_speed > 0:
                    joueur.corp.bottom = block.top

                elif joueur.y_speed < 0:
                    joueur.corp.top = block.bottom
                
                joueur.y_speed = 0

        # fait ca en premier 
        if keys[joueur.key_jump] and joueur.jump_cooldown == 0:
            joueur.jump_cooldown = 15
            joueur.y_speed = -10

        if joueur.jump_cooldown > 0:
            joueur.jump_cooldown -= 1

#####################################################################################


    for joueur in joueurs:
        joueur.draw(screen)

    for block in obstacles:
        if block.width == 920: 
            screen.blit(sol_img, block)
        else:
            img_temp = pygame.transform.scale(obs_img, (block.width, block.height))
            screen.blit(img_temp, block)


    pygame.display.update()