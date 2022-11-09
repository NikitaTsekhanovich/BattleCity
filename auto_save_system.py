def auto_save(player_tank, enemy_tank_predator, enemy_tank_hulk,
              enemy_tank_kamikaze, enemy_tank_crazy, current_level, blocks,
              ai_settings):
    file_tanks = open("save tanks.txt", "w")
    file_tanks.write("auto save\n")
    file_tanks.write(f'{str(player_tank.x)}\n{str(player_tank.y)}\n'
                     f'{str(enemy_tank_predator.x)}\n{str(enemy_tank_predator.y)}\n'
                     f'{str(enemy_tank_hulk.x)}\n{str(enemy_tank_hulk.y)}\n'
                     f'{str(enemy_tank_kamikaze.x)}\n{str(enemy_tank_kamikaze.y)}\n'
                     f'{str(enemy_tank_crazy.x)}\n{str(enemy_tank_crazy.y)}\n'
                     f'{str(current_level)}\n'
                     f'{str(ai_settings.player_tank_life)}\n'
                     f'{str(ai_settings.enemy_tank_predator_life)}\n'
                     f'{str(ai_settings.enemy_tank_hulk_life)}\n'
                     f'{str(ai_settings.enemy_tank_kamikaze_life)}\n'
                     f'{str(ai_settings.enemy_tank_crazy_life)}\n')
    file_tanks.close()

    file_blocks = open("save blocks.txt", "w")
    file_blocks.write("auto save\n")
    file_blocks.write(f'{str(len(blocks.mapr))}\n')
    for block in blocks.mapr:
        file_blocks.write(f'{str(block[0])} {str(block[1])} {str(block.type)}\n')

    print("save")


def get_data_save_tanks():
    file = open("save tanks.txt", "r")
    l = [line.strip() for line in file]
    file.close()
    return l


def get_data_save_blocks():
    file = open("save blocks.txt", "r")
    l = [line.strip() for line in file]
    file.close()
    return l


def dont_save():
    file = open("save tanks.txt", "w")
    file.write("dont save")
    file.close()
    file = open("save blocks.txt", "w")
    file.write("dont save")
    file.close()
