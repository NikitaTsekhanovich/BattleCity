import unittest
import pygame
import BattleCity as bs
from settings import Settings
from player_tank import Player_tank
from bonus_attribute import Bonus_attribute
from bonus_damage import Bonus_damage
from bonus_lives import Bonus_lives
from blocks import Block


class TestPlayerTank(unittest.TestCase):
    def test_check_auto_save_data(self):
        file = open("test_save_tanks.txt", "r")
        save_data = [line.strip() for line in file]
        file.close()

        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, save_data)
        self.assertEqual((abs(player_tank.rect.x - float(save_data[1]))) <= 1, True)
        self.assertEqual((abs(player_tank.rect.y - float(save_data[2]))) <= 1, True)
        self.assertEqual((abs(player_tank.x - float(save_data[1]))) <= 1, True)
        self.assertEqual((abs(player_tank.y - float(save_data[2]))) <= 1, True)

    def test_check_dont_save_data(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        self.assertEqual(player_tank.rect.x, settings.player_tank_pos_x)
        self.assertEqual(player_tank.rect.y, settings.player_tank_pos_y)
        self.assertEqual(player_tank.x, settings.player_tank_pos_x)
        self.assertEqual(player_tank.y, settings.player_tank_pos_y)

    def test_take_bonus_attribute(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        bonus_attribute = Bonus_attribute(settings, screen)
        bonus_attribute.rect.x = 146
        bonus_attribute.rect.y = 390
        player_tank.check_bonus_attribute(bonus_attribute)
        self.assertEqual(settings.player_tank_acceleration, 0.07 + 0.01)
        self.assertEqual(settings.player_tank_bullet_speed,  0.1 + 0.3)

    def test_take_bonus_lives(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        bonus_lives = Bonus_lives(settings, screen)
        bonus_lives.rect.x = 146
        bonus_lives.rect.y = 390
        player_tank.check_bonus_lives(bonus_lives)
        self.assertEqual(settings.player_tank_life, 3 + 1)

    def test_take_bonus_damage(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        bonus_damage = Bonus_damage(settings, screen)
        bonus_damage.rect.x = 146
        bonus_damage.rect.y = 390
        player_tank.check_bonus_damage(bonus_damage)
        self.assertEqual(settings.player_tank_bullet_damage, 1 + 1)

    def test_move_right(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        player_tank.moving_right = True
        player_tank.move_next(blocks)
        self.assertEqual(player_tank.x, 146 + 1 * 0.07)

    def test_move_left(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        player_tank.moving_left = True
        player_tank.move_next(blocks)
        self.assertEqual(player_tank.x, 146 - 1 * 0.07)

    def test_move_up(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        player_tank.moving_up = True
        player_tank.move_next(blocks)
        self.assertEqual(player_tank.y, 390 - 1 * 0.07)

    def test_move_down(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        player_tank.y = 380
        player_tank.rect.y = 380
        blocks = Block(screen, 1, "dont save")
        player_tank.moving_down = True
        player_tank.move_next(blocks)
        self.assertEqual(player_tank.y, 380 + 1 * 0.07)

    def test_touch_tile_right(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        player_tank.x = 198.00999999999493
        player_tank.y = 303.9700000000084
        self.assertEqual(player_tank.touch_tile_right(blocks), False)
        player_tank.x = 133.96000000000117
        player_tank.y = 314.54000000000735
        self.assertEqual(player_tank.touch_tile_right(blocks), True)

    def test_touch_tile_left(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        player_tank.x = 128.99000000000166
        player_tank.y = 303.9700000000084
        self.assertEqual(player_tank.touch_tile_left(blocks), False)
        player_tank.x = 129.06000000000165
        player_tank.y = 316.8500000000071
        self.assertEqual(player_tank.touch_tile_left(blocks), True)

    def test_touch_tile_up(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        player_tank.x = 128.99000000000166
        player_tank.y = 303.9700000000084
        self.assertEqual(player_tank.touch_tile_up(blocks), False)
        player_tank.x = 128.99000000000166
        player_tank.y = 320.0000000000068
        self.assertEqual(player_tank.touch_tile_up(blocks), True)

    def test_touch_tile_down(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        blocks = Block(screen, 1, "dont save")
        player_tank.x = 190.1699999999957
        player_tank.y = 342.0500000000047
        self.assertEqual(player_tank.touch_tile_down(blocks), False)
        player_tank.x = 128.99000000000166
        player_tank.y = 309.9900000000078
        self.assertEqual(player_tank.touch_tile_down(blocks), True)


if __name__ == '__main__':
    unittest.main()
