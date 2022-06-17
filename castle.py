import pygame
from pygame.sprite import Sprite


class Castle(Sprite):
    def __init__(self, screen):
        super().__init__()
        sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])
        self.screen = screen
        self.img_undamaged = sprites.subsurface(0, 15 * 2, 16 * 2, 16 * 2)  # крепость
        self.img_destroyed = sprites.subsurface(16 * 2, 15 * 2, 16 * 2, 16 * 2)  # сломанная крепость
        self.rect = pygame.Rect(12 * 16, 24 * 16, 32, 32)
        self.x = 192
        self.y = 384

    def draw(self):
        self.screen.blit(self.img_undamaged, self.rect)