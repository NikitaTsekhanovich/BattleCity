import pygame
from pygame.sprite import Sprite
import copy
import random


class Fire_player(Sprite):
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
        self.speed = ai_settings.player_tank_bullet_speed
        self.rect.x = player_tank.rect.centerx
        self.rect.y = player_tank.rect.top
        self.player_tank_fire_y = float(self.rect.y)
        self.player_tank_fire_x = float(self.rect.x)
        self.fire_down_player = copy.deepcopy(player_tank.moving_look_down)
        self.fire_right_player = copy.deepcopy(player_tank.moving_look_right)
        self.fire_left_player = copy.deepcopy(player_tank.moving_look_left)
        self.fire_up_player = copy.deepcopy(player_tank.moving_look_up)

    def update(self, blocks, bullets, enemy_tank_predator, castle_group, all_tanks,
               bonus_attribute, bonus_damage, bonus_lives, bonuses_group,
               enemy_tank_hulk, player_tank, enemy_tank_kamikaze, enemy_tank_crazy):

        self.player_tank_fire(blocks, bullets, enemy_tank_predator, castle_group, all_tanks,
                              bonus_attribute, bonus_damage, bonus_lives, bonuses_group,
                              enemy_tank_hulk, player_tank, enemy_tank_kamikaze, enemy_tank_crazy)

    def player_tank_fire(self, blocks, bullets, enemy_tank_predator, castle_group, all_tanks,
                         bonus_attribute, bonus_damage, bonus_lives, bonuses_group,
                         enemy_tank_hulk, player_tank, enemy_tank_kamikaze, enemy_tank_crazy):
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

        self.check_blocks(blocks, player_tank, bullets)
        self.check_enemy_tank(enemy_tank_predator, bullets, all_tanks, bonus_attribute, bonus_damage,
                              bonus_lives, bonuses_group, enemy_tank_hulk, enemy_tank_kamikaze, enemy_tank_crazy)
        self.check_castle(bullets, castle_group)

    def check_blocks(self, blocks, player_tank, bullets):
        for block in blocks.mapr:
            if block.type != 3 and block.type != 4:
                if block[1] <= self.player_tank_fire_y <= block[1] + 16 and \
                        abs(block[0] - self.player_tank_fire_x) <= 10 and \
                        (player_tank.moving_look_right or player_tank.moving_look_left):
                    if block.type == 2 and self.ai_settings.player_tank_bullet_damage != 3:
                        self.delete_bullet(bullets, True)
                        break
                    blocks.mapr.pop(blocks.mapr.index(block))
                    self.delete_bullet(bullets, True)
                if block[0] <= self.player_tank_fire_x <= block[0] + 16 and \
                        abs(block[1] - self.player_tank_fire_y) <= 16 and \
                        (player_tank.moving_look_up or player_tank.moving_look_down):
                    if block.type == 2 and self.ai_settings.player_tank_bullet_damage < 3:
                        self.delete_bullet(bullets, True)
                        break
                    blocks.mapr.pop(blocks.mapr.index(block))
                    self.delete_bullet(bullets, True)

    def check_enemy_tank(self, enemy_tank_predator, bullets, all_tanks, bonus_attribute, bonus_damage,
                         bonus_lives, bonuses_group, enemy_tank_hulk, enemy_tank_kamikaze, enemy_tank_crazy):
        for tank in all_tanks:
            if tank == enemy_tank_predator:
                if abs(tank.rect.x - self.rect.x) <= 26 and \
                        abs(tank.rect.y - self.rect.y) <= 26:
                    if tank.bonus:
                        random_bonus = int(random.uniform(0, 3))
                        if random_bonus == 0:
                            bonuses_group.add(bonus_attribute)
                        elif random_bonus == 1:
                            bonuses_group.add(bonus_lives)
                        else:
                            bonuses_group.add(bonus_damage)
                    tank.kill()
                    self.delete_bullet(bullets, True)
            if tank == enemy_tank_hulk:
                if abs(tank.rect.x - self.rect.x) <= 26 and \
                        abs(tank.rect.y - self.rect.y) <= 26:
                    enemy_tank_hulk.count_tank_lives -= self.ai_settings.player_tank_bullet_damage
                    self.delete_bullet(bullets, True)
                    if enemy_tank_hulk.count_tank_lives <= 0:
                        if tank.bonus:
                            random_bonus = int(random.uniform(0, 3))
                            if random_bonus == 0:
                                bonuses_group.add(bonus_attribute)
                            elif random_bonus == 1:
                                bonuses_group.add(bonus_lives)
                            else:
                                bonuses_group.add(bonus_damage)
                        tank.kill()
            if tank == enemy_tank_kamikaze:
                if abs(tank.rect.x - self.rect.x) <= 26 and \
                        abs(tank.rect.y - self.rect.y) <= 26:
                    self.delete_bullet(bullets, True)
                    tank.kill()
            if tank == enemy_tank_crazy:
                if abs(tank.rect.x - self.rect.x) <= 26 and \
                        abs(tank.rect.y - self.rect.y) <= 26:
                    if tank.bonus:
                        random_bonus = int(random.uniform(0, 3))
                        if random_bonus == 0:
                            bonuses_group.add(bonus_attribute)
                        elif random_bonus == 1:
                            bonuses_group.add(bonus_lives)
                        else:
                            bonuses_group.add(bonus_damage)
                    tank.kill()
                    self.delete_bullet(bullets, True)

    def check_castle(self, bullets, castle_group):
        for castle in castle_group:
            if castle.y <= self.player_tank_fire_y <= castle.y + 32 and \
                    castle.x <= self.player_tank_fire_x <= castle.x + 32:
                self.delete_bullet(bullets, True)
                castle.kill()

    def delete_bullet(self, bullets, hit_tile):
        for bullet in bullets.copy():
            if bullet.rect.x < 0:
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
            self.screen.blit(self.image_left, (self.rect.x - 10, self.rect.y + 10))
        elif self.fire_right_player:
            self.screen.blit(self.image_right, (self.rect.x + 13, self.rect.y + 11))
        elif self.fire_down_player:
            self.screen.blit(self.image_down, (self.rect.x - 3, self.rect.y + 19))
        elif self.fire_up_player:
            self.screen.blit(self.image, (self.rect.x - 3, self.rect.y - 3))