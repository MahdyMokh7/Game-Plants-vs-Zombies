import os
from abc import ABC
from abc import ABC, abstractmethod  
from Consts import *
import pygame


class OtherItem(ABC):

    def __init__(self, speed, interval, time, map):
        self.speed = speed
        self.interval = interval
        self.time = time  # Assuming Time is defined elsewhere
        self.map = map    # Assuming Map is defined elsewhere

    @abstractmethod
    def show_plant(self):
        pass


class Sun(OtherItem):

    SUN_PATH = os.path.join("Image files", "sun.png")
    image = pygame.image.load(SUN_PATH)

    def __init__(self, SPEED, INTERVAL, time, map):
        super().__init__(SPEED, INTERVAL, time, map)
      

    def show_plant(self):
        pass
