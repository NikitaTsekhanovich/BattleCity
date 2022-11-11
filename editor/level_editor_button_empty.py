import pygame
from pygame.sprite import Sprite


class ButtonEmpty(Sprite):
    def __init__(self, ai_settings, screen, x, y):
        super().__init__()

        tile_images = pygame.Surface((8 * 2, 8 * 2))

        self.screen = screen
        self.ai_settings = ai_settings
        self.image = tile_images
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.screen.blit(self.image, self.rect)
