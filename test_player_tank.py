import unittest
import pygame
import BattleCity as bs
from settings import Settings
from player_tank import Player_tank
from bonus_attribute import Bonus_attribute
from bonus_damage import Bonus_damage
from bonus_lives import Bonus_lives


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
        player_tank.moving_right = True


if __name__ == '__main__':
    unittest.main()
