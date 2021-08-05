import pygame
import pyscroll
import pytmx.util_pygame

from player import Joueur


class Game:

    def __init__(self):
        # creer la fenetre du jeu
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Pygamon - Adventure")

        #charger la carte(tmx)
        tmx_data = pytmx.util_pygame.load_pygame('assets/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        #generer un joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Joueur(player_position.x, player_position.y)


        #dessiner le groupe de calque
        self.groupe = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.groupe.add(self.player)

    def run(self):
        # creer la boucle du jeu
        running = True
        while running:
            self.groupe.update()
            self.groupe.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()