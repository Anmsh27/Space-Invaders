import pygame
from settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('gfx/001-ghost.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 5

    def update(self):
        if self.rect.right >= SCREEN_WIDTH:
            self.direction.x = -1
            self.rect.y += 48
        elif self.rect.left <= 0:
            self.direction.x = 1
            self.rect.y += 48

        self.rect.x += self.direction.x * self.speed
