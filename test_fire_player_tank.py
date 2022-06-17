import unittest
import pygame
import BattleCity as bs
from settings import Settings
from player_tank import Player_tank
from fire_player_tank import Fire_player


class Test_fire_player_tank(unittest.TestCase):
    def test_get_variables_Battle_city(self):
        settings = Settings()
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen)
        fire_player = Fire_player(settings, screen, player_tank)

        self.assertEqual(fire_player.screen, screen)
        self.assertEqual(fire_player.ai_settings, settings)

    def test_get_variables_player_tank(self):
        settings = Settings()
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        player_tank = Player_tank(settings, screen)
        fire_player = Fire_player(settings, screen, player_tank)
        self.assertEqual(fire_player.rect.x, player_tank.rect.centerx)
        self.assertEqual(fire_player.rect.y, player_tank.rect.top)
        self.assertEqual(fire_player.fire_down_player, player_tank.moving_look_down)
        self.assertEqual(fire_player.fire_right_player, player_tank.moving_look_right)
        self.assertEqual(fire_player.fire_left_player, player_tank.moving_look_left)
        self.assertEqual(fire_player.fire_up_player, player_tank.moving_look_up)


if __name__ == '__main__':
    unittest.main()