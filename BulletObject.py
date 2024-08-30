import os
from abc import ABC, abstractmethod
from typing import override
from Consts import SCALE
import pygame


class Bullet(ABC):

    def __init__(self, speed, time, maap, x_pos, y_pos, row_num , damage , ui):
        self.speed = speed * SCALE
        self.time = time
        self.maap = maap
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.row_num = row_num
        self.damage = damage
        self.ui = ui

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
    
    @abstractmethod
    def render(self):
        pass

###################################################
class Pea(Bullet):
    
    IMAGE_PATH = os.path.join("Image files", "pea.png")
    IMAGE_SIZE = (30, 30)
    SPEED = 7
    image = pygame.image.load(IMAGE_PATH)
    image = pygame.transform.scale(image, IMAGE_SIZE)
    NAME = "Pea"

    def __init__(self, speed, time, maap, x_pos, y_pos, row_num, damage, ui):
        super().__init__(speed, time, maap, x_pos, y_pos, row_num, damage, ui)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")

    def show_plant(self):
        pass

    def hit(self , zombie):
        zombie.got_hit(self)

    def render(self):
        x = self.x_pos - Pea.image.get_rect().width // 2
        y = self.y_pos - Pea.image.get_rect().height // 2
        self.ui.draw_object(Pea.image, x, y)

#####################################################
class SnowPea(Bullet):

    IMAGE_PATH = os.path.join("Image files", "snow pea.png")
    IMAGE_SIZE = (30, 30)
    SPEED = 5
    image = pygame.image.load(IMAGE_PATH)
    image = pygame.transform.scale(image, IMAGE_SIZE)
    NAME = "SnowPea"
    FREEZE_TIME = 5
    SPEED_ACCELERATE = 2

    def __init__(self, speed, time, maap, x_pos, y_pos, row_num, damage, ui):
        super().__init__(speed, time, maap, x_pos, y_pos, row_num, damage, ui)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")

    def show_plant(self):
        pass

    def hit(self , zombie):
        zombie.got_hit(self)

    def render(self):
        x = self.x_pos - SnowPea.image.get_rect().width // 2
        y = self.y_pos - SnowPea.image.get_rect().height // 2
        self.ui.draw_object(SnowPea.image, x, y)

#####################################################
class WaterMelon(Bullet):
    NAME = "WaterMelon"

    def __init__(self, speed, time, maap, x_pos, y_pos, row_num, damage, ui):
        super().__init__(speed, time, maap, x_pos, y_pos, row_num, damage, ui)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")

    def render(self):
        return "render"
