from Plant import *



class User:

    def __init__(self, maap, time):
        self.is_brain_eaten = False
        self.nums_of_sun = 0
        self.time = time
        self.maap = maap

    def place_the_plant(self, plant_type, pos_x, pos_y):
        new_plant = None
        tile = self.maap.find_tile_by_pos(pos_x, pos_y)
        if tile is not None:
            if tile.is_empty():
                if plant_type == PeaShooter.NAME:
                    new_plant = PeaShooter(tile.get_x_center(), tile.get_y_center(), self.maap, 
                                           self.time, tile.get_row_num(), tile.get_col_num())
                    
                elif plant_type == SnowPeaShooter.NAME:
                    new_plant = SnowPeaShooter(tile.get_x_center(), tile.get_y_center(), self.maap, 
                                               self.time, tile.get_row_num(), tile.get_col_num())

                elif plant_type == Sibzamini.NAME:
                    new_plant = Sibzamini(tile.get_x_center(), tile.get_y_center(), self.maap, 
                                          self.time, tile.get_row_num(), tile.get_col_num())

                elif plant_type == Sunflower.NAME:
                    new_plant = Sunflower(tile.get_x_center(), tile.get_y_center(), self.maap, 
                                          self.time, tile.get_row_num(), tile.get_col_num())

        self.maap.add_plant(new_plant, tile)
            

    def increment_nums_of_sun(self):
        self.nums_of_sun += 1

    def run_game(self, event):
        pass

