import unittest
import pygame
import BattleCity as bs
from settings import Settings
from enemy_tank_hulk import Hulk_tank
from pygame.sprite import Group


class Test_enemy_tank_hulk(unittest.TestCase):
    def test_get_variables_Battle_city(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_hulk = Hulk_tank(settings, screen, None, "dont save")
        self.assertEqual(enemy_tank_hulk.screen, screen)
        self.assertEqual(enemy_tank_hulk.ai_settings, settings)

    def test_type(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        bullets = Group()
        enemy_tank_hulk = Hulk_tank(settings, screen, bullets, "dont save")
        self.assertEqual(type(enemy_tank_hulk.rect.x), int)
        self.assertEqual(type(enemy_tank_hulk.rect.y), int)
        self.assertEqual(type(enemy_tank_hulk.x), float)
        self.assertEqual(type(enemy_tank_hulk.y), float)
        self.assertEqual(type(enemy_tank_hulk.bullets), Group)


if __name__ == '__main__':
    unittest.main()