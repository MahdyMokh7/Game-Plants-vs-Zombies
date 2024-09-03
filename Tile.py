class Tile:  

    TILE_SIZE = (94, 110)     # static field 94x110

    def __init__(self, left_x, right_x, up_y, down_y, row_num, col_num):  
        self.left_x = left_x      
        self.right_x = right_x    
        self.up_y = up_y         
        self.down_y = down_y          
        self.row_position = None  
        self.x_of_center, self.y_of_center = self.calc_center_position()

        self.row_num = row_num
        self.col_num = col_num

        self.plant = None             # plant that place in this tile    
        self.is_empty = True   


    def calc_center_position(self):  
        return (self.right_x + self.left_x) // 2, (self.up_y + self.down_y) // 2 

    def set_plant(self, plant):  
        self.plant = plant  
        self.is_empty = False

    def is_tile_empty(self) -> bool:
        return self.is_empty

    def set_is_empty(self, empty: bool):
        self.is_empty = empty

    def is_position_in_this_tile(self, x_pos, y_pos):
        return (self.left_x <= x_pos <= self.right_x) and (self.up_y <= y_pos <= self.down_y)
    
    def remove_plant(self):
        self.plant = None
        self.set_is_empty(True)

    def add_plant(self, plant):
        self.plant = plant
        self.set_is_empty(False)

    def get_row_num(self):
        return self.row_num
    
    def get_col_num(self):
        return self.col_num
    
    def get_x_center(self):
        return self.x_of_center
    
    def get_y_center(self):
        return self.y_of_center

