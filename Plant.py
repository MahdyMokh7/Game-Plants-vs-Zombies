import os
from abc import ABC, abstractmethod  
from Consts import *
import pygame
from typing import override
from BulletObject import Pea, SnowPea, Bullet
from Time import Time
from Map import Map
from OtherItem import Sun


class Plant(ABC): 

    def __init__(self, health, cool_down, price, x_pos, y_pos, maap: Map, time: Time, row_num, col_num):  
        self.health = health  
        self.cool_down = cool_down  
        self.price = price  
        self.x_pos = x_pos  
        self.y_pos = y_pos  
        self.row_num = row_num
        self.col_num = col_num
        self.time = time  
        self.maap = maap


    @staticmethod
    def get_image_by_type(plant_type):
        if PeaShooter.NAME == plant_type:
            return PeaShooter.image
        
        elif SnowPeaShooter.NAME == plant_type:
            return SnowPeaShooter.image
        
        elif Sibzamini.NAME == plant_type:
            return Sibzamini.image

        elif Sunflower.NAME == plant_type:
            return Sunflower.image
        return None

    
    def get_row_num(self):
        return self.row_num
    
    def get_col_num(self):
        return self.col_num
    
    @abstractmethod
    def show_plant(self):
        pass

    def is_alive(self):  
        return self.health != 0  

    @abstractmethod  
    def got_hit(self):  
        pass  

    def get_x_pos(self):
        return self.x_pos
    
    def get_y_pos(self):
        return self.y_pos
    
    @abstractmethod
    def get_rect(self):  
        pass

    def got_hit(self, damage):
        self.health -= damage

    @abstractmethod
    def render(self):
        pass


class AttackerPlant(Plant):  
    def __init__(self, health, cool_down, price, damage, hit_rate, speed, x_pos, y_pos, maap, time, row_num, col_num):  
        super().__init__(health, cool_down, price, x_pos, y_pos, maap, time, row_num, col_num)  
        self.damage = damage  
        self.hit_rate = hit_rate  
        self.speed = speed  
        self.attack = False  
        self.last_shot_time = 0 
        self.shot_freq = hit_rate  # hit rate is estimated in seconds but something stings here

    def is_time_to_shoot(self):
        return self.time.get_current_time() - self.last_shot_time >= self.shot_freq

    @abstractmethod
    def show_plant(self):
        pass
        
    def make_bullet(self):  
        self.last_shot_time = self.time.get_current_time()
        
   
    @abstractmethod
    def get_rect(self):  
        pass

    @abstractmethod
    def render(self):
        pass

class ProviderPlant(Plant):  
    def __init__(self, health, cool_down, price, hit_rate, x_pos, y_pos, maap, time, row_num, col_num):  
        super().__init__(health, cool_down, price, x_pos, y_pos, maap, time, row_num, col_num)  
        self.hit_rate = hit_rate  
        self.provide_freq = hit_rate  ####### hit rate is estimated in seconds but something stings here
        self.last_production_time = 0  # Initialize if needed  

    def is_time_to_provide(self):  
        return self.time.get_current_time() - self.last_production_time >= self.provide_freq

    @abstractmethod
    def show_plant(self):
        pass

    def update_last_production_time(self):  
        self.last_production_time = self.time.get_current_time()

    @abstractmethod
    def get_rect(self):  
        pass

    @abstractmethod
    def render(self):
        pass


class DefenderPlant(Plant):  
    def __init__(self, health, cool_down, price, x_pos, y_pos, maap, time, row_num, col_num):  
        super().__init__(health, cool_down, price, x_pos, y_pos, maap, time, row_num, col_num)  

    @abstractmethod
    def show_plant(self):
        pass

    @abstractmethod
    def get_rect(self):  
        pass

    @abstractmethod
    def render(self):
        pass


class OtherPlant(Plant):  
    def __init__(self, health, cool_down, price, x_pos, y_pos, maap, time, row_num, col_num):  
        super().__init__(health, cool_down, price, x_pos, y_pos, maap, time, row_num, col_num)  

    @abstractmethod
    def show_plant(self):
        pass

    @abstractmethod
    def get_rect(self):  
        pass

    @abstractmethod
    def render(self):
        pass


# Subclass for AttackerPlant  
class PeaShooter(AttackerPlant):  

    IMAGE_PATH = os.path.join("Image files", "pea shooter.png")
    image = pygame.image.load(IMAGE_PATH)
    NAME = "PeaShooter"
    last_time_selected = 0

    @staticmethod
    def is_available():
        return Time.get_global_time() - PeaShooter.last_time_selected >= PEA_SHOOTER_COOL_DOWN

    def __init__(self, x_pos, y_pos, maap, time, row_num, col_num):  
        super().__init__(PEA_SHOOTER_HEALTH, PEA_SHOOTER_COOL_DOWN, PEA_SHOOTER_PRICE, 
                         PEA_SHOOTER_DAMAGE, PEA_SHOOTER_HIT_RATE, PEA_SHOOTER_SPEED, 
                         x_pos, y_pos, maap, time, row_num, col_num)
        self.image = None

    def show_plant(self):
        pass

    @override
    def make_bullet(self) -> Bullet:  
        super().make_bullet()
        new_bullet = Pea(Pea.SPEED, self.time, self.maap, self.x_pos, self.y_pos, self.row_num , self.damage)
        return new_bullet
    
    def get_type(self):  
        print("m") 


    def get_type(self) -> str:
        return PeaShooter.NAME
    
    def get_rect(self):  
        return PeaShooter.image.get_rect()
    
    def got_hit(self, damage):
        super().got_hit(damage)
        ##############  
        if not self.is_alive(self):
            self.plant_died_handle()##############
    
    def plant_died_handle(self):
        ################
        # remove from list plant in map
        
        self.maap.remove_plant(self , self.row_num)

    def render(self):
        return "render"


class SnowPeaShooter(AttackerPlant):  

    IMAGE_PATH = os.path.join("Image files", "snow pea shooter.png")
    image = pygame.image.load(IMAGE_PATH)
    NAME = "SnowPeaShooter"
    last_time_selected = 0

    @staticmethod
    def is_available():
        return Time.get_global_time() - PeaShooter.last_time_selected >= SNOW_PEA_SHOOTER_COOL_DOWN

    def __init__(self, x_pos, y_pos, map, time, row_num, col_num):  
        super().__init__(SNOW_PEA_SHOOTER_HEALTH, SNOW_PEA_SHOOTER_COOL_DOWN, SNOW_PEA_SHOOTER_PRICE,
                          SNOW_PEA_SHOOTER_DAMAGE, SNOW_PEA_SHOOTER_HIT_RATE, SNOW_PEA_SHOOTER_SPEED,
                            x_pos, y_pos, map, time, row_num, col_num)  

    def make_bullet(self, x_pos, y_pos, row_num):  
        super().make_bullet()
        new_bullet = SnowPea(SnowPea.SPEED, self.time, self.maap, x_pos, y_pos, row_num , self.damage)
        return new_bullet
    

    def get_type(self) -> str:
        return SnowPeaShooter.NAME
    
    def get_rect(self):  
        return SnowPeaShooter.image.get_rect()
    
    def got_hit(self, damage):
        super().got_hit(damage)
        ##############  
        if not self.is_alive(self):
            self.plant_died_handle()##############

    def render(self):
        return "render"
    
    def plant_died_handle(self):
        ################
        # remove from list plant in map
        
        self.maap.remove_plant(self , self.row_num)

    
class Sunflower(ProviderPlant):  

    IMAGE_PATH = os.path.join("Image files", "sun flower.png")
    image = pygame.image.load(IMAGE_PATH)
    NAME = "SunFlower"
    last_time_selected = 0

    @staticmethod
    def is_available():
        return Time.get_global_time() - PeaShooter.last_time_selected >= SUN_FLOWER_COOL_DOWN

    def __init__(self, x_pos, y_pos, maap, time, row_num, col_num):  
        super().__init__(SUN_FLOWER_HEALTH, SUN_FLOWER_COOL_DOWN, SUN_FLOWER_PRICE, 
                         SUN_FLOWER_HIT_RATE, x_pos, y_pos, maap, time, row_num, col_num)  

    def make_sun(self):  
        super().update_last_production_time()
        new_sun = Sun(self.time, self.maap, 0, self.x_pos, self.y_pos)
        return new_sun

    def get_type(self) -> str:
        return Sunflower.NAME
    
    def get_rect(self):  
        return Sunflower.image.get_rect()

    def got_hit(self, damage):
        super().got_hit(damage)
        ##############  
        if not self.is_alive(self):
            self.plant_died_handle()##############
    
    def plant_died_handle(self):
        ################
        # remove from list plant in map
        
        self.maap.remove_plant(self , self.row_num)

    def render(self):
        return "render"

class Sibzamini(DefenderPlant):  

    IMAGE_PATH = os.path.join("Image file", "sib zamini.png")
    image = pygame.image.load(IMAGE_PATH)
    NAME = "Sibzamini"
    last_time_selected = 0

    @staticmethod
    def is_available():
        return Time.get_global_time() - PeaShooter.last_time_selected >= SIB_ZAMINI_COOL_DOWN

    def __init__(self, x_pos, y_pos, maap, time, row_num, col_num):  
        super().__init__(SIB_ZAMINI_HEALTH, SIB_ZAMINI_COOL_DOWN, SIB_ZAMINI_PRICE, 
                         x_pos, y_pos, maap, time, row_num, col_num)

    def get_type(self) -> str:
        return Sibzamini.NAME
    
    def got_hit(self, damage):
        super().got_hit(damage)
        ##############  
        if not self.is_alive(self):
            self.plant_died_handle()##############
    
    def plant_died_handle(self):
        ################
        # remove from list plant in map
        
        self.maap.remove_plant(self , self.row_num)

    def get_rect(self):  
        return Sibzamini.image.get_rect()
    
    def render(self):
        return "render"
    

if __name__ == "__main__":  
    #a=Plant()
    a = PeaShooter(1,3,4,10, 2, 4, 4, 6, 1, 0)
    print(a)