import pygame

class Player:
    def __init__(self, x, y, couleur, keys_config, nom):
        self.corp = pygame.Rect(x, y, 20, 20)
        self.nom = nom
        self.couleur = couleur
        
        # Configuration des touches
        self.key_gauche = keys_config.get('left', 0)
        self.key_droite = keys_config.get('right', 0)


        
        self.key_saut = keys_config.get('jump', 0)
        self.key_tirer = keys_config.get('shoot', 0)
        
        # Statistiques
        self.vitesse_marche = 5
        self.vitesse_verticale = 0
        self.vie = 3
        
        # États
        self.direction = 1 # 1 pour droite, -1 pour gauche
        self.jump_cooldown = 0
        self.shoot_cooldown = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.couleur, self.corp)

class Bullet:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(0, 0, 10, 5)
        self.rect.center = (x, y)
        self.direction = direction
        self.couleur = (255, 255, 0) # Jaune

    def move(self):
        self.rect.x += 15 * self.direction

    def draw(self, surface):
        pygame.draw.rect(surface, self.couleur, self.rect)
