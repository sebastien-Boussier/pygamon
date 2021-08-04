import pygame
pygame.init()

# creer la fenetre du jeu
pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygamon - Adventure")

# creer la boucle du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()