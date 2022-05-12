import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, player_tank):
        super().__init__()
        self.screen = screen

        # создание пули и ее направления
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        # self.rect.x = player_tank.rect.x
        # self.rect.top = player_tank.rect.top
        self.rect.centerx = player_tank.rect.centerx
        self.rect.top = player_tank.rect.top
        # Позиция пули
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        # перемещение пули
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
