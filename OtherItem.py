import os
from abc import ABC
from Consts import *


class OtherItem(ABC):

    def __init__(self, time, maap, speed):
        self.speed = speed
        self.time = time  
        self.maap = maap    


class Sun(OtherItem):

    SUN_PATH = os.path.join("Image files", "sun.png")

    def __init__(self, time, maap, sun_speed, x_pos, y_pos):
        super().__init__(time, maap, sun_speed)
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self):
        self.y_pos += self.speed

