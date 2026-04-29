import pygame
from sys import exit


def Menu(type, joueur=""):
    if type == "start":
        phrase = "Epi Dash 1v1"
    elif type == "end":
        phrase = "Le " + joueur + " a gagné la partie !"
        
    pygame.init()
    screen = pygame.display.set_mode((920, 500))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 60)

    def draw_text(text, x, y):
        img = font.render(text, True, (255, 255, 255))
        screen.blit(img, (x, y))

    menu = True

    while menu:
        screen.fill((30, 30, 30))

        draw_text(phrase, 100, 100)
        draw_text("1 - Jouer", 100, 250)
        draw_text("2 - Quitter", 100, 320)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    menu = False   # on quitte le menu et on lance la game
                if event.key == pygame.K_2:
                    pygame.quit()
                    exit()

        pygame.display.update()
        clock.tick(30)

    
    print("Le jeu démarre !")
