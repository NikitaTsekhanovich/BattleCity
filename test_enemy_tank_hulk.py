import unittest
import pygame
import BattleCity as bs
from settings import Settings
from enemy_tank_hulk import Hulk_tank
from pygame.sprite import Group
from blocks import Block
import math


class TestEnemyTankPredator(unittest.TestCase):
    def test_spawn_random_bonus_tank(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_hulk = Hulk_tank(settings, screen, None, "dont save")

        sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])
        images = [
            sprites.subsurface(32 * 2, 0, 13 * 2, 15 * 2),
            sprites.subsurface(32 * 2, 16 * 2, 13 * 2, 15 * 2)
        ]
        random_bonus_tank = 0
        enemy_tank_hulk.spawn_random_bonus_tank(images, random_bonus_tank)
        self.assertEqual(enemy_tank_hulk.bonus, False)
        self.assertEqual(enemy_tank_hulk.image, images[0])

        random_bonus_tank = 1
        enemy_tank_hulk.spawn_random_bonus_tank(images, random_bonus_tank)
        self.assertEqual(enemy_tank_hulk.bonus, True)
        self.assertEqual(enemy_tank_hulk.image, images[1])

    def test_spawn_position_tank_auto_save(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_hulk = Hulk_tank(settings, screen, None, "dont save")
        file = open("test_save_tanks.txt", "r")
        save_data = [line.strip() for line in file]
        file.close()

        spawn_position = 1
        enemy_tank_hulk.spawn_position_tank(spawn_position, save_data)
        self.assertEqual(enemy_tank_hulk.rect.x, math.floor(float(save_data[5])))
        self.assertEqual(enemy_tank_hulk.rect.y, math.floor(float(save_data[6])))
        self.assertEqual(enemy_tank_hulk.x, float(save_data[5]))
        self.assertEqual(enemy_tank_hulk.y, float(save_data[6]))

    def test_spawn_position_tank_dont_save(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_hulk = Hulk_tank(settings, screen, None, "dont save")
        save_data = "dont save"

        spawn_position = 0
        enemy_tank_hulk.spawn_position_tank(spawn_position, save_data)
        self.assertEqual(enemy_tank_hulk.rect.x, settings.enemy_tank_pos_x)
        self.assertEqual(enemy_tank_hulk.rect.y, settings.enemy_tank_pos_x)

        spawn_position = 1
        enemy_tank_hulk.spawn_position_tank(spawn_position, save_data)
        self.assertEqual(enemy_tank_hulk.rect.x, 192)
        self.assertEqual(enemy_tank_hulk.rect.y, settings.enemy_tank_pos_x)

        spawn_position = 2
        enemy_tank_hulk.spawn_position_tank(spawn_position, save_data)
        self.assertEqual(enemy_tank_hulk.rect.x, 384)
        self.assertEqual(enemy_tank_hulk.rect.y, settings.enemy_tank_pos_x)

    def test_move_right(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_hulk = Hulk_tank(settings, screen, None, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_hulk.moving_right = True
        spawn_position = 192
        enemy_tank_hulk.x = spawn_position
        enemy_tank_hulk.rect.x = spawn_position
        enemy_tank_hulk.move_right(blocks)
        self.assertEqual(enemy_tank_hulk.x, spawn_position + settings.hulk_tank_speed)
        spawn_position = 390
        enemy_tank_hulk.x = spawn_position
        enemy_tank_hulk.rect.x = spawn_position
        enemy_tank_hulk.move_right(blocks)
        self.assertEqual(enemy_tank_hulk.x, spawn_position)

    def test_move_left(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_hulk = Hulk_tank(settings, screen, None, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_hulk.moving_left = True
        enemy_tank_hulk.moving_up = False
        enemy_tank_hulk.moving_down = False
        enemy_tank_hulk.moving_right = False
        spawn_position = 192
        enemy_tank_hulk.x = spawn_position
        enemy_tank_hulk.rect.x = spawn_position
        enemy_tank_hulk.move_left(blocks)
        self.assertEqual(enemy_tank_hulk.x, spawn_position - settings.hulk_tank_speed)
        spawn_position = 0
        enemy_tank_hulk.x = spawn_position
        enemy_tank_hulk.rect.x = spawn_position
        enemy_tank_hulk.move_left(blocks)
        self.assertEqual(enemy_tank_hulk.x, spawn_position)

    def test_move_up(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_hulk = Hulk_tank(settings, screen, None, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_hulk.moving_left = False
        enemy_tank_hulk.moving_up = True
        enemy_tank_hulk.moving_down = False
        enemy_tank_hulk.moving_right = False
        spawn_position = 1
        enemy_tank_hulk.y = spawn_position
        enemy_tank_hulk.rect.y = spawn_position
        enemy_tank_hulk.move_up(blocks)
        self.assertEqual(enemy_tank_hulk.y, spawn_position - settings.hulk_tank_speed)
        spawn_position = 0
        enemy_tank_hulk.y = spawn_position
        enemy_tank_hulk.rect.y = spawn_position
        enemy_tank_hulk.move_up(blocks)
        self.assertEqual(enemy_tank_hulk.y, spawn_position)

    def test_move_down(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_hulk = Hulk_tank(settings, screen, None, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_hulk.moving_left = False
        enemy_tank_hulk.moving_up = False
        enemy_tank_hulk.moving_down = True
        enemy_tank_hulk.moving_right = False
        spawn_position = 1
        enemy_tank_hulk.y = spawn_position
        enemy_tank_hulk.rect.y = spawn_position
        enemy_tank_hulk.move_down(blocks)
        self.assertEqual(enemy_tank_hulk.y, spawn_position + settings.hulk_tank_speed)
        spawn_position = 390
        enemy_tank_hulk.y = spawn_position
        enemy_tank_hulk.rect.y = spawn_position
        enemy_tank_hulk.move_down(blocks)
        self.assertEqual(enemy_tank_hulk.y, spawn_position)

    def test_touch_tile_right(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_hulk = Hulk_tank(settings, screen, None, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_hulk.x = 198.00999999999493
        enemy_tank_hulk.y = 303.9700000000084
        self.assertEqual(enemy_tank_hulk.touch_tile_right(blocks), False)
        enemy_tank_hulk.x = 133.96000000000117
        enemy_tank_hulk.y = 314.54000000000735
        self.assertEqual(enemy_tank_hulk.touch_tile_right(blocks), True)

    def test_touch_tile_left(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_hulk = Hulk_tank(settings, screen, None, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_hulk.x = 128.99000000000166
        enemy_tank_hulk.y = 303.9700000000084
        self.assertEqual(enemy_tank_hulk.touch_tile_left(blocks), False)
        enemy_tank_hulk.x = 129.06000000000165
        enemy_tank_hulk.y = 316.8500000000071
        self.assertEqual(enemy_tank_hulk.touch_tile_left(blocks), True)

    def test_touch_tile_up(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_hulk = Hulk_tank(settings, screen, None, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_hulk.x = 128.99000000000166
        enemy_tank_hulk.y = 303.9700000000084
        self.assertEqual(enemy_tank_hulk.touch_tile_up(blocks), False)
        enemy_tank_hulk.x = 128.99000000000166
        enemy_tank_hulk.y = 320.0000000000068
        self.assertEqual(enemy_tank_hulk.touch_tile_up(blocks), True)

    def test_touch_tile_down(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_hulk = Hulk_tank(settings, screen, None, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_hulk.x = 190.1699999999957
        enemy_tank_hulk.y = 342.0500000000047
        self.assertEqual(enemy_tank_hulk.touch_tile_down(blocks), True)
        enemy_tank_hulk.x = 128.99000000000166
        enemy_tank_hulk.y = 309.9900000000078
        self.assertEqual(enemy_tank_hulk.touch_tile_down(blocks), True)


if __name__ == '__main__':
    unittest.main()