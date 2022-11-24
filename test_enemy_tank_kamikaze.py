import unittest
import pygame
import BattleCity as bs
from settings import Settings
from enemy_tank_kamikaze import Kamikaze_tank


class Test_enemy_tank_kamikaze(unittest.TestCase):
    def test_get_variables_Battle_city(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_kamikaze = Kamikaze_tank(settings, screen, "dont save")
        self.assertEqual(enemy_tank_kamikaze.screen, screen)
        self.assertEqual(enemy_tank_kamikaze.ai_settings, settings)

    def test_type(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_kamikaze = Kamikaze_tank(settings, screen, "dont save")
        self.assertEqual(type(enemy_tank_kamikaze.rect.x), int)
        self.assertEqual(type(enemy_tank_kamikaze.rect.y), int)
        self.assertEqual(type(enemy_tank_kamikaze.x), float)
        self.assertEqual(type(enemy_tank_kamikaze.y), float)


if __name__ == '__main__':
    unittest.main()