import unittest
import pygame
import BattleCity as bs
from settings import Settings
from player_tank import Player_tank
# import auto_save_system as sv


class Test_player_tank(unittest.TestCase):
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

    def test_take_bonus(self):
        settings = Settings("auto save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        bonus_attribute = Bonus_attribute(settings, screen)
        bonus_damage = Bonus_damage(settings, screen)
        bonus_lives = Bonus_lives(settings, screen)
        bonuses_group = Group()
        player_tank.check_bonuses(bonus_attribute, bonus_damage, bonus_lives, bonuses_group)

if __name__ == '__main__':
    unittest.main()
