import pygame
import time
import os
from Tile import Tile


class Map: 

    START_MAP_POS_X = 275
    END_MAP_POS_X = 1121

    START_MAP_POS_Y = 100
    END_MAP_POS_Y = 650

    NUM_OF_ROWS = 5
    NUM_OF_COLS = 9

    def __init__(self):   
        self.tiles = [[None for _ in range(9)] for _ in range(5)]  # Create a two-dimensional array  
        self.__add_tiles()

    def __add_tiles(self):  
        
        i = 0 
        j = 0
        for x in range(Map.START_MAP_POS_X, Map.END_MAP_POS_X, Tile.TILE_SIZE[0]): 
           # print(f"Outer Loop Value: {x}")  
            for y in range(Map.START_MAP_POS_Y, Map.END_MAP_POS_Y, Tile.TILE_SIZE[1]): 
               # print(f"    Inner Loop Value: {y}")  
                tile = Tile(x , x + Tile.TILE_SIZE[0], y, y + Tile.TILE_SIZE[1], i, j)  
                self.tiles[i][j] = tile   
                j += 1
            i += 1
            j = 0

    def calc_tile_which_mouse_is_left_in_its_range(self, x_mos_pos , y_mos_pos) -> Tile:
        i_int_temp = (x_mos_pos - Map.START_MAP_POS_X) // Tile.TILE_SIZE[0]
        j_int_temp = (y_mos_pos - Map.START_MAP_POS_Y) // Tile.TILE_SIZE[1]

        if 0 <= i_int_temp < Map.NUM_OF_ROWS and 0 <= j_int_temp < Map.NUM_OF_COLS:
            ###
            print("mouse_click_in_map_pos:  ", f"({i_int_temp} , {j_int_temp})")
            return self.tiles[i_int_temp][j_int_temp] 
        else :
            return None
        
    def place_the_plant(self, plant, x_pos, y_pos):  ################## not done
        tile = self.calc_tile_which_mouse_is_left_in_its_range(x_pos, y_pos)
        if tile is None:
            return 
            pass
        
        if not tile.is_tile_empty():
            return 
            pass
        
        tile.set_plant(plant=plant)

