import pygame
from pygame.locals import *
from sys import exit


from menu import Menu
# Menu("start")


# tout mettre en anglais

#### modification :
#  2 obstacles sol et plafond
# chercher le key           ( keys = pygame.key.get_pressed())
# screen.blitz

# mouvement :
# on le premier if, on met une phrase pour la direction (dx = ....)
# on retie le deuxieme bloc pour aller a gauche
# on retire les direction

# ajouter `joueur.corp.x += dx`

## collistion :
# pour `joueur.corp.?` on met dcp un ?

## saut :
# keys[joueur.key_jump] on met  un ?
# on retire ca joueur.y_speed = -10 ils doivent le trouver

# on retire `joueur.y_speed += 0.5 ` ils vont devoir le trouver

# pour les collisions en y, on retire toutm on lleur dit de reprendre comme au dessus
# on leur indique en rouge qu'ild evrait y avoir un bug ca peut etre utile `joueur.y_speed += 0.5 `


## tirer
# on retire `keys[joueur.key_shoot] and joueur.shoot_cooldown == 0:` ils doivent mettre la touche mais pas le cooldown
# on retire `Bullet(joueur.corp.centerx, joueur.corp.centery, joueur.direction)` on fait reference au player ici pour qu'il trouve le centre
# on enelve ` joueur.shoot_cooldown = 10 ` `if joueur.shoot_cooldown > 0:`` et `joueur.shoot_cooldown -= 1`` le joueur les mettra plius tard
# on enleve `bullet.move()`     
# apres ca le joueur devrait se rednre compte que c'est une pm dcp il va mettre un cooldown



## colsiion munition
# on retire tout
# on leur indique que c'est comme au dessus et il faut regarder le .remove




## collision munition avec player 
# on retire tout
# on leur explique que c'est comme pour les obstaclea mais avec les joueurs, on ajout `vie` aux attributs de la classe Player


# on retire tout partie 7
# on explqiue qu'on peut mettre ds fonctions en dehors de la boucle while
# on laisse `def Dessiner_Vie(joueur, x, y):`
# on explique les argument de `screen.blit()` donc image, x et y
# afficher selon la vie des coeurs vide ou plein

# puis les appeller en bas dans le code

pygame.init()
screen = pygame.display.set_mode((920, 500))
clock = pygame.time.Clock() 


##################################################################
                        ## Partie donne##
class Player:
    def __init__(self, x, y, color, key_left, key_right, key_jump, key_shoot, key_dash, name):
        self.corp = pygame.Rect(x, y, 20, 20)
        self.name = name
        self.color = color
        # a ajouter partie 1
        self.y_speed = 0  
        self.x_speed = 5
        self.key_left = key_left
        self.key_right = key_right
    
        # a ajouter partie 3
        self.key_jump = key_jump
        self.jump_cooldown = 0

        # partie 4 
        self.key_shoot = key_shoot
        self.shoot_cooldown = 0
        self.direction = 1

        # partie 6 
        self.vie = 3


        # on verra / bonus
        self.key_dash = key_dash
        self.max_jumps = 2
        self.dash_cd = 0


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.corp)


class Bullet:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(0, 0, 10, 5)
        self.rect.center = (x, y)
        self.direction = direction
        self.color = (255, 255, 0)  # Jaune

    def move(self):
        self.rect.x += 15 * self.direction

    def draw(self, surface):
        # On dessine le rectangle directement
        pygame.draw.rect(surface, self.color, self.rect)


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


# Nos joueurs
joueur1 = Player(100, 320, (255, 0, 0), K_q, K_d, K_z, K_a, K_x, "Player 1")       
joueur2 = Player(800, 460, (0, 0, 255), K_LEFT, K_RIGHT, K_UP, K_DOWN, K_l, "Player 2") 

joueurs = [joueur1, joueur2]

# emplacement des obstacles
obstacles = [
    pygame.Rect(0, 480, 920, 20),    # Le sol
    pygame.Rect(250, 450, 60, 20),   # Plateforme 1
    pygame.Rect(400, 400, 100, 20)   # Plateforme 2
]

# emplacement des munitions
bullets = []

# gravite et vitesse 
G = 9.87
y_speed = 0

####################################################################################
####################################################################################


# def addition(x, y):
#     return (x+y)

# addition(5, 4) >>> 9


def Dessiner_Vie(joueur, x, y):
    for i in range(3):
        if i < joueur.vie:
            screen.blit(Vie_plein_img, (x + i*35, y))
        else:
            screen.blit(Vie_vide_img, (x + i*35, y))





####################################################################################
############################ A completer par l'etudiant ############################
####################################################################################
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





        
        if keys[joueur.key_left] and (joueur.corp.x != -joueur.corp.height /2 ):
            # pass
######################## A CODER EUX MEME   PARTIE 1    MOUVEMENT X     #######################3
            dx = -joueur.x_speed
            # apres
            joueur.direction = -1

        if keys[joueur.key_right] and (joueur.corp.x != 920 -joueur.corp.height /2 ):
            dx = joueur.x_speed
            # apres
            joueur.direction = 1


###########
        if keys[joueur.key_dash] and joueur.dash_cd == 0:
            dx += joueur.direction * 55
            joueur.dash_cd = 40

        if joueur.dash_cd > 0:
            joueur.dash_cd -= 1
############

#################################################################################
    
        joueur.corp.x += dx


############################# POARTIE 2  COLLIDE  #############################################
        for block in obstacles:
            if joueur.corp.colliderect(block):
                if dx > 0: # si va a droite alors on le met a gauche
                    joueur.corp.right = block.left
                if dx < 0: # si va a gauche alors on le met a droite
                    joueur.corp.left = block.right
#################################################################################



############################### partie 3  SAUT et Y ###############################
        # on fait ca en deux
        joueur.y_speed += 0.5 
        joueur.corp.y += joueur.y_speed

        

    
        for block in obstacles:
            if joueur.corp.colliderect(block):
                if joueur.y_speed > 0: # si on tombe sur un bloc on le met dessus
                    joueur.corp.bottom = block.top

                elif joueur.y_speed < 0: # si on tape le dessous d'un bloc alors on le met en dessous
                    joueur.corp.top = block.bottom
                
                joueur.y_speed = 0
        




        # fait ca en premier 
        if keys[joueur.key_jump] and joueur.jump_cooldown == 0:
            joueur.jump_cooldown = 15
            joueur.y_speed = -10

        if joueur.jump_cooldown > 0:
            joueur.jump_cooldown -= 1


        # expliquer on fini le moovement dcp on le dessine        
        joueur.draw(screen)

#################################################################################










############################ PARTIE 4 tirer ###############################
        if keys[joueur.key_shoot] and joueur.shoot_cooldown == 0:

            new_bullet = Bullet(joueur.corp.centerx, joueur.corp.centery, joueur.direction)
            bullets.append(new_bullet)

            joueur.shoot_cooldown = 10
        

        if joueur.shoot_cooldown > 0:
            joueur.shoot_cooldown -= 1


        
    for bullet in bullets[:]:
        bullet.move()
        bullet.draw(screen)
        
#########################################################################


############################ PARTIE 5 collision avec obstacle ###############################
        for block in obstacles:
            if bullet.rect.colliderect(block):
                bullets.remove(bullet)



##############################PARTIE 6 perdre une vie############################

    
                
        for joueur in joueurs:
            if bullet.rect.colliderect(joueur.corp):
                # si touche on le degage
                bullets.remove(bullet)
                # on retire  poin de vie
                joueur.vie = joueur.vie - 1
                if joueur.vie == 0:
                    print("tu as perdu", joueur.name)
                    # Menu("end", joueur.name)



#######################333 partie e7 #######################################3
    Dessiner_Vie(joueur1, 20, 20)
    Dessiner_Vie(joueur2, 800, 20)
            


#################################################################################

############################## PARTIE 7 BONUS ############################

    # dash qui est plus haut




#################################################################################


    for block in obstacles:
        if block.width == 920: 
            screen.blit(sol_img, block)
        else:
            img_temp = pygame.transform.scale(obs_img, (block.width, block.height))
            screen.blit(img_temp, block)


    pygame.display.update()