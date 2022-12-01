import unittest
import pygame
import BattleCity as bs
from settings import Settings
from enemy_tank_crazy import Crazy_tank
from pygame.sprite import Group


class Test_enemy_tank_crazy(unittest.TestCase):
    def test_get_variables_Battle_city(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        enemy_tank_crazy = Crazy_tank(settings, screen, None, "dont save")
        self.assertEqual(enemy_tank_crazy.screen, screen)
        self.assertEqual(enemy_tank_crazy.ai_settings, settings)

    def test_type(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        bullets = Group()
        enemy_tank_crazy = Crazy_tank(settings, screen, bullets, "dont save")
        self.assertEqual(type(enemy_tank_crazy.rect.x), int)
        self.assertEqual(type(enemy_tank_crazy.rect.y), int)
        self.assertEqual(type(enemy_tank_crazy.x), float)
        self.assertEqual(type(enemy_tank_crazy.y), float)
        self.assertEqual(type(enemy_tank_crazy.bullets), Group)


if __name__ == '__main__':
    unittest.main()