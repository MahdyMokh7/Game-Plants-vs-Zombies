import os
from abc import ABC, abstractmethod
from typing import override
from Consts import SCALE


class Bullet(ABC):

    def __init__(self, speed, time, maap, x_pos, y_pos, row_num):
        self.speed = speed * SCALE
        self.time = time
        self.maap = maap
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.row_num = row_num

    def run_shoot(self):
        self.move()


    def __did_it_hit(self) -> bool:
        self.maap.did_bullet_hit_in_this_pos(self.x_pos, self.row_num)

    def move(self):
        self.x_pos += self.speed
    
    def calc_momentary_position(self):
        # Logic to calculate the momentary position
        pass

    def what_row_are_we_in(self):
        row = -1
        # Logic to determine the current row
        return row
    

###################################################
class Pea(Bullet):
    
    IMAGE_PATH = os.path.join("Image files", "pea.png")
    SPEED = 7

    def __init__(self, speed, time, maap, x_pos, y_pos, row_num):
        super().__init__(speed, time, maap, x_pos, y_pos, row_num)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")


#####################################################
class SnowPea(Bullet):

    IMAGE_PATH = os.path.join("Image files", "snow pea.png")
    SPEED = 5

    def __init__(self, speed, time, maap, x_pos, y_pos, row_num):
        super().__init__(speed, time, maap, x_pos, y_pos, row_num)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")


#####################################################
class WaterMelon(Bullet):
    def __init__(self, speed, time, maap, x_pos, y_pos, row_num):
        super().__init__(speed, time, maap, x_pos, y_pos, row_num)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")
