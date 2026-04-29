import pygame

class Player:
    def __init__(self, x, y, color, keys_config, name):
        self.corp = pygame.Rect(x, y, 20, 20)
        self.name = name
        self.color = color
        
        # Configuration des touches
        self.key_left = keys_config['left']
        self.key_right = keys_config['right']
        self.key_jump = keys_config['jump']
        self.key_shoot = keys_config['shoot']
        
        # Statistiques
        self.x_speed = 5
        self.y_speed = 0
        self.vie = 3
        
        # États
        self.direction = 1 # 1 pour droite, -1 pour gauche
        self.jump_cooldown = 0
        self.shoot_cooldown = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.corp)

class Bullet:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(0, 0, 10, 5)
        self.rect.center = (x, y)
        self.direction = direction
        self.color = (255, 255, 0) # Jaune

    def move(self):
        self.rect.x += 15 * self.direction

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
