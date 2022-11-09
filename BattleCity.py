import pygame
from settings import Settings
from player_tank import Player_tank
from enemy_tank_predator import Predator_tank
from pygame.sprite import Group
from blocks import Block
from castle import Castle
from bonus_attribute import Bonus_attribute
from bonus_damage import Bonus_damage
from bonus_lives import Bonus_lives
from enemy_tank_hulk import Hulk_tank
from enemy_tank_kamikaze import Kamikaze_tank
from enemy_tank_crazy import Crazy_tank
import game_functions as gf
import time
import auto_save_system as sv


def run_game(run):
    pygame.init()
    save_data_tanks = sv.get_data_save_tanks()
    save_data_blocks = sv.get_data_save_blocks()
    ai_settings = Settings(save_data_tanks)
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Battle City")

    if save_data_tanks[0] == "auto save":
        current_level = int(save_data_tanks[11])
    else:
        current_level = 1
    blocks = Block(screen, current_level, save_data_blocks)

    bonus_attribute = Bonus_attribute(ai_settings, screen)
    bonus_damage = Bonus_damage(ai_settings, screen)
    bonus_lives = Bonus_lives(ai_settings, screen)
    bonuses_group = Group()

    castle = Castle(screen)
    castle_group = Group(castle)

    bullets_player = Group()
    bullets_enemy_tank_predator = Group()
    bullets_enemy_tank_hulk = Group()
    bullets_enemy_tank_crazy = Group()

    player_tank = Player_tank(ai_settings, screen, save_data_tanks)
    enemy_tank_predator = Predator_tank(ai_settings, screen, bullets_enemy_tank_predator, save_data_tanks)
    enemy_tank_hulk = Hulk_tank(ai_settings, screen, bullets_enemy_tank_hulk, save_data_tanks)
    enemy_tank_kamikaze = Kamikaze_tank(ai_settings, screen, save_data_tanks)
    enemy_tank_crazy = Crazy_tank(ai_settings, screen, bullets_enemy_tank_crazy, save_data_tanks)
    all_tanks = Group(player_tank, enemy_tank_predator, enemy_tank_hulk, enemy_tank_kamikaze, enemy_tank_crazy)

    while run:
        gf.check_events(ai_settings, screen, player_tank, bullets_player,
                        enemy_tank_predator, enemy_tank_hulk, enemy_tank_kamikaze,
                        enemy_tank_crazy, current_level, blocks)

        for tank in all_tanks:
            if tank == player_tank:
                tank.update(blocks, all_tanks, player_tank, bonus_attribute,
                            bonus_damage, bonus_lives, bonuses_group)
            if tank == enemy_tank_predator:
                tank.update(blocks, player_tank)
            if tank == enemy_tank_hulk:
                tank.update(blocks, all_tanks, player_tank, enemy_tank_hulk, castle)
            if tank == enemy_tank_kamikaze:
                tank.update(blocks, all_tanks, player_tank, enemy_tank_kamikaze)
            if tank == enemy_tank_crazy:
                tank.update(blocks)

        bullets_player.update(blocks, bullets_player, enemy_tank_predator, castle_group, all_tanks,
                              bonus_attribute, bonus_damage, bonus_lives, bonuses_group,
                              enemy_tank_hulk, player_tank, enemy_tank_kamikaze, enemy_tank_crazy)
        bullets_enemy_tank_predator.update(player_tank, blocks, bullets_enemy_tank_predator,
                                           enemy_tank_predator, castle_group, all_tanks)
        bullets_enemy_tank_hulk.update(player_tank, blocks, bullets_enemy_tank_hulk,
                                       enemy_tank_hulk, castle_group, all_tanks)
        bullets_enemy_tank_crazy.update(player_tank, blocks, bullets_enemy_tank_crazy,
                                        enemy_tank_crazy, castle_group, all_tanks)
        gf.update_screen(ai_settings, screen, player_tank, bullets_player,
                         blocks, enemy_tank_predator, bullets_enemy_tank_predator, all_tanks,
                         castle_group, bonuses_group, bonus_attribute, bonus_damage, bonus_lives,
                         enemy_tank_hulk, bullets_enemy_tank_hulk, enemy_tank_kamikaze,
                         enemy_tank_crazy, bullets_enemy_tank_crazy)

        if not (player_tank in all_tanks) and ai_settings.player_tank_life > 0:
            ai_settings.player_tank_life -= 1
            ai_settings.player_tank_acceleration = 0.04
            ai_settings.player_tank_bullet_speed = 0.1
            ai_settings.player_tank_bullet_damage = 1
            player_tank = Player_tank(ai_settings, screen, "dont save")
            all_tanks.add(player_tank)

        if not (enemy_tank_predator in all_tanks) and ai_settings.enemy_tank_predator_life > 0:
            ai_settings.enemy_tank_predator_life -= 1
            enemy_tank_predator = Predator_tank(ai_settings, screen, bullets_enemy_tank_predator, "dont save")
            all_tanks.add(enemy_tank_predator)

        if not (enemy_tank_hulk in all_tanks) and ai_settings.enemy_tank_hulk_life > 0:
            ai_settings.enemy_tank_hulk_life -= 1
            enemy_tank_hulk = Hulk_tank(ai_settings, screen, bullets_enemy_tank_hulk, "dont save")
            all_tanks.add(enemy_tank_hulk)

        if not (enemy_tank_kamikaze in all_tanks) and ai_settings.enemy_tank_kamikaze_life > 0:
            ai_settings.enemy_tank_kamikaze_life -= 1
            enemy_tank_kamikaze = Kamikaze_tank(ai_settings, screen, "dont save")
            all_tanks.add(enemy_tank_kamikaze)

        if not (enemy_tank_crazy in all_tanks) and ai_settings.enemy_tank_crazy_life > 0:
            ai_settings.enemy_tank_crazy_life -= 1
            enemy_tank_crazy = Crazy_tank(ai_settings, screen, bullets_enemy_tank_crazy, "dont save")
            all_tanks.add(enemy_tank_crazy)

        if not (castle in castle_group) or not (player_tank in all_tanks):
            sv.dont_save()
            break

        if ai_settings.enemy_tank_predator_life == 0 and \
                ai_settings.enemy_tank_hulk_life == 0 and \
                ai_settings.enemy_tank_kamikaze_life == 0 and \
                ai_settings.enemy_tank_crazy_life == 0:
            time.sleep(5)
            sv.dont_save()
            current_level += 1
            blocks = Block(screen, current_level, "dont save")
            castle = Castle(screen)
            castle_group = Group(castle)
            player_tank = Player_tank(ai_settings, screen, "dont save")
            enemy_tank_predator = Predator_tank(ai_settings, screen, bullets_enemy_tank_predator, "dont save")
            enemy_tank_hulk = Hulk_tank(ai_settings, screen, bullets_enemy_tank_hulk, "dont save")
            enemy_tank_kamikaze = Kamikaze_tank(ai_settings, screen, "dont save")
            enemy_tank_crazy = Crazy_tank(ai_settings, screen, bullets_enemy_tank_crazy, "dont save")
            all_tanks = Group(player_tank, enemy_tank_predator, enemy_tank_hulk, enemy_tank_kamikaze, enemy_tank_crazy)
            ai_settings = Settings("dont save")
