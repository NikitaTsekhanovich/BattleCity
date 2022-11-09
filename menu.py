import pygame
from settings import Settings
import pygame_menu
import BattleCity as bs


def Menu():
    pygame.init()
    ai_settings = Settings("dont save")
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Battle City")
    main_theme = pygame_menu.themes.THEME_DARK.copy()
    main_theme.set_background_color_opacity(0.0)
    menu = pygame_menu.Menu('', 480, 416, theme=main_theme)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)


def start_the_game():
    bs.run_game(True)


Menu()