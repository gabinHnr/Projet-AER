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
    def __init__(self, x, y, couleur, nom):
        self.corp = pygame.Rect(x, y, 20, 20)
        self.nom = nom
        self.couleur = couleur

    def draw(self, surface):
        pygame.draw.rect(surface, self.couleur, self.corp)

# Nos joueurs
joueur1 = Player(100, 460, (255, 0, 0), "Player 1")       
joueur2 = Player(800, 460, (0, 0, 255), "Player 2") 

joueurs = [joueur1, joueur2]

# emplacement des obstacles
obstacles = [
    pygame.Rect(0, 480, 920, 20),    # Le sol
    pygame.Rect(0, 0, 920, 20),    # Le plafond
]

while True:
    clock.tick(30)
    screen.blit(background_img, (0, 0))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

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