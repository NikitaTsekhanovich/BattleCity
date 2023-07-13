import pygame
import sys
import os
from pathlib import Path
from editor.level_editor_button_brick import ButtonBrick
from editor.level_editor_button_froze import ButtonFroze
from editor.level_editor_button_water import ButtonWater
from editor.level_editor_button_grass import ButtonGrass
from editor.level_editor_button_steel import ButtonSteel
from editor.level_editor_button_empty import ButtonEmpty
from editor.level_editor_settings import GameFieldSettings


def check_events(button_brick, button_froze, button_water,
                 button_grass, button_steel, game_field_settings,
                 all_buttons, ai_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_coord = event.pos
            game_field_settings.current_block = check_mouse_click_buttons(button_brick, button_froze, button_water,
                                                                          button_grass, button_steel, mouse_coord)
        if event.type == pygame.MOUSEBUTTONUP:
            x = 0
            y = 0
            row = 0
            column = 0
            while row < event.pos[0]:
                x += 1
                row += 16
            while column < event.pos[1]:
                y += 1
                column += 16

            if game_field_settings.current_block is None:
                game_field_settings.current_block = '.'
                button_empty = ButtonEmpty(ai_settings, screen,
                                           (event.pos[0] // 16) * 16, (event.pos[1] // 16) * 16)
                all_buttons.add(button_empty)
            try:
                game_field_settings.game_field[y - 1][x - 1] = game_field_settings.current_block

                if game_field_settings.current_block == '#':
                    button_brick = ButtonBrick(ai_settings, screen, "add",
                                               (event.pos[0] // 16) * 16, (event.pos[1] // 16) * 16)
                    all_buttons.add(button_brick)
                if game_field_settings.current_block == '-':
                    button_froze = ButtonFroze(ai_settings, screen, "add",
                                               (event.pos[0] // 16) * 16, (event.pos[1] // 16) * 16)
                    all_buttons.add(button_froze)
                if game_field_settings.current_block == '~':
                    button_water = ButtonWater(ai_settings, screen, "add",
                                               (event.pos[0] // 16) * 16, (event.pos[1] // 16) * 16)
                    all_buttons.add(button_water)
                if game_field_settings.current_block == '%':
                    button_grass = ButtonGrass(ai_settings, screen, "add",
                                               (event.pos[0] // 16) * 16, (event.pos[1] // 16) * 16)
                    all_buttons.add(button_grass)
                if game_field_settings.current_block == '@':
                    button_steel = ButtonSteel(ai_settings, screen, "add",
                                               (event.pos[0] // 16) * 16, (event.pos[1] // 16) * 16)
                    all_buttons.add(button_steel)
            except IndexError:
                print("Out of the field")
            print(game_field_settings.game_field)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_s:
                save_game_field(game_field_settings.game_field)


def save_game_field(game_field):
    new_level = open(r"editor\new_level", "w")
    for x in range(26):
        if x != 0:
            new_level.write("\n")
        for y in range(26):
            new_level.write(game_field[x][y])
    new_level.close()

    path = r'levels'
    path_copy = r"editor"
    folder = Path(path)
    if not folder.is_dir():
        raise ValueError(f"[{folder}] не существует или не является директорией")
    count_levels = sum(1 for x in folder.iterdir())
    os.system(f'copy {path_copy}\\new_level {path}')
    os.rename(f'{path}\\new_level', f'{path}\{count_levels + 1}')


def check_mouse_click_buttons(button_brick, button_froze, button_water,
                              button_grass, button_steel, mouse_coord):
    if button_brick.rect.y <= mouse_coord[1] <= button_brick.rect.y + 16 and \
       button_brick.rect.x <= mouse_coord[0] <= button_brick.rect.x + 16:
        return '#'
    if button_froze.rect.y <= mouse_coord[1] <= button_froze.rect.y + 16 and \
       button_froze.rect.x <= mouse_coord[0] <= button_froze.rect.x + 16:
        return '-'
    if button_water.rect.y <= mouse_coord[1] <= button_water.rect.y + 16 and \
       button_water.rect.x <= mouse_coord[0] <= button_water.rect.x + 16:
        return '~'
    if button_grass.rect.y <= mouse_coord[1] <= button_grass.rect.y + 16 and \
       button_grass.rect.x <= mouse_coord[0] <= button_grass.rect.x + 16:
        return '%'
    if button_steel.rect.y <= mouse_coord[1] <= button_steel.rect.y + 16 and \
       button_steel.rect.x <= mouse_coord[0] <= button_steel.rect.x + 16:
        return '@'


def update_screen(screen, all_buttons):
    for button in all_buttons:
        button.draw()

    for row in range(27):
        pygame.draw.aaline(screen, (255, 255, 255), [0, 0+16*row], [416, 0+16*row])
        pygame.draw.aaline(screen, (255, 255, 255), [0+16*row, 0], [0+16*row, 416])

    pygame.display.flip()
