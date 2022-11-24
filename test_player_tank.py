import unittest
import pygame
import BattleCity as bs
from settings import Settings
from player_tank import Player_tank


class Test_player_tank(unittest.TestCase):
    def test_get_variables_Battle_city(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        self.assertEqual(player_tank.screen, screen)
        self.assertEqual(player_tank.ai_settings, settings)

    def test_type(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen, "dont save")
        self.assertEqual(type(player_tank.rect.x), int)
        self.assertEqual(type(player_tank.rect.y), int)
        self.assertEqual(type(player_tank.x), float)
        self.assertEqual(type(player_tank.y), float)


if __name__ == '__main__':
    unittest.main()