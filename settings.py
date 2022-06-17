class Settings:
    def __init__(self):
        self.screen_width = 480
        self.screen_height = 416
        self.back_ground_color = (0, 0, 0)

        self.player_tank_acceleration = 0.07
        self.player_tank_pos_x = 146
        self.player_tank_pos_y = 390
        self.player_tank_bullet_speed = 0.1
        self.player_tank_bullet_damage = 1
        self.player_tank_life = 3

        self.enemy_tank_pos_x = 0
        self.enemy_tank_pos_y = 0

        self.predator_tank_speed = 0.1
        self.predator_tank_bullet_speed = 0.1
        self.enemy_tank_predator_life = 3

        self.hulk_tank_speed = 0.03
        self.hulk_tank_bullet_speed = 0.5
        self.enemy_tank_hulk_life = 3

        self.kamikaze_tank_speed = 0.15
        self.enemy_tank_kamikaze_life = 3

        self.crazy_tank_speed = 0.05
        self.crazy_tank_bullet_speed = 0.3
        self.enemy_tank_crazy_life = 3