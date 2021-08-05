import pygame
import pyscroll


class Game:

    def __init__(self):
        # creer la fenetre du jeu
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Pygamon - Adventure")

        #charger la carte(tmx)
        tmx_data = 

    def run(self):
        # creer la boucle du jeu
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()