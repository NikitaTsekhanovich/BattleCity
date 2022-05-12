import pygame


# flag = True

class Player_Tank():
    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения корабля и получение прямоугольника.
        # self.image = pygame.image.load('ImagesOld/Player_Tank.png')
        sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])
        self.image = sprites.subsurface(0, 0, 13*2, 13*2)
        # метод get_rect() используется
        # для получения атрибута rect поверхности
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана. 236 стр

        self.rect.x = 450
        self.rect.y = 680
        self.width_player = 114
        self.height_player = 106
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        self.move_next()

    def move_next(self):
        if self.moving_right and self.ai_settings.screen_width - self.width_player != self.rect.x:
            self.rect.x += 1
            self.image = self.image_right
            # if flag:
            #     self.rotate_tank(270)
        elif self.moving_left and self.rect.x != 0:
            self.rect.x -= 1
            # if flag:
            #     self.rotate_tank(90)
        elif self.moving_up and self.rect.y != 0:
            self.rect.y -= 1
            # if flag:
            #     self.rotate_tank(0)
        elif self.moving_down and self.ai_settings.screen_height - self.height_player != self.rect.y:
            self.rect.y += 1
            # if flag:
            #     self.rotate_tank(180)

    # def rotate_tank(self, angle):
    #     flag = False
    #     self.image = pygame.transform.rotate(self.image, angle)

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
