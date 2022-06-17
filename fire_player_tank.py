import pygame
from pygame.sprite import Sprite
import copy


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, player_tank):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])
        self.image = sprites.subsurface(75 * 2, 74 * 2, 3 * 2, 4 * 2)
        self.image_left = pygame.transform.rotate(self.image, 90)
        self.image_down = pygame.transform.rotate(self.image, 180)
        self.image_right = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.speed = ai_settings.bullet_speed
        self.rect.x = player_tank.rect.centerx
        self.rect.y = player_tank.rect.top
        self.player_tank_fire_y = float(self.rect.y)
        self.player_tank_fire_x = float(self.rect.x)
        self.fire_down_player = copy.deepcopy(player_tank.moving_look_down)
        self.fire_right_player = copy.deepcopy(player_tank.moving_look_right)
        self.fire_left_player = copy.deepcopy(player_tank.moving_look_left)
        self.fire_up_player = copy.deepcopy(player_tank.moving_look_up)

    def update(self, player_tank, blocks, bullets, enemy_tanks, castle):
        self.player_tank_fire(player_tank, blocks, bullets, enemy_tanks, castle)

    def player_tank_fire(self, player_tank, blocks, bullets, enemy_tank, castle):
        self.delete_bullet(bullets, None)
        if self.fire_down_player:
            self.player_tank_fire_y += self.speed
            self.rect.y = self.player_tank_fire_y
        elif self.fire_right_player:
            self.player_tank_fire_x += self.speed
            self.rect.x = self.player_tank_fire_x
        elif self.fire_left_player:
            self.player_tank_fire_x -= self.speed
            self.rect.x = self.player_tank_fire_x
        elif self.fire_up_player:
            self.player_tank_fire_y -= self.speed
            self.rect.y = self.player_tank_fire_y

        for block in blocks.mapr:
            if block[1] <= self.player_tank_fire_y <= block[1] + 16 and \
                    abs(block[0] - self.player_tank_fire_x) <= 10 and \
                    (player_tank.moving_look_right or player_tank.moving_look_left):
                blocks.mapr.pop(blocks.mapr.index(block))
                self.delete_bullet(bullets, True)
            if block[0] <= self.player_tank_fire_x <= block[0] + 16 and \
                    abs(block[1] - self.player_tank_fire_y) <= 16 and \
                    (player_tank.moving_look_up or player_tank.moving_look_down):
                blocks.mapr.pop(blocks.mapr.index(block))
                self.delete_bullet(bullets, True)

        if abs(enemy_tank.rect.x - self.rect.x) <= 26 and \
                abs(enemy_tank.rect.y - self.rect.y) <= 26:
            enemy_tank.tank_is_live = False
            self.delete_bullet(bullets, True)

        if abs(castle.x - self.player_tank_fire_x) <= 0.1:
            castle.destroyed = True


    def delete_bullet(self, bullets, hit_tile):
        for bullet in bullets.copy():
            if bullet.rect.x <= 0:
                bullets.remove(bullet)
            elif bullet.rect.y < 0:
                bullets.remove(bullet)
            elif bullet.rect.y >= self.ai_settings.screen_height:
                bullets.remove(bullet)
            elif bullet.rect.x >= self.ai_settings.screen_width:
                bullets.remove(bullet)
            elif hit_tile:
                bullets.remove(bullet)

    def draw_bullet(self):
        if self.fire_left_player:
            self.screen.blit(self.image_left, self.rect)
        elif self.fire_right_player:
            self.screen.blit(self.image_right, self.rect)
        elif self.fire_down_player:
            self.screen.blit(self.image_down, self.rect)
        elif self.fire_up_player:
            self.screen.blit(self.image, self.rect)