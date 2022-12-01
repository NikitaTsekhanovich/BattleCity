import unittest
import os
import pygame
from settings import Settings


class TestSettings(unittest.TestCase):
    def test_auto_save(self):
        file = open("test_save_tanks.txt", "r")
        save_data = [line.strip() for line in file]
        file.close()

        settings = Settings(save_data)

        self.assertTrue(settings.player_tank_life, int(save_data[12]))
        self.assertTrue(settings.enemy_tank_predator_life, int(save_data[13]))
        self.assertTrue(settings.enemy_tank_hulk_life, int(save_data[14]))
        self.assertTrue(settings.enemy_tank_kamikaze_life, int(save_data[15]))
        self.assertTrue(settings.enemy_tank_crazy_life, int(save_data[16]))

    def test_dont_auto_save(self):
        settings = Settings("dont save")

        self.assertTrue(settings.player_tank_life, 3)
        self.assertTrue(settings.enemy_tank_predator_life, 3)
        self.assertTrue(settings.enemy_tank_hulk_life, 3)
        self.assertTrue(settings.enemy_tank_kamikaze_life, 3)
        self.assertTrue(settings.enemy_tank_crazy_life, 3)


if __name__ == '__main__':
    unittest.main()
