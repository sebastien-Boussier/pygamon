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
        self.speed = 2
        self.images = {
            'down' : self.get_image(0, 0),
            'left' : self.get_image(0, 32),
            'right' : self.get_image(0, 64),
            'up' : self.get_image(0, 96),
        }


    def change_animation(self, animation):
        self.image = self.images[animation]
        self.image.set_colorkey(0, 0, 0)

    def move_right(self):
        self.change_animation("right")
        self.position[0] += self.speed

    def move_left(self):
        self.change_animation("left")
        self.position[0] -= self.speed

    def move_above(self):
        self.change_animation("up")
        self.position[1] += self.speed

    def move_below(self):
        self.change_animation("down")
        self.position[1] -= self.speed

    def update(self):
        self.rect.topleft = self.position


    def get_image(self, x, y):
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet, (0,0),(x,y,32,32))
        return image

