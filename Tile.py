class Tile:  

    TILE_SIZE = (94, 110)     #static field 94x110

    def __init__(self, left_x, right_x, up_y, down_y, x_int, y_int):  
        self.left_x = left_x      
        self.right_x = right_x    
        self.up_y = up_y         
        self.down_y = down_y        
        self.x_of_center = None     
        self.y_of_center = None     
        self.row_position = None  
        self.calc_center_position()

        self.x_int = x_int
        self.y_int = y_int

        self.plant = None             # plant that place in this tile    
        self.is_empty = True   


    def calc_center_position(self):  
        self.x_of_center = (self.right_x + self.left_x) // 2        # its not 2!
        self.y_of_center = (self.up_y + self.down_y) // 2 
        self.row_position = self.y_of_center

    def set_plant(self, plant):  
        self.plant = plant  
        self.is_empty = False

    def is_tile_empty(self) -> bool:
        self.is_empty

    def set_is_empty(self, empty: bool):
        self.is_empty = empty
