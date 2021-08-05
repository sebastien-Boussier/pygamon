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

        #deninir une liste pour les collisions

        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))


        #dessiner le groupe de calque
        self.groupe = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.groupe.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
          print("haut")
          self.player.move_above()
        elif pressed[pygame.K_DOWN]:
            print("bas")
            self.player.move_below()
        elif pressed[pygame.K_LEFT]:
            print("gauche")
            self.player.move_left()
        elif pressed[pygame.K_RIGHT]:
            print("droite")
            self.player.move_right()

    def update(self):
        self.groupe.update()
        #verification des collisions
        for sprite in self.groupe.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):

        clock = pygame.time.Clock()

        # creer la boucle du jeu
        running = True
        while running:
            self.player.save_location()
            self.handle_input()
            self.update()
            self.groupe.center(self.player.rect)
            self.groupe.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(60)
        pygame.quit()