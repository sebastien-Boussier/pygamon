import pygame

class Joueur(pygame.sprite.Sprite):

    def __init__(self, x,y):
        super().__init__()
        #chargement de l'image joueur
        self.sprite_sheet = pygame.image.load('assets/player.png')
        self.image = self.get_image(0,0)
        self.rect = self.image.get_rect()
        self.image.set_colorkey([0, 0, 0])
        self.position = [x, y]

    def update(self):
        self.rect.topleft = self.position


    def get_image(self, x, y):
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet, (0,0),(x,y,32,32))
        return image

