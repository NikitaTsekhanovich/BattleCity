import pygame
from settings import Settings
from player_tank import Player_Tank
import game_functions as gf
from pygame.sprite import Group


#  pygame.event.get() Каждое событие идентифицируется методом

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Battle City")
    player_tank = Player_Tank(ai_settings, screen)
    bullets = Group()

    # Запус основного цикла игры
    while True:
        gf.check_events(ai_settings, screen, player_tank, bullets)
        player_tank.update()
        bullets.update()
        for bullet in bullets.copy():
           if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, player_tank, bullets)


run_game()