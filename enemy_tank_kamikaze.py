import pygame
import copy
import random
import game_functions as gf
from pygame.sprite import Sprite


class Kamikaze_tank(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        sprites = pygame.transform.scale(pygame.image.load("images/kamikaze.png"), [24, 24])
        self.image = sprites.subsurface(0, 0, 24, 24)

        self.image_up = self.image
        self.image_left = pygame.transform.rotate(self.image, 90)
        self.image_down = pygame.transform.rotate(self.image, 180)
        self.image_right = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.spawn_position = int(random.uniform(0, 3))
        if self.spawn_position == 0:
            self.rect.x = self.ai_settings.enemy_tank_pos_x
            self.rect.y = self.ai_settings.enemy_tank_pos_y
        elif self.spawn_position == 1:
            self.rect.x = 192
            self.rect.y = self.ai_settings.enemy_tank_pos_y
        else:
            self.rect.x = 384
            self.rect.y = self.ai_settings.enemy_tank_pos_y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.width = 26
        self.height = 26
        self.tank_fire = False
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = True
        self.moving_look_right = True
        self.moving_look_left = False
        self.moving_look_up = False
        self.moving_look_down = True

    def update(self, blocks, all_tanks, player_tank, enemy_tank_kamikaze):
        self.move_next(blocks, player_tank, all_tanks, enemy_tank_kamikaze)

    def move_next(self, blocks, player_tank, all_tanks, enemy_tank_kamikaze):

        if abs(player_tank.rect.x - self.x) > 16 or abs(player_tank.rect.y - self.y) > 16:
            if self.moving_right:
                if self.ai_settings.screen_width - self.width - 64 != self.rect.x and \
                        self.touch_tile_right(blocks):
                    self.moving_look_right = True
                    self.moving_look_left = False
                    self.moving_look_up = False
                    self.moving_look_down = False
                    self.x += self.ai_settings.kamikaze_tank_speed
                    self.rect.x = self.x
                else:
                    self.moving_right = False
                    self.moving_down = True

            if self.moving_down:
                if self.ai_settings.screen_height - self.height != self.rect.y and \
                        self.touch_tile_down(blocks):
                    self.moving_look_down = True
                    self.moving_look_right = False
                    self.moving_look_left = False
                    self.moving_look_up = False
                    self.y += self.ai_settings.kamikaze_tank_speed
                    self.rect.y = self.y
                else:
                    self.moving_down = False
                    self.moving_left = True

            if self.moving_left:
                if self.rect.x != 0 and self.touch_tile_left(blocks):
                    self.moving_look_left = True
                    self.moving_look_right = False
                    self.moving_look_up = False
                    self.moving_look_down = False
                    self.x -= self.ai_settings.kamikaze_tank_speed
                    self.rect.x = self.x
                else:
                    self.moving_left = False
                    if int(random.uniform(0, 2)) == 0:
                        self.moving_up = True
                    else:
                        self.moving_down = True

            if self.moving_up:
                if self.rect.y != 0 and self.touch_tile_up(blocks):
                    self.moving_look_up = True
                    self.moving_look_right = False
                    self.moving_look_left = False
                    self.moving_look_down = False
                    self.y -= self.ai_settings.kamikaze_tank_speed
                    self.rect.y = self.y
                else:
                    self.moving_up = False
                    if int(random.uniform(0, 2)) == 0:
                        self.moving_right = True
                    else:
                        self.moving_left = True
        else:
            self.tank_fire = True
            for tank in all_tanks:
                if tank == player_tank:
                    tank.kill()
                if tank == enemy_tank_kamikaze:
                    tank.kill()

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