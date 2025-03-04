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
        self.tiles = [[] for _ in range(Map. NUM_OF_ROWS)]  # Create a two-dimensional array  
        self.all_zombies_2d = [[] for _ in range(Map. NUM_OF_ROWS)]
        self.all_bullets_2d = [[] for _ in range(Map. NUM_OF_ROWS)]
        self.all_suns_1d = []
        self.all_plants_2d = [[]  for _ in range(Map. NUM_OF_ROWS)]
        self.__add_tiles()

    def __add_tiles(self):  
        
        i = 0 
        j = 0
        try: 
            for y in range(Map.START_MAP_POS_Y, Map.END_MAP_POS_Y, Tile.TILE_SIZE[1]): 
                #print(f"Outer Loop Value: {x}")  
                for x in range(Map.START_MAP_POS_X, Map.END_MAP_POS_X, Tile.TILE_SIZE[0]): 
                    #print(f"    Inner Loop Value: {y}")  
                    tile = Tile(x , x + Tile.TILE_SIZE[0], y, y + Tile.TILE_SIZE[1], i, j)     
                    self.tiles[i].append(tile)      
                    j += 1
                i += 1
                j = 0
        
        except Exception as e:
            print(e)
            print(i, j)
        
        # try:
        #     for row in self.tiles:  
        #         for col in row:
        #             print(col.row_num , col.col_num, end="---") 
        #         print()
        # except Exception as e:
        #     print(row)
        #     print(col)
        #     print("erorrrrrrrrrrr")


    def find_tile_by_pos(self, x_mos_pos , y_mos_pos) -> Tile:
        i_int_temp = (y_mos_pos - Map.START_MAP_POS_Y) // Tile.TILE_SIZE[1]
        j_int_temp = (x_mos_pos - Map.START_MAP_POS_X) // Tile.TILE_SIZE[0]
        # print("wwwwwww::",i_int_temp)
        # print("wwwwwww::",j_int_temp)
        # print("y_mos_pos:  ", y_mos_pos)
        # print('x_mox_pos:  ', x_mos_pos)

        if 0 <= i_int_temp < Map.NUM_OF_ROWS and 0 <= j_int_temp < Map.NUM_OF_COLS:
            ###
            print("mouse_click_in_map_pos:  ", f"({i_int_temp} , {j_int_temp})")
        
            return self.tiles[i_int_temp][j_int_temp] 
        else :
            print("no tile found")
            return None
        
    def add_plant(self, new_plant, tile):
        tile.set_plant(new_plant)
        self.all_plants_2d[tile.get_row_num()].append(new_plant)

    def remove_sun(self, mouse_pos):
        intended_sun = None
        for sun in self.all_suns_1d:
            if sun.colide_with_mouse_click(mouse_pos):
                intended_sun = sun
                break
            
        if intended_sun is not None:
            self.all_suns_1d.remove(intended_sun)


        
    # def place_the_plant(self, plant, x_pos, y_pos):  ################## not done
    #     tile = self.calc_tile_which_mouse_is_left_in_its_range(x_pos, y_pos)
    #     if tile is None:
    #         return 
    #         pass
        
    #     if not tile.is_tile_empty():
    #         return 
    #         pass
        
    #     tile.set_plant(plant=plant)

    def did_bullet_hit_in_this_pos(self, x_pos, row_num):
        for index, zombie in enumerate(self.all_zombies_2d[row_num]):
            if zombie.did_bullet_hit():
                zombie.bullet_hit()
                if not zombie.is_alive():


                    return True
                
    def add_zombie(self, zombie, row_num):
        self.all_zombies_2d[row_num].append(zombie)

    def add_sun(self, sun):
        self.all_suns_1d.append(sun)

    def add_bullet(self, bullet, row_num):
        self.all_bullets_2d[row_num].append(bullet)


    def remove_plant(self, plant, row_num): 
        print("plant:  ", plant) 
        print("row plants :  ", self.all_plants_2d[row_num])
        print("row_num: ", row_num)
        self.all_plants_2d[row_num].remove(plant)
        for tile in self.tiles[row_num]:
            if tile.is_position_in_this_tile(plant.get_x_pos(), plant.get_y_pos()):
                tile.remove_plant()
                break

    def remove_bullet(self, bullet, row_num):
        if bullet in self.all_bullets_2d[row_num]:
            self.all_bullets_2d[row_num].remove(bullet)

    def remove_zombie(self, zombie, row_num):
        print("remove zombie was called")
        self.all_zombies_2d[row_num].remove(zombie)



