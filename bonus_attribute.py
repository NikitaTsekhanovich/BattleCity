import pygame
import random
from pygame.sprite import Sprite


class Bonus_attribute(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])
        self.images = sprites.subsurface(16*6, 32*2, 16*2, 15*2)
        self.image = self.images
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = random.uniform(0, 370)
        self.rect.y = random.uniform(0, 380)
        self.acceleration = 0.01
        self.bullet_speed = 0.3

    def draw(self):
        self.screen.blit(self.image, self.rect)