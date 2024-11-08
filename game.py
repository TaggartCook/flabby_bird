import pygame
import random

class Game:
    def __init__(self,bird_img,pipe_img,bg_img,ground_img):
        self.bird = pygame.image.load(bird_img).convert_alpha()
        self.bird_rect = self.bird.get_rect(center = (70,180))
        self.pipe = pygame.image.load(pipe_img).convert_alpha()
        self.bg = pygame.image.load(bg_img).convert_alpha()
        self.ground = pygame.image.load(ground_img).convert_alpha()
        self.ground_position = 0
        self.active = True
        self.gravity = 0.05
        self.bird_movement = 0
        self.rotated_bird = pygame.Surface((0,0))

    def resize_images(self):
        self.bird = pygame.transform.scale(self.bird, (51,34))
        self.pipe = pygame.transform.scale(self.pipe, (80,438))
        self.bg = pygame.transform.scale(self.bg, (400,720))
        self.ground = pygame.transform.scale(self.ground, (470,160))
        
    def show_bg(self,screen):
        screen.blit(self.bg, (0,0))

    def show_ground(self,screen):
        screen.blit(self.ground, (self.ground_position,650))

    def move_ground(self):
        self.ground_position -= 1
        self.ground_position %= 45
        self.ground_position -= 45

    def show_bird(self,screen):
        screen.blit(self.rotated_bird ,self.bird_rect)

    def update_bird(self):
        self.bird_movement += self.gravity
        self.rotated_bird = self.rotate_bird()
        self.bird_rect.centery += self.bird_movement

    def rotate_bird(self):
        new_bird = pygame.transform.rotozoom(self.bird, -self.bird_movement * 3, 1)
        return new_bird
    
    def show_pipe(self,screen):
        screen.blit(self.ground,())

    def flap(self):
        self.bird_movement = 0
        self.bird_movement -= 2.5