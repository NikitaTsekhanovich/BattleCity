import pygame
from pygame.sprite import Sprite


class Player_tank(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.player_tank_acceleration = ai_settings.player_tank_acceleration
        sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])
        self.image = sprites.subsurface(0, 0, 13*2, 13*2)
        self.image_left = pygame.transform.rotate(self.image, 90)
        self.image_down = pygame.transform.rotate(self.image, 180)
        self.image_right = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.ai_settings.player_tank_pos_x
        self.rect.y = self.ai_settings.player_tank_pos_y
        self.x = float(self.ai_settings.player_tank_pos_x)
        self.y = float(self.ai_settings.player_tank_pos_y)
        self.width_player = 26
        self.height_player = 26
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.moving_look_right = False
        self.moving_look_left = False
        self.moving_look_up = True
        self.moving_look_down = False

    def update(self, blocks, all_tanks, player_tank,
               bonus_attribute, bonus_damage, bonus_lives, bonuses_group):
        self.move_next(blocks)
        self.check_bonuses(bonus_attribute, bonus_damage, bonus_lives, bonuses_group)

    def check_bonuses(self, bonus_attribute, bonus_damage, bonus_lives, bonuses_group):
        for bonus in bonuses_group:
            if bonus_attribute == bonus:
                if bonus.rect.x < self.x + self.width_player <= bonus.rect.x + 32 and \
                        abs(bonus.rect.y - self.y) <= 32 or bonus.rect.x < self.x <= bonus.rect.x + 32 and \
                        abs(bonus.rect.y - self.y) <= 32:
                    bonus.kill()
                    self.ai_settings.player_tank_acceleration += bonus.acceleration
                    self.ai_settings.player_tank_bullet_speed += bonus.bullet_speed
            if bonus_damage == bonus:
                if bonus.rect.x < self.x + self.width_player <= bonus.rect.x + 32 and \
                        abs(bonus.rect.y - self.y) <= 32 or bonus.rect.x < self.x <= bonus.rect.x + 32 and \
                        abs(bonus.rect.y - self.y) <= 32:
                    bonus.kill()
                    self.ai_settings.player_tank_bullet_damage += bonus.bullet_damage
            if bonus_lives == bonus:
                if bonus.rect.x < self.x + self.width_player <= bonus.rect.x + 32 and \
                        abs(bonus.rect.y - self.y) <= 32 or bonus.rect.x < self.x <= bonus.rect.x + 32 and \
                        abs(bonus.rect.y - self.y) <= 32:
                    bonus.kill()
                    self.ai_settings.player_tank_life += bonus.lives

    def move_next(self, blocks):
        if self.moving_right and self.ai_settings.screen_width - self.width_player - 64 != self.rect.x:
            self.moving_look_right = True
            self.moving_look_left = False
            self.moving_look_up = False
            self.moving_look_down = False
            if self.touch_tile_right(blocks):
                self.x += 1 * self.ai_settings.player_tank_acceleration
                self.rect.x = self.x

        elif self.moving_left and self.rect.x != 0:
            self.moving_look_left = True
            self.moving_look_right = False
            self.moving_look_up = False
            self.moving_look_down = False
            if self.touch_tile_left(blocks):
                self.x -= 1 * self.ai_settings.player_tank_acceleration
                self.rect.x = self.x

        elif self.moving_up and self.rect.y != 0:
            self.moving_look_up = True
            self.moving_look_right = False
            self.moving_look_left = False
            self.moving_look_down = False
            if self.touch_tile_up(blocks):
                self.y -= 1 * self.ai_settings.player_tank_acceleration
                self.rect.y = self.y

        elif self.moving_down and self.ai_settings.screen_height - self.height_player != self.rect.y:
            self.moving_look_down = True
            self.moving_look_right = False
            self.moving_look_left = False
            self.moving_look_up = False
            if self.touch_tile_down(blocks):
                self.y += 1 * self.ai_settings.player_tank_acceleration
                self.rect.y = self.y

    def touch_tile_right(self, blocks):
        for block in blocks.mapr:
            if block[0] < self.x + self.width_player <= block[0] + blocks.tile_size and \
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
            if block[1] < self.y <= block[1] + blocks.tile_size and \
                    abs(block[0] - self.x) <= blocks.tile_size:
                if block.type == 4:
                    return True
                return False
        return True

    def touch_tile_down(self, blocks):
        for block in blocks.mapr:
            if block[1] < self.y + self.width_player <= block[1] + blocks.tile_size and \
                    abs(block[0] - self.x) <= blocks.tile_size:
                if block.type == 4:
                    return True
                return False
        return True

    def blitme(self):
        if self.moving_look_left:
            self.screen.blit(self.image_left, self.rect)
        elif self.moving_look_right:
            self.screen.blit(self.image_right, self.rect)
        elif self.moving_look_down:
            self.screen.blit(self.image_down, self.rect)
        elif self.moving_look_up:
            self.screen.blit(self.image, self.rect)