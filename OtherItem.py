import os
from abc import ABC
from abc import ABC, abstractmethod  
from Consts import *
import pygame


class OtherItem(ABC):

    def __init__(self, time, maap, speed, ui):
        self.speed = speed
        self.time = time  
        self.maap = maap    
        self.ui = ui

    @abstractmethod
    def render(self):
        pass


class Sun(OtherItem):

    NAME = "Sun"
    SUN_SIZE = (50, 50)
    SUN_PATH = os.path.join("Image files", "sun.png")
    image = pygame.image.load(SUN_PATH)
    image = pygame.transform.scale(image, SUN_SIZE)

    def __init__(self, time, maap, sun_speed, x_pos, y_pos, ui):
        super().__init__(time, maap, sun_speed, ui)
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self):
        self.y_pos += self.speed

    def render(self):
        x = self.x_pos
        y = self.y_pos
        self.ui.draw_object(Sun.image, x, y)

