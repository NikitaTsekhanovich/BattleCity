from settings import Settings
import pygame
import editor.level_editor_functions as lf
from editor.level_editor_button_brick import ButtonBrick
from editor.level_editor_button_froze import ButtonFroze
from editor.level_editor_button_water import ButtonWater
from editor.level_editor_button_grass import ButtonGrass
from editor.level_editor_button_steel import ButtonSteel
from editor.level_editor_button_empty import ButtonEmpty
from editor.level_editor_settings import GameFieldSettings
from pygame.sprite import Group


def level_editor():
    ai_settings = Settings("dont save")
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    button_brick = ButtonBrick(ai_settings, screen, "null", 0, 0)
    button_froze = ButtonFroze(ai_settings, screen, "null", 0, 0)
    button_water = ButtonWater(ai_settings, screen, "null", 0, 0)
    button_grass = ButtonGrass(ai_settings, screen, "null", 0, 0)
    button_steel = ButtonSteel(ai_settings, screen, "null", 0, 0)
    button_empty = ButtonEmpty(ai_settings, screen, 0, 0)
    game_field_settings = GameFieldSettings()
    all_buttons = Group(button_brick, button_froze, button_water,
                        button_grass, button_steel, button_empty)
    while True:
        lf.update_screen(screen, all_buttons)
        lf.check_events(button_brick, button_froze, button_water,
                        button_grass, button_steel, game_field_settings,
                        all_buttons, ai_settings, screen)
