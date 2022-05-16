import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load('gfx/001-bullet.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 25

    def update(self):
        self.rect.y += self.direction.y * self.speed
