import pygame
import sys
print(pygame)
pygame.init()
screen = pygame.display.set_mode((400, 720))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # sys.exit()

    pygame.display.flip()
    clock.tick(120)
    