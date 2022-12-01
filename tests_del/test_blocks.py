import unittest
import os
import pygame
from settings import Settings
from blocks import Block


class Test_blocks(unittest.TestCase):
    def test_correct_file_path(self):
        settings = Settings("dont save")
        screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        block = Block(screen, 1, "dont save")
        self.assertTrue(os.path.exists(block.path_file))


if __name__ == '__main__':
    unittest.main()
