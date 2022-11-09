import pygame
import sys


class Block():

    (TILE_EMPTY, TILE_BRICK, TILE_STEEL, TILE_WATER, TILE_GRASS, TILE_FROZE) = range(6)

    def __init__(self, screen, current_level, save_data):
        self.screen = screen
        self.path_file = "levels/"
        if current_level > 35:
            current_level = 1

        try:
            self.level = open(f'{self.path_file}{current_level}', 'r')
        except Exception:
            print("Поврежден файл игры")
            sys.exit()

        data = self.level.read().split("\n")
        sprites = pygame.transform.scale(pygame.image.load("images/sprites.gif"), [192, 224])

        tile_images = [
            pygame.Surface((8 * 2, 8 * 2)),
            sprites.subsurface(48 * 2, 64 * 2, 8 * 2, 8 * 2),
            sprites.subsurface(48 * 2, 72 * 2, 8 * 2, 8 * 2),
            sprites.subsurface(56 * 2, 72 * 2, 8 * 2, 8 * 2),
            sprites.subsurface(64 * 2, 64 * 2, 8 * 2, 8 * 2),
            sprites.subsurface(64 * 2, 64 * 2, 8 * 2, 8 * 2),
            sprites.subsurface(72 * 2, 64 * 2, 8 * 2, 8 * 2),
            sprites.subsurface(64 * 2, 72 * 2, 8 * 2, 8 * 2)
        ]

        self.tile_empty = tile_images[0]
        self.tile_brick = tile_images[1]
        self.tile_steel = tile_images[2]
        self.tile_grass = tile_images[3]
        self.tile_water = tile_images[4]
        self.tile_water1 = tile_images[4]
        self.tile_water2 = tile_images[5]
        self.tile_froze = tile_images[6]
        self.mapr = []
        self.tile_size = 16
        if save_data[0] == "auto save":
            for i in range(2, int(save_data[1])):
                block_characteristics = save_data[i].split(" ")
                self.mapr.append(myRect(int(block_characteristics[0]), int(block_characteristics[1]),
                                        self.tile_size, self.tile_size, int(block_characteristics[2])))
        else:
            x, y = 0, 0
            for row in data:
                for ch in row:
                    if ch == "#":
                        self.mapr.append(myRect(x, y, self.tile_size, self.tile_size, self.TILE_BRICK))
                    elif ch == "@":
                        self.mapr.append(myRect(x, y, self.tile_size, self.tile_size, self.TILE_STEEL))
                    elif ch == "~":
                        self.mapr.append(myRect(x, y, self.tile_size, self.tile_size, self.TILE_WATER))
                    elif ch == "%":
                        self.mapr.append(myRect(x, y, self.tile_size, self.tile_size, self.TILE_GRASS))
                    elif ch == "-":
                        self.mapr.append(myRect(x, y, self.tile_size, self.tile_size, self.TILE_FROZE))
                    x += self.tile_size
                x = 0
                y += self.tile_size

    def draw(self):
        (TILE_EMPTY, TILE_BRICK, TILE_STEEL, TILE_WATER, TILE_GRASS, TILE_FROZE) = range(6)
        tiles = [TILE_BRICK, TILE_STEEL, TILE_WATER, TILE_GRASS, TILE_FROZE]

        for tile in self.mapr:
            if tile.type in tiles:
                if tile.type == self.TILE_BRICK:
                    self.screen.blit(self.tile_brick, tile.topleft)
                elif tile.type == self.TILE_STEEL:
                    self.screen.blit(self.tile_steel, tile.topleft)
                elif tile.type == self.TILE_WATER:
                    self.screen.blit(self.tile_water, tile.topleft)
                elif tile.type == self.TILE_FROZE:
                    self.screen.blit(self.tile_froze, tile.topleft)
                elif tile.type == self.TILE_GRASS:
                    self.screen.blit(self.tile_grass, tile.topleft)


class myRect(pygame.Rect):
    def __init__(self, left, top, width, height, type):
        pygame.Rect.__init__(self, left, top, width, height)
        self.type = type
