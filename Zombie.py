import os
from abc import ABC, abstractmethod  
from Consts import *


class Zombie(ABC):  

    REGULAR_ZOMBIE_PATH = os.path.join("Image files/regular zombie.png")
    GIANT_ZOMBIE_PATH = os.path.join("Image files/giant zombie.png")

    def __init__(self, damage, health, hit_rate, speed, map, time):  
        self.damage = damage  
        self.health = health  
        self.hit_rate = hit_rate  
        self.speed = speed  
        self.time = time  
        self.map = map
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.row_num = row_num

    def is_still_alive(self):  
        return self.health != 0  
    
    @abstractmethod
    def show_plant(self):
        pass

    @abstractmethod  
    def hit(self):  
        pass
    
    def move(self):
        self.x_pos -= self.speed
        # did zombie approached any plant 
        # did zombie went to the house
        # if the zombie is still eating the plant dont move

    def is_eating(self):
        pass

    def did_bullet_hit(self, x_pos_bullet):
        return x_pos_bullet >= self.x_pos
    
    def bullet_hit(self, damage_caused):
        self.health -= damage_caused

    def is_alive(self):
        return self.health > 0
    
    def did_colide(self, plant):

        return plant.get_rect().colliderect(self.get_rect())  ######################x jeloye zambie manzor نرگس: اگر یکسان بودند ایکس ها، ترو میشود
                                  
    def get_rect(self):
        return self.rect   ######################
        

class RegularZombie(Zombie):  
    def __init__(self, REGULAR_ZOMBIE_DAMAGE, REGULAR_ZOMBIE_HEALTH, REGULAR_ZOMBIE_HIT_RATE, REGULAR_ZOMBIE_SPEED, map, time):  
        super().__init__(REGULAR_ZOMBIE_DAMAGE, REGULAR_ZOMBIE_HEALTH, REGULAR_ZOMBIE_HIT_RATE, REGULAR_ZOMBIE_SPEED, map, time)  

    def hit(self, plant):  
        ############
        plant.got_hit(self.damage)   ###########
        pass  

class GiantZombie(Zombie):  
    def __init__(self, GIANT_ZOMBIE_DAMAGE, GIANT_ZOMBIE_HEALTH, GIANT_ZOMBIE_HIT_RATE, GIANT_ZOMBIE_SPEED, map, time):  
        super().__init__(GIANT_ZOMBIE_DAMAGE, GIANT_ZOMBIE_HEALTH, GIANT_ZOMBIE_HIT_RATE, GIANT_ZOMBIE_SPEED, map, time)  

    def hit(self):  
        # Implement the hit logic for GiantZombie  
        pass