import unittest
import pygame
import BattleCity as bs
from cheats import Cheats
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
import BattleCity


class TestEnemyTankPredator(unittest.TestCase):
    def test_cheat_damage_bullet_speed(self):
        cheats = Cheats()
        settings = Settings("dont save")
        cheats.input = "hesoyam"
        cheats.cheat_input_check(settings)
        self.assertEqual(settings.player_tank_bullet_speed, 1)
        self.assertEqual(settings.player_tank_bullet_damage, 3)

    def test_cheat_move_speed(self):
        cheats = Cheats()
        settings = Settings("dont save")
        cheats.input = "forsaj"
        cheats.cheat_input_check(settings)
        self.assertEqual(settings.player_tank_acceleration, 0.2)
        self.assertEqual(settings.player_tank_life, 5)

    def test_cheat_next_level(self):
        bullets_enemy_tank_predator = Group()
        bullets_enemy_tank_hulk = Group()
        bullets_enemy_tank_crazy = Group()
        cheats = Cheats()
        ai_settings = Settings("dont save")

        cheats.input = "next"
        ai_settings.enemy_tank_predator_life = 0
        ai_settings.enemy_tank_hulk_life = 0
        ai_settings.enemy_tank_kamikaze_life = 0
        ai_settings.enemy_tank_crazy_life = 0

        current_level = 1
        screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
        blocks = Block(screen, current_level, "dont save")
        castle = Castle(screen)
        castle_group = Group(castle)
        player_tank = Player_tank(ai_settings, screen, "dont save")
        enemy_tank_predator = Predator_tank(ai_settings, screen, bullets_enemy_tank_predator, "dont save")
        enemy_tank_hulk = Hulk_tank(ai_settings, screen, bullets_enemy_tank_hulk, "dont save")
        enemy_tank_kamikaze = Kamikaze_tank(ai_settings, screen, "dont save")
        enemy_tank_crazy = Crazy_tank(ai_settings, screen, bullets_enemy_tank_crazy, "dont save")
        all_tanks = Group(player_tank, enemy_tank_predator, enemy_tank_hulk, enemy_tank_kamikaze, enemy_tank_crazy)
        new_ai_settings, new_all_tanks, new_blocks, new_castle, new_castle_group, new_current_level, \
        new_enemy_tank_crazy, new_enemy_tank_hulk, new_enemy_tank_kamikaze, new_enemy_tank_predator, new_player_tank = \
            BattleCity.next_level(ai_settings, all_tanks, blocks, bullets_enemy_tank_crazy, bullets_enemy_tank_hulk,
                                  bullets_enemy_tank_predator, castle, castle_group, cheats, current_level,
                                  enemy_tank_crazy, enemy_tank_hulk, enemy_tank_kamikaze, enemy_tank_predator,
                                  player_tank, screen)
        self.assertEqual(type(new_ai_settings), type(ai_settings))
        self.assertEqual(type(new_all_tanks), type(all_tanks))
        self.assertEqual(type(new_blocks), type(blocks))
        self.assertEqual(type(new_castle), type(castle))
        self.assertEqual(type(new_castle_group), type(castle_group))
        self.assertEqual(new_current_level, current_level + 1)
        self.assertEqual(type(new_enemy_tank_crazy), type(enemy_tank_crazy))
        self.assertEqual(type(new_enemy_tank_hulk), type(enemy_tank_hulk))
        self.assertEqual(type(new_enemy_tank_kamikaze), type(enemy_tank_kamikaze))
        self.assertEqual(type(new_enemy_tank_predator), type(enemy_tank_predator))
        self.assertEqual(type(new_player_tank), type(player_tank))


if __name__ == '__main__':
    unittest.main()
