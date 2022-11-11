import sys
import pygame
from fire_player_tank import Fire_player
from fire_enemy_tank_predator import Fire_predator
from fire_enemy_tank_hulk import Fire_hulk
from fire_enemy_tank_crazy import Fire_crazy
import auto_save_system as sv


def check_keydown_events(event, ai_settings, screen, player_tank, bullets_player,
                         enemy_tank_predator, enemy_tank_hulk, enemy_tank_kamikaze,
                         enemy_tank_crazy, current_level, blocks, cheats):
    cheats.cheat_check(ai_settings, event)

    if event.key == pygame.K_d or \
            event.key == pygame.K_RIGHT:
        player_tank.moving_right = True

    elif event.key == pygame.K_a or \
            event.key == pygame.K_LEFT:
        player_tank.moving_left = True

    elif event.key == pygame.K_s or \
            event.key == pygame.K_DOWN:
        player_tank.moving_down = True

    elif event.key == pygame.K_w or \
            event.key == pygame.K_UP:
        player_tank.moving_up = True

    elif event.key == pygame.K_ESCAPE:
        sv.auto_save(player_tank, enemy_tank_predator, enemy_tank_hulk,
                     enemy_tank_kamikaze, enemy_tank_crazy, current_level, blocks,
                     ai_settings)
        sys.exit()

    elif event.key == pygame.K_SPACE:
        player_tank_fire = True
        fire_bullet(ai_settings, screen, player_tank, bullets_player,
                    player_tank_fire, False, None, None,
                    None, None, False, None, None, False)


def fire_bullet(ai_settings, screen,
                player_tank, bullets_player, player_tank_fire,
                enemy_tank_predator_fire, bullets_enemy_tank_predator, enemy_tank_predator,
                enemy_tank_hulk, bullets_enemy_tank_hulk, enemy_tank_hulk_fire,
                enemy_tank_crazy, bullets_enemy_tank_crazy, enemy_tank_crazy_fire):
    if player_tank_fire:
        count_bullets(ai_settings, screen, player_tank, bullets_player, Fire_player, 1)
    if enemy_tank_predator_fire:
        count_bullets(ai_settings, screen, enemy_tank_predator, bullets_enemy_tank_predator, Fire_predator, 1)
    if enemy_tank_hulk_fire:
        count_bullets(ai_settings, screen, enemy_tank_hulk, bullets_enemy_tank_hulk, Fire_hulk, 1)
    if enemy_tank_crazy_fire:
        count_bullets(ai_settings, screen, enemy_tank_crazy, bullets_enemy_tank_crazy, Fire_crazy, 1)


def count_bullets(ai_settings, screen, tank, bullets, fire, bullets_allowed):
    if len(bullets) < bullets_allowed:
        new_bullet = fire(ai_settings, screen, tank)
        bullets.add(new_bullet)


def check_keyup_events(event, player_tank):
    if event.key == pygame.K_d or \
            event.key == pygame.K_RIGHT:
        player_tank.moving_right = False
    elif event.key == pygame.K_a or \
            event.key == pygame.K_LEFT:
        player_tank.moving_left = False
    elif event.key == pygame.K_s or \
            event.key == pygame.K_DOWN:
        player_tank.moving_down = False
    elif event.key == pygame.K_w or \
            event.key == pygame.K_UP:
        player_tank.moving_up = False


def check_events(ai_settings, screen, player_tank, bullets,
                 enemy_tank_predator, enemy_tank_hulk, enemy_tank_kamikaze,
                 enemy_tank_crazy, current_level, blocks, cheats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, player_tank, bullets,
                                 enemy_tank_predator, enemy_tank_hulk, enemy_tank_kamikaze,
                                 enemy_tank_crazy, current_level, blocks, cheats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player_tank)


def update_screen(ai_settings, screen, player_tank, bullets_player,
                  blocks, enemy_tank_predator, bullets_enemy_tank_predator, all_tanks,
                  castle_group, bonuses_group, bonus_attribute, bonus_damage, bonus_lives,
                  enemy_tank_hulk, bullets_enemy_tank_hulk, enemy_tank_kamikaze,
                  enemy_tank_crazy, bullets_enemy_tank_crazy):
    screen.fill(ai_settings.back_ground_color)

    for tank in all_tanks:
        if tank == player_tank:
            tank.blitme()
        if tank == enemy_tank_predator:
            tank.draw()
        if tank == enemy_tank_hulk:
            tank.draw()
        if tank == enemy_tank_kamikaze:
            tank.draw()
        if tank == enemy_tank_crazy:
            tank.draw()

    blocks.draw()

    for bonus in bonuses_group:
        if bonus == bonus_attribute:
            bonus.draw()
        if bonus == bonus_damage:
            bonus.draw()
        if bonus == bonus_lives:
            bonus.draw()

    for castle in castle_group:
        castle.draw()

    for bullet in bullets_player.sprites():
        bullet.draw_bullet()
    for bullet in bullets_enemy_tank_predator.sprites():
        bullet.draw_bullet()
    for bullet in bullets_enemy_tank_hulk.sprites():
        bullet.draw_bullet()
    for bullet in bullets_enemy_tank_crazy.sprites():
        bullet.draw_bullet()

    pygame.display.flip()
