import unittest
import pygame
import BattleCity as bs
from settings import Settings
from enemy_tank_kamikaze import Kamikaze_tank
from pygame.sprite import Group
from blocks import Block
import math


class TestEnemyTankPredator(unittest.TestCase):
    def test_spawn_position_tank_auto_save(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_kamikaze = Kamikaze_tank(settings, screen, "dont save")
        file = open("test_save_tanks.txt", "r")
        save_data = [line.strip() for line in file]
        file.close()

        spawn_position = 1
        enemy_tank_kamikaze.spawn_position_tank(spawn_position, save_data)
        self.assertEqual(enemy_tank_kamikaze.rect.x, math.floor(float(save_data[7])))
        self.assertEqual(enemy_tank_kamikaze.rect.y, math.floor(float(save_data[8])))
        self.assertEqual(enemy_tank_kamikaze.x, float(save_data[7]))
        self.assertEqual(enemy_tank_kamikaze.y, float(save_data[8]))

    def test_spawn_position_tank_dont_save(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_kamikaze = Kamikaze_tank(settings, screen, "dont save")
        save_data = "dont save"

        spawn_position = 0
        enemy_tank_kamikaze.spawn_position_tank(spawn_position, save_data)
        self.assertEqual(enemy_tank_kamikaze.rect.x, settings.enemy_tank_pos_x)
        self.assertEqual(enemy_tank_kamikaze.rect.y, settings.enemy_tank_pos_x)

        spawn_position = 1
        enemy_tank_kamikaze.spawn_position_tank(spawn_position, save_data)
        self.assertEqual(enemy_tank_kamikaze.rect.x, 192)
        self.assertEqual(enemy_tank_kamikaze.rect.y, settings.enemy_tank_pos_x)

        spawn_position = 2
        enemy_tank_kamikaze.spawn_position_tank(spawn_position, save_data)
        self.assertEqual(enemy_tank_kamikaze.rect.x, 384)
        self.assertEqual(enemy_tank_kamikaze.rect.y, settings.enemy_tank_pos_x)

    def test_move_right(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_kamikaze = Kamikaze_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_kamikaze.moving_right = True
        spawn_position = 192
        enemy_tank_kamikaze.x = spawn_position
        enemy_tank_kamikaze.rect.x = spawn_position
        enemy_tank_kamikaze.move_right(blocks)
        self.assertEqual(enemy_tank_kamikaze.x, spawn_position + settings.kamikaze_tank_speed)
        spawn_position = 390
        enemy_tank_kamikaze.x = spawn_position
        enemy_tank_kamikaze.rect.x = spawn_position
        enemy_tank_kamikaze.move_right(blocks)
        self.assertEqual(enemy_tank_kamikaze.x, spawn_position)

    def test_move_left(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_kamikaze = Kamikaze_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_kamikaze.moving_left = True
        enemy_tank_kamikaze.moving_up = False
        enemy_tank_kamikaze.moving_down = False
        enemy_tank_kamikaze.moving_right = False
        spawn_position = 192
        enemy_tank_kamikaze.x = spawn_position
        enemy_tank_kamikaze.rect.x = spawn_position
        enemy_tank_kamikaze.move_left(blocks)
        self.assertEqual(enemy_tank_kamikaze.x, spawn_position - settings.kamikaze_tank_speed)
        spawn_position = 0
        enemy_tank_kamikaze.x = spawn_position
        enemy_tank_kamikaze.rect.x = spawn_position
        enemy_tank_kamikaze.move_left(blocks)
        self.assertEqual(enemy_tank_kamikaze.x, spawn_position)

    def test_move_up(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_kamikaze = Kamikaze_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_kamikaze.moving_left = False
        enemy_tank_kamikaze.moving_up = True
        enemy_tank_kamikaze.moving_down = False
        enemy_tank_kamikaze.moving_right = False
        spawn_position = 1
        enemy_tank_kamikaze.y = spawn_position
        enemy_tank_kamikaze.rect.y = spawn_position
        enemy_tank_kamikaze.move_up(blocks)
        self.assertEqual(enemy_tank_kamikaze.y, spawn_position - settings.kamikaze_tank_speed)
        spawn_position = 0
        enemy_tank_kamikaze.y = spawn_position
        enemy_tank_kamikaze.rect.y = spawn_position
        enemy_tank_kamikaze.move_up(blocks)
        self.assertEqual(enemy_tank_kamikaze.y, spawn_position)

    def test_move_down(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_kamikaze = Kamikaze_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_kamikaze.moving_left = False
        enemy_tank_kamikaze.moving_up = False
        enemy_tank_kamikaze.moving_down = True
        enemy_tank_kamikaze.moving_right = False
        spawn_position = 1
        enemy_tank_kamikaze.y = spawn_position
        enemy_tank_kamikaze.rect.y = spawn_position
        enemy_tank_kamikaze.move_down(blocks)
        self.assertEqual(enemy_tank_kamikaze.y, spawn_position + settings.kamikaze_tank_speed)
        spawn_position = 390
        enemy_tank_kamikaze.y = spawn_position
        enemy_tank_kamikaze.rect.y = spawn_position
        enemy_tank_kamikaze.move_down(blocks)
        self.assertEqual(enemy_tank_kamikaze.y, spawn_position)

    def test_touch_tile_right(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_kamikaze = Kamikaze_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_kamikaze.x = 198.00999999999493
        enemy_tank_kamikaze.y = 303.9700000000084
        self.assertEqual(enemy_tank_kamikaze.touch_tile_right(blocks), False)
        enemy_tank_kamikaze.x = 133.96000000000117
        enemy_tank_kamikaze.y = 314.54000000000735
        self.assertEqual(enemy_tank_kamikaze.touch_tile_right(blocks), True)

    def test_touch_tile_left(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_kamikaze = Kamikaze_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_kamikaze.x = 128.99000000000166
        enemy_tank_kamikaze.y = 303.9700000000084
        self.assertEqual(enemy_tank_kamikaze.touch_tile_left(blocks), False)
        enemy_tank_kamikaze.x = 129.06000000000165
        enemy_tank_kamikaze.y = 316.8500000000071
        self.assertEqual(enemy_tank_kamikaze.touch_tile_left(blocks), True)

    def test_touch_tile_up(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_kamikaze = Kamikaze_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_kamikaze.x = 128.99000000000166
        enemy_tank_kamikaze.y = 303.9700000000084
        self.assertEqual(enemy_tank_kamikaze.touch_tile_up(blocks), False)
        enemy_tank_kamikaze.x = 128.99000000000166
        enemy_tank_kamikaze.y = 320.0000000000068
        self.assertEqual(enemy_tank_kamikaze.touch_tile_up(blocks), True)

    def test_touch_tile_down(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_kamikaze = Kamikaze_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        enemy_tank_kamikaze.x = 190.1699999999957
        enemy_tank_kamikaze.y = 342.0500000000047
        self.assertEqual(enemy_tank_kamikaze.touch_tile_down(blocks), True)
        enemy_tank_kamikaze.x = 128.99000000000166
        enemy_tank_kamikaze.y = 309.9900000000078
        self.assertEqual(enemy_tank_kamikaze.touch_tile_down(blocks), True)


if __name__ == '__main__':
    unittest.main()