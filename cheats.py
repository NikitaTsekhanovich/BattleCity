from settings import Settings
import pygame


class Cheats():
    def __init__(self):
        self.cheat_damage_bullet_speed = "hesoyam"
        self.cheat_move_speed = "forsaj"
        self.input = ""

    def cheat_check(self, ai_settings, event):
        if self.input == self.cheat_damage_bullet_speed:
            ai_settings.player_tank_bullet_speed = 1
            ai_settings.player_tank_bullet_damage = 3
        if self.input == self.cheat_move_speed:
            ai_settings.player_tank_acceleration = 0.2
            ai_settings.player_tank_life = 5

        elif (event.key == pygame.K_f or
              event.key == pygame.K_UP) and \
                self.input == "":
            self.input = "f"
            print(self.input)

        elif (event.key == pygame.K_r or
              event.key == pygame.K_UP) and \
                self.input == "fo":
            self.input += "r"
            print(self.input)

        elif (event.key == pygame.K_j or
              event.key == pygame.K_UP) and \
                self.input == "forsa":
            self.input += "j"
            print(self.input)

        elif (event.key == pygame.K_h or
            event.key == pygame.K_UP) and \
                self.input == "":
            self.input = "h"
            print(self.input)

        elif (event.key == pygame.K_e or
              event.key == pygame.K_UP) and \
                self.input == "h":
            self.input += "e"
            print(self.input)

        elif (event.key == pygame.K_s or
              event.key == pygame.K_UP) and \
             (self.input == "he" or self.input == "for"):
            self.input += "s"
            print(self.input)

        elif (event.key == pygame.K_o or
              event.key == pygame.K_UP) and \
             (self.input == "hes" or self.input == "f"):
            self.input += "o"
            print(self.input)

        elif (event.key == pygame.K_y or
              event.key == pygame.K_UP) and \
                self.input == "heso":
            self.input += "y"
            print(self.input)

        elif (event.key == pygame.K_a or
              event.key == pygame.K_UP) and \
             (self.input == "hesoy" or self.input == "fors"):
            self.input += "a"
            print(self.input)

        elif (event.key == pygame.K_m or
              event.key == pygame.K_UP) and \
                self.input == "hesoya":
            self.input += "m"
            print(self.input)

        else:
            self.input = ""