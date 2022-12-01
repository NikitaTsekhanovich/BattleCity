import pygame
import copy
import random
import game_functions as gf
from pygame.sprite import Sprite


class Predator_tank(Sprite):
    def __init__(self, ai_settings, screen, bullets_tank, save_data):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.bullets = bullets_tank
        sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])
        images = [
            sprites.subsurface(32 * 2, 0, 13 * 2, 15 * 2),
            sprites.subsurface(32 * 2, 16 * 2, 13 * 2, 15 * 2)
        ]

        random_bonus_tank = int(random.uniform(0, 2))
        self.spawn_random_bonus_tank(images, random_bonus_tank)

        self.image_up = self.image
        self.image_left = pygame.transform.rotate(self.image, 90)
        self.image_down = pygame.transform.rotate(self.image, 180)
        self.image_right = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        spawn_position = int(random.uniform(0, 3))
        self.spawn_position_tank(spawn_position, save_data)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.width = 26
        self.height = 26
        self.tank_fire = False
        self.moving_right = True
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.moving_look_right = True
        self.moving_look_left = False
        self.moving_look_up = False
        self.moving_look_down = False

    def spawn_position_tank(self, spawn_position, save_data):
        if save_data[0] == "auto save":
            self.rect.x = float(save_data[3])
            self.rect.y = float(save_data[4])
            self.x = float(save_data[3])
            self.y = float(save_data[4])
        else:
            if spawn_position == 0:
                self.rect.x = self.ai_settings.enemy_tank_pos_x
                self.rect.y = self.ai_settings.enemy_tank_pos_y
            elif spawn_position == 1:
                self.rect.x = 192
                self.rect.y = self.ai_settings.enemy_tank_pos_y
            else:
                self.rect.x = 384
                self.rect.y = self.ai_settings.enemy_tank_pos_y

    def spawn_random_bonus_tank(self, images, random_bonus_tank):
        if random_bonus_tank == 0:
            self.bonus = False
            self.image = images[0]
        else:
            self.bonus = True
            self.image = images[1]

    def update(self, blocks, player_tank):
        self.move_next(blocks, player_tank)

    def move_next(self, blocks, player_tank):
        if abs(player_tank.rect.x - self.x) > 100 or abs(player_tank.rect.y - self.y) > 100:
            self.tank_fire = False
            self.move_right(blocks)
            self.move_down(blocks)
            self.move_left(blocks)
            self.move_up(blocks)
        else:
            self.tank_fire = True
            gf.fire_bullet(self.ai_settings, self.screen,
                           None, None, False, True, self.bullets,
                           ((self.x,
                             self.y),
                            (self.moving_look_up,
                             self.moving_look_right,
                             self.moving_look_left,
                             self.moving_look_down)),
                           None, None, False, None, None, False)

    def move_right(self, blocks):
        if self.moving_right:
            if self.ai_settings.screen_width - self.width - 64 != self.rect.x and \
                    self.touch_tile_right(blocks):
                self.moving_look_right = True
                self.moving_look_left = False
                self.moving_look_up = False
                self.moving_look_down = False
                self.x += self.ai_settings.predator_tank_speed
                self.rect.x = self.x
            else:
                self.moving_right = False
                self.moving_down = True

    def move_down(self, blocks):
        if self.moving_down:
            if self.ai_settings.screen_height - self.height != self.rect.y and \
                    self.touch_tile_down(blocks):
                self.moving_look_down = True
                self.moving_look_right = False
                self.moving_look_left = False
                self.moving_look_up = False
                self.y += self.ai_settings.predator_tank_speed
                self.rect.y = self.y
            else:
                self.moving_down = False
                self.moving_left = True

    def move_left(self, blocks):
        if self.moving_left:
            if self.rect.x != 0 and self.touch_tile_left(blocks):
                self.moving_look_left = True
                self.moving_look_right = False
                self.moving_look_up = False
                self.moving_look_down = False
                self.x -= self.ai_settings.predator_tank_speed
                self.rect.x = self.x
            else:
                self.moving_left = False
                if int(random.uniform(0, 2)) == 0:
                    self.moving_up = True
                else:
                    self.moving_down = True

    def move_up(self, blocks):
        if self.moving_up:
            if self.rect.y != 0 and self.touch_tile_up(blocks):
                self.moving_look_up = True
                self.moving_look_right = False
                self.moving_look_left = False
                self.moving_look_down = False
                self.y -= self.ai_settings.predator_tank_speed
                self.rect.y = self.y
            else:
                self.moving_up = False
                if int(random.uniform(0, 2)) == 0:
                    self.moving_right = True
                else:
                    self.moving_left = True

    def touch_tile_right(self, blocks):
        for block in blocks.mapr:
            if block[0] < self.x + self.width <= block[0] + blocks.tile_size and \
                    abs(block[1] - self.y) <= blocks.tile_size:
                if block.type == 4:
                    return True
                return False
        return True

    def touch_tile_left(self, blocks):
        for block in blocks.mapr:
            if block[0] < self.x <= block[0] + blocks.tile_size + 1 and \
                    abs(block[1] - self.y) <= blocks.tile_size:
                if block.type == 4:
                    return True
                return False
        return True

    def touch_tile_up(self, blocks):
        for block in blocks.mapr:
            if block[1] < self.y - 1 <= block[1] + blocks.tile_size and \
                    abs(block[0] - self.x) <= blocks.tile_size:
                if block.type == 4:
                    return True
                return False
        return True

    def touch_tile_down(self, blocks):
        for block in blocks.mapr:
            if block[1] < self.y + self.width - 10 <= block[1] + blocks.tile_size and \
                    abs(block[0] - self.x) <= blocks.tile_size:
                if block.type == 4:
                    return True
                return False
        return True

    def draw(self):
        if self.moving_look_left:
            self.screen.blit(self.image_left, self.rect)
        elif self.moving_look_right:
            self.screen.blit(self.image_right, self.rect)
        elif self.moving_look_down:
            self.screen.blit(self.image_down, self.rect)
        elif self.moving_look_up:
            self.screen.blit(self.image, self.rect)