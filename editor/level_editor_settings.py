class GameFieldSettings():
    def __init__(self):
        self.current_block = '.'
        self.game_field = ['.'] * 26
        for index in range(26):
            self.game_field[index] = ['.'] * 26
