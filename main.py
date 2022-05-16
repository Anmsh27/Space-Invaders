import pygame
import random
from sys import exit
from settings import *
from player import Player
from enemy import Enemy
from bullet import Bullet
from button import Button


class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space Invaders")
        icon = pygame.image.load('icon.ico').convert_alpha()
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()

        self.player = pygame.sprite.GroupSingle()
        self.player_sprite = Player(pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 64))
        self.score = 0

        self.max_enemy = MAX_ENEMY
        self.enemy_list = []

        self.bullet = pygame.sprite.GroupSingle()
        self.bullet_fired = False

        self.gui = True

    def run(self):
        self.player.add(self.player_sprite)
        self.bullet.add(Bullet(pos=self.player.sprite.rect.midtop))
        self.create_enemy(self.max_enemy)
        while True:
            self.screen.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.gui:
                        self.bullet_fired = True
                    if event.key == pygame.K_ESCAPE:
                        self.gui = True

            if self.gui:

                #gui
                font = pygame.font.Font(None, 190)
                rendered = font.render("Space Invaders", True, 'lightblue')
                rect = rendered.get_rect(topleft = (0,0))
                rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/4)
                self.screen.blit(rendered,rect)

                play_button = pygame.sprite.GroupSingle()
                play_button.add(Button((300,150),'white',(SCREEN_WIDTH/2,700), self.play_gui_button, "PLAY", 100))
                play_button.sprite.rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 + 100)
                play_button.draw(self.screen)
                play_button.update('black')

            if not self.gui:

                self.player.draw(self.screen)
                self.player.update()

                if not self.bullet_fired:
                    self.bullet.sprite.rect.midtop = self.player.sprite.rect.midtop

                if len(self.enemy_list) < self.max_enemy:
                    self.create_enemy(1)

                for enemy in self.enemy_list:
                    enemy.draw(self.screen)
                    enemy.update()
                    if enemy.sprite.rect.colliderect(self.bullet.sprite.rect):
                        self.bullet.sprite.rect.midtop = self.player.sprite.rect.midtop
                        self.bullet_fired = False
                        self.enemy_list.remove(enemy)
                        self.score += 1
                    if enemy.sprite.rect.colliderect(self.player.sprite.rect):
                        pygame.quit()
                        exit()

                if self.bullet_fired:
                    self.bullet.draw(self.screen)
                    self.bullet.update()
                    if self.bullet.sprite.rect.y < 0:
                        self.bullet_fired = False
                        self.bullet.sprite.rect.midtop = self.player.sprite.rect.midtop

                self.display_score()

            pygame.display.update()
            self.clock.tick(FPS)

    def create_enemy(self, enemy_num):
        for i in range(enemy_num):
            enemy_sprite = Enemy(pos=(random.randrange(0, SCREEN_WIDTH - 48, 48), random.randrange(0, 320, 48)))
            enemy = pygame.sprite.GroupSingle()
            enemy.add(enemy_sprite)
            self.enemy_list.append(enemy)

    def display_score(self):
        display_surf = pygame.display.get_surface()
        font = pygame.font.Font(None, FONT_SIZE)
        rendered = font.render("Your score is " + str(self.score), True, 'white')
        rendered_rect = rendered.get_rect(topleft=(0, 0))
        display_surf.blit(rendered, rendered_rect)

    def play_gui_button(self):
        self.gui = False

if __name__ == '__main__':
    game = Game()
    game.run()
