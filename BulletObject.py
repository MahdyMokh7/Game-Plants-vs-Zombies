import os
from abc import ABC, abstractmethod
from typing import override
from Consts import SCALE
import pygame


class Bullet(ABC):

    def __init__(self, speed, time, maap, x_pos, y_pos, row_num , damage):
        self.speed = speed * SCALE
        self.time = time
        self.maap = maap
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.row_num = row_num
        self.damage = damage

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
    
    @abstractmethod
    def show_plant(self):
        pass
    
    @abstractmethod
    def hit(self):
        pass

    def get_damage(self):
        return self.damage
###################################################
class Pea(Bullet):
    
    IMAGE_PATH = os.path.join("Image files", "pea.png")
    SPEED = 7
    image = pygame.image.load(IMAGE_PATH)
    NAME = "Pea"

    def __init__(self, speed, time, maap, x_pos, y_pos, row_num, damage):
        super().__init__(speed, time, maap, x_pos, y_pos, row_num, damage)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")

    def show_plant(self):
        pass

    def hit(self , zombie):
        zombie.got_hit(self)

#####################################################
class SnowPea(Bullet):

    IMAGE_PATH = os.path.join("Image files", "snow pea.png")
    SPEED = 5
    image = pygame.image.load(IMAGE_PATH)
    NAME = "SnowPea"
    FREEZE_TIME = 5
    SPEED_ACCELERATE = 2

    def __init__(self, speed, time, maap, x_pos, y_pos, row_num, damage):
        super().__init__(speed, time, maap, x_pos, y_pos, row_num, damage)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")

    def show_plant(self):
        pass

    def hit(self , zombie):
        zombie.got_hit(self)

#####################################################
class WaterMelon(Bullet):
    NAME = "WaterMelon"
    def __init__(self, speed, time, maap, x_pos, y_pos, row_num, damage):
        super().__init__(speed, time, maap, x_pos, y_pos, row_num, damage)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")
