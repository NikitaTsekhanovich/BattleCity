import unittest
import os
import pygame
from bonus_attribute import Bonus_attribute
from settings import Settings


class Test_blocks(unittest.TestCase):
    def test_correct_file_path(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        a = Bonus_attribute(settings, screen)
        b = a.draw()
        self.assertTrue(b, True)


if __name__ == '__main__':
    unittest.main()
