import pygame
from pygame.sprite import Sprite


class ButtonBrick(Sprite):
    def __init__(self, ai_settings, screen, new_button, x, y):
        super().__init__()

        try:
            sprites = pygame.transform.scale(pygame.image.load
                                         (r"C:\Users\honor\source\repos\BattleCity\images\sprites.gif"), [192, 224])
        except Exception:
            print("Поврежден файл игры")
            sys.exit()

        tile_images = sprites.subsurface(48 * 2, 64 * 2, 8 * 2, 8 * 2)

        self.screen = screen
        self.ai_settings = ai_settings
        self.image = tile_images
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        if new_button == "null":
            self.rect.x = 440
            self.rect.y = 50
        else:
            self.rect.x = x
            self.rect.y = y

    def draw(self):
        self.screen.blit(self.image, self.rect)
