import os
from abc import ABC, abstractmethod  
from Consts import *
import pygame



class Zombie(ABC):  
    
    def __init__(self, damage, health, hit_rate, speed, map, time):  
        self.damage = damage  
        self.health = health  
        self.hit_rate = hit_rate  
        self.speed = speed  
        self.time = time
        self.map = map

    def is_still_alive(self):  
        return self.health != 0  
    
    @abstractmethod
    def show_plant(self):
        pass

    @abstractmethod  
    def hit(self):  
        pass  

class RegularZombie(Zombie):  

    IMAGE_PATH = os.path.join("Image files", "regular zombie.png")
    image = pygame.image.load(IMAGE_PATH)

    def __init__(self, REGULAR_ZOMBIE_DAMAGE, REGULAR_ZOMBIE_HEALTH, REGULAR_ZOMBIE_HIT_RATE, REGULAR_ZOMBIE_SPEED, map, time):  
        super().__init__(REGULAR_ZOMBIE_DAMAGE, REGULAR_ZOMBIE_HEALTH, REGULAR_ZOMBIE_HIT_RATE, REGULAR_ZOMBIE_SPEED, map, time)  
       


    def hit(self):  
        # Implement the hit logic for RegularZombie  
        pass  
   
    def show_plant(self):
        pass



class GiantZombie(Zombie):  

    IMAGE_PATH = os.path.join("Image files", "giant zombie.png")
    image = pygame.image.load(IMAGE_PATH)

    def __init__(self, GIANT_ZOMBIE_DAMAGE, GIANT_ZOMBIE_HEALTH, GIANT_ZOMBIE_HIT_RATE, GIANT_ZOMBIE_SPEED, map, time):  
        super().__init__(GIANT_ZOMBIE_DAMAGE, GIANT_ZOMBIE_HEALTH, GIANT_ZOMBIE_HIT_RATE, GIANT_ZOMBIE_SPEED, map, time)  
       


    def hit(self):  
        # Implement the hit logic for GiantZombie  
        pass

    def show_plant(self):
        pass