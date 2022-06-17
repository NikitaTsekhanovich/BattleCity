import pygame
from pygame.sprite import Sprite
import copy


class Fire_predator(Sprite):
    def __init__(self, ai_settings, screen, enemy_tank):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])
        self.image = sprites.subsurface(75 * 2, 74 * 2, 3 * 2, 4 * 2)
        self.image_left = pygame.transform.rotate(self.image, 90)
        self.image_down = pygame.transform.rotate(self.image, 180)
        self.image_right = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.speed = ai_settings.predator_tank_bullet_speed
        self.rect.x = enemy_tank[0][0]
        self.rect.y = enemy_tank[0][1]
        self.enemy_tank_fire_y = float(self.rect.y)
        self.enemy_tank_fire_x = float(self.rect.x)
        self.fire_down_enemy = copy.deepcopy(enemy_tank[1][3])
        self.fire_right_enemy = copy.deepcopy(enemy_tank[1][1])
        self.fire_left_enemy = copy.deepcopy(enemy_tank[1][2])
        self.fire_up_enemy = copy.deepcopy(enemy_tank[1][0])

    def update(self, player_tank, blocks, bullets, enemy_tank, castle_group, all_tanks):
        self.tank_fire(player_tank, blocks, bullets, enemy_tank, castle_group, all_tanks)

    def tank_fire(self, player_tank, blocks, bullets, enemy_tank, castle_group, all_tanks):
        self.delete_bullet(bullets, None)
        if self.fire_down_enemy:
            self.enemy_tank_fire_y += self.speed
            self.rect.y = self.enemy_tank_fire_y
        elif self.fire_right_enemy:
            self.enemy_tank_fire_x += self.speed
            self.rect.x = self.enemy_tank_fire_x
        elif self.fire_left_enemy:
            self.enemy_tank_fire_x -= self.speed
            self.rect.x = self.enemy_tank_fire_x
        elif self.fire_up_enemy:
            self.enemy_tank_fire_y -= self.speed
            self.rect.y = self.enemy_tank_fire_y

        self.check_blocks(blocks, enemy_tank, bullets)
        self.check_player_tank(player_tank, bullets, all_tanks)
        self.check_castle(bullets, castle_group)

    def check_blocks(self, blocks, enemy_tank, bullets):
        for block in blocks.mapr:
            if block.type != 3 and block.type != 4:
                if block[1] <= self.enemy_tank_fire_y <= block[1] + 16 and \
                        abs(block[0] - self.enemy_tank_fire_x) <= 10 and \
                        (enemy_tank.moving_look_right or enemy_tank.moving_look_left):
                    if block.type == 2:
                        self.delete_bullet(bullets, True)
                        break
                    blocks.mapr.pop(blocks.mapr.index(block))
                    self.delete_bullet(bullets, True)
                if block[0] <= self.enemy_tank_fire_x <= block[0] + 16 and \
                        abs(block[1] - self.enemy_tank_fire_y) <= 16 and \
                        (enemy_tank.moving_look_up or enemy_tank.moving_look_down):
                    if block.type == 2:
                        self.delete_bullet(bullets, True)
                        break
                    blocks.mapr.pop(blocks.mapr.index(block))
                    self.delete_bullet(bullets, True)

    def check_player_tank(self, player_tank, bullets, all_tanks):
        for tank in all_tanks:
            if tank == player_tank:
                if abs(tank.rect.x - self.rect.x) <= 26 and \
                        abs(tank.rect.y - self.rect.y) <= 26:
                    tank.kill()
                    self.delete_bullet(bullets, True)

    def check_castle(self, bullets, castle_group):
        for castle in castle_group:
            if castle.y <= self.enemy_tank_fire_y <= castle.y + 32 and \
                    castle.x <= self.enemy_tank_fire_x <= castle.x + 32:
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
        if self.fire_left_enemy:
            self.screen.blit(self.image_left, (self.rect.x + 3, self.rect.y + 10))
        elif self.fire_right_enemy:
            self.screen.blit(self.image_right, (self.rect.x + 13, self.rect.y + 11))
        elif self.fire_down_enemy:
            self.screen.blit(self.image_down, (self.rect.x + 10, self.rect.y + 19))
        elif self.fire_up_enemy:
            self.screen.blit(self.image, (self.rect.x + 10, self.rect.y - 3))