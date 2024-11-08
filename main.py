import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()
game = Game('bird.png','pipe.png','background.png','ground.png')
game.resize_images()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.active:
                game.flap()

    game.show_bg(screen)

    if game.active:
        game.show_bird(screen)
        game.update_bird()

    game.show_ground(screen)
    game.move_ground()
    
    pygame.display.flip()
    clock.tick(120)
