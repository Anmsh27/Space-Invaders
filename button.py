import pygame
from settings import *

class Button(pygame.sprite.Sprite):
    def __init__(self,size,colour,pos,function,button_text,font_size=64):
        super().__init__()
        self.colour = colour
        self.image = pygame.Surface(size=size)
        self.image.fill(self.colour)
        self.rect = self.image.get_rect(topleft=pos)
        self.button_function = function
        self.button_text = button_text
        self.font_size = font_size

    def clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        is_clicked = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_pos) and is_clicked[0]:
            self.button_function()



    def draw_text(self,colour):
        font = pygame.font.Font(None,self.font_size)
        font_rendered = font.render(self.button_text, True, colour)
        font_rect = font_rendered.get_rect(topleft=self.rect.center)
        display_surf = pygame.display.get_surface()
        font_rect.center = self.rect.center
        display_surf.blit(font_rendered,font_rect)

    def update(self,colour):
        self.clicked()
        self.draw_text(colour)
