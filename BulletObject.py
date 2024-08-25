import os
from abc import ABC, abstractmethod
from typing import override
import pygame


class BulletObject(ABC):

    def __init__(self, time, speed, maap):
        self.speed = speed
        self.time = time
        self.maap = maap

    @abstractmethod
    def run_shoot(self):
        pass
    
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
    

###################################################
class Pee(BulletObject):
    
    PEA_IMAGE_PATH = os.path.join("Image files", "pea.png")
    image = pygame.image.load(PEA_IMAGE_PATH)

    def __init__(self, map, time, speed):
        super().__init__(map, time, speed)
        


    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")

    def show_plant(self):
        pass

#####################################################
class SnowPee(BulletObject):

    SNOW_PEA_IMAGE_PATH = os.path.join("Image files", "snow pea.png")
    image = pygame.image.load(SNOW_PEA_IMAGE_PATH)


    def __init__(self, map, time, speed):
        super().__init__(map, time, speed)
       


    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")

    def show_plant(self):
        pass

#####################################################
class WaterMelon(BulletObject):
    def __init__(self, map, time, speed):
        super().__init__(map, time, speed)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")
