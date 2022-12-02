from settings import Settings
import pygame


class Cheats():
    def __init__(self):
        self.cheat_damage_bullet_speed = "hesoyam"
        self.cheat_move_speed = "forsaj"
        self.cheat_next_level = "next"
        self.input = ""

    def cheat_input(self, ai_settings, event):
        self.cheat_input_check(ai_settings)

        if (event.key == pygame.K_n or
            event.key == pygame.K_UP) and \
                self.input == "":
            self.input = "n"

        elif (event.key == pygame.K_x or
              event.key == pygame.K_UP) and \
                self.input == "ne":
            self.input += "x"

        elif (event.key == pygame.K_t or
              event.key == pygame.K_UP) and \
                self.input == "nex":
            self.input += "t"

        elif (event.key == pygame.K_f or
              event.key == pygame.K_UP) and \
                self.input == "":
            self.input = "f"

        elif (event.key == pygame.K_r or
              event.key == pygame.K_UP) and \
                self.input == "fo":
            self.input += "r"

        elif (event.key == pygame.K_j or
              event.key == pygame.K_UP) and \
                self.input == "forsa":
            self.input += "j"

        elif (event.key == pygame.K_h or
              event.key == pygame.K_UP) and \
                self.input == "":
            self.input = "h"

        elif (event.key == pygame.K_e or
              event.key == pygame.K_UP) and \
                (self.input == "h" or self.input == "n"):
            self.input += "e"

        elif (event.key == pygame.K_s or
              event.key == pygame.K_UP) and \
             (self.input == "he" or self.input == "for"):
            self.input += "s"

        elif (event.key == pygame.K_o or
              event.key == pygame.K_UP) and \
             (self.input == "hes" or self.input == "f"):
            self.input += "o"

        elif (event.key == pygame.K_y or
              event.key == pygame.K_UP) and \
                self.input == "heso":
            self.input += "y"

        elif (event.key == pygame.K_a or
              event.key == pygame.K_UP) and \
             (self.input == "hesoy" or self.input == "fors"):
            self.input += "a"

        elif (event.key == pygame.K_m or
              event.key == pygame.K_UP) and \
                self.input == "hesoya":
            self.input += "m"

        else:
            self.input = ""

    def cheat_input_check(self, ai_settings):
        if self.input == self.cheat_damage_bullet_speed:
            ai_settings.player_tank_bullet_speed = 1
            ai_settings.player_tank_bullet_damage = 3
        if self.input == self.cheat_move_speed:
            ai_settings.player_tank_acceleration = 0.2
            ai_settings.player_tank_life = 5
