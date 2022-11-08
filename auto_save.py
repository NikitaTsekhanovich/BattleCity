def auto_save(player_tank, enemy_tank_predator, enemy_tank_hulk,
              enemy_tank_kamikaze, enemy_tank_crazy, current_level, blocks):
    file = open("save.txt", "w")

    file.write("auto save\n")
    file.write(f'{str(player_tank.x)}\n{str(player_tank.y)}\n'
               f'{str(enemy_tank_predator.x)}\n{str(enemy_tank_predator.y)}\n'
               f'{str(enemy_tank_hulk.x)}\n{str(enemy_tank_hulk.y)}\n'
               f'{str(enemy_tank_kamikaze.x)}\n{str(enemy_tank_kamikaze.y)}\n'
               f'{str(enemy_tank_crazy.x)}\n{str(enemy_tank_crazy.y)}\n'
               f'{str(current_level)}\n'
               f'{str(blocks)}\n')
    file.close()
    print("save")


def get_data_save():
    file = open("save.txt", "r")
    l = [line.strip() for line in file]
    file.close()
    return l


def dont_save():
    file = open("save.txt", "w")
    file.write("dont save")
    file.close()
