import os
from abc import ABC, abstractmethod  
from Consts import *
import pygame
from BulletObject import *
from Map import Map


class Zombie(ABC):     ### i can make did_colide a method for Zombie (check self is the class you go in or the object that calls)

    REGULAR_ZOMBIE_PATH = os.path.join("Image files/regular zombie.png")
    GIANT_ZOMBIE_PATH = os.path.join("Image files/giant zombie.png")

    def __init__(self, damage, health, hit_rate, speed, map, time, x_pos, y_pos, row_num):  
        self.damage = damage  
        self.health = health  
        self.hit_rate = hit_rate  
        self.speed = speed  
        self.time = time  
        self.map = map
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.row_num = row_num
        self.is_moving = True
        self.last_time_hit_by_snow_pea = 0
        self.is_using_temp_speed = False

    def is_still_alive(self):  
        return self.health != 0  
    
    @abstractmethod
    def show_plant(self):
        pass

    @abstractmethod  
    def hit(self):  
        pass
    
    def move(self):
        if self.is_moving:
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
    
    @abstractmethod
    def did_colide(self, plant):
        pass 
                                  
    def get_rect(self):
        return self.rect   ######################
        

    def stop_movement(self):
        self.is_moving = False

    def start_movement(self):
        self.is_moving = True

    def got_hit(self, damage):
        self.health-=damage

    @abstractmethod
    def update(self):
        pass

    def did_arrive_home(self):
        if self.x_pos <= Map.START_MAP_POS_X:
            return True
        return False

class RegularZombie(Zombie):  

    NAME = "RegularZombie"
    IMAGE_PATH = os.path.join("Image files", "snow pea shooter.png")
    image = pygame.image.load(IMAGE_PATH)


    def __init__(self, REGULAR_ZOMBIE_DAMAGE, REGULAR_ZOMBIE_HEALTH, REGULAR_ZOMBIE_HIT_RATE, REGULAR_ZOMBIE_SPEED, map, time):  
        super().__init__(REGULAR_ZOMBIE_DAMAGE, REGULAR_ZOMBIE_HEALTH, REGULAR_ZOMBIE_HIT_RATE, REGULAR_ZOMBIE_SPEED, map, time)  

    def hit(self, plant):  
        ############
        plant.got_hit(self.damage)   ###########


    def get_rect(self):
        return RegularZombie.image.get_rect()

    def did_colide(self, plant):
        return plant.get_rect().colliderect(self.get_rect()) 

    def got_hit(self , damage):
        super().got_hit()
        if not self.is_alive(self):
            self.zombie_died_handle()##############
    
    def zombie_died_handle(self):
        ############
        self.maap.remove_zombie(self , self.row_num)



class GiantZombie(Zombie):  
    def __init__(self, GIANT_ZOMBIE_DAMAGE, GIANT_ZOMBIE_HEALTH, GIANT_ZOMBIE_HIT_RATE, GIANT_ZOMBIE_SPEED, map, time):  
        super().__init__(GIANT_ZOMBIE_DAMAGE, GIANT_ZOMBIE_HEALTH, GIANT_ZOMBIE_HIT_RATE, GIANT_ZOMBIE_SPEED, map, time)  

    def hit(self):  
        # Implement the hit logic for GiantZombie  
        pass

    def get_rect(self):
        return GiantZombie.image.get_rect()
    
    def did_colide(self, plant):
        return plant.get_rect().colliderect(self.get_rect()) 
    

    def got_hit(self , bullet):
        super().got_hit(bullet.get_damage())
        if bullet.NAME == SnowPea.NAME:
            if self.is_using_temp_speed == False:
                (self.speed) = (self.speed)//SnowPea.SPEED_ACCELERATE
              
            self.last_time_hit_by_snow_pea = self.time.get_current_time()

            
            


        if not self.is_alive():
            self.zombie_died_handle()##############
    
    def zombie_died_handle(self):
        ############
        self.maap.remove_zombie(self , self.row_num)

    def update(self):
        if self.is_using_temp_speed == True:
            if (self.time.get_current_time() - self.last_time_hit_by_snow_pea) >= SnowPea.FREEZE_TIME:
                self.is_using_temp_speed = False
                self.speed = self.speed * SnowPea.SPEED_ACCELERATE