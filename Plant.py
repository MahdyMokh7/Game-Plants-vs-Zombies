import os
from abc import ABC, abstractmethod  

PEA_SHOOTER_DAMAGE = 5
SNOW_PEA_SHOOTER_DAMAGE = 8
SUN_FLOWER_DAMAGE = 0
SIB_ZAMINI_DAMAGE = 0


PEA_SHOOTER_HEALTH = 40
SNOW_PEA_SHOOTER_HEALTH = 30
SUN_FLOWER_HEALTHE = 30
SIB_ZAMINI_HEALTH = 200

PEA_SHOOTER_COOL_DOWN = 5
SNOW_PEA_SHOOTER_COOL_DOWN = 9
SUN_FLOWER_COOL_DOWN = 10
SIB_ZAMINI_COOL_DOWN = 10

PEA_SHOOTER_HIT_RATE = 5
SNOW_PEA_SHOOTER_HIT_RATE = 5
SUN_FLOWER_HIT_RATE = 12
SIB_ZAMINI_HIT_RATE = 0

PEA_SHOOTER_SPEED = 7
SNOW_PEA_SHOOTER_SPEED = 5
SUN_FLOWER_SPEED = 0
SIB_ZAMINI_SPEED = 0

PEA_SHOOTER_PRICE = 4
SNOW_PEA_SHOOTER_PRICE = 6
SUN_FLOWER_PRICE = 2
SIB_ZAMINI_PRICE = 2

class Plant(ABC):  
    
    PEA_SHOOTER_PATH = os.path.join("Image files/pea shooter.png")
    SNOW_PEA_SHOOTER_PATH = os.path.join("Image files/snow pea shooter.png")
    SUN_FLOWER_PATH = os.path.join("Image files/sun flower.png")
    SIB_ZAMINI_PATH = os.path.join("Image files/sib zamini.png")


    def __init__(self, health, cool_down, price, x_pos, y_pos, map, time):  
        self.health = health  
        self.cool_down = cool_down  
        self.price = price  
        self.x_position = x_pos  
        self.y_position = y_pos  
        self.time = time  
        self.map = map

    @abstractmethod  
    def get_type(self):  
        pass  

    def is_alive(self):  
        return self.health != 0  

    @abstractmethod  
    def got_hit(self):  
        pass  


class AttackerPlant(Plant):  
    def __init__(self, health, cool_down, price, damage, hit_rate, speed, x_pos, y_pos, map_instance, time_instance):  
        super().__init__(health, cool_down, price, x_pos, y_pos, map_instance, time_instance)  
        self.damage = damage  
        self.hit_rate = hit_rate  
        self.speed = speed  
        self.attack = False  

    def should_plant_shoot(self):  
        pass  

    @abstractmethod  
    def shoot(self):  
        pass  

    @abstractmethod  
    def get_type(self):  
        pass  

    @abstractmethod  
    def got_hit(self):  
        pass  

class ProviderPlant(Plant):  
    def __init__(self, health, cool_down, price, hit_rate, x_pos, y_pos, map_instance, time_instance):  
        super().__init__(health, cool_down, price, x_pos, y_pos, map_instance, time_instance)  
        self.hit_rate = hit_rate  
        self.production_time_left = 0  # Initialize if needed  

    def is_time_to_produce(self):  
        pass  

    @abstractmethod  
    def produce(self):  
        pass  


class DefenderPlant(Plant):  
    def __init__(self, health, cool_down, price, x_pos, y_pos, map_instance, time_instance):  
        super().__init__(health, cool_down, price, x_pos, y_pos, map_instance, time_instance)  


class OtherPlant(Plant):  
    def __init__(self, health, cool_down, price, x_pos, y_pos, map_instance, time_instance):  
        super().__init__(health, cool_down, price, x_pos, y_pos, map_instance, time_instance)  


# Subclass for AttackerPlant  
class PeaShooter(AttackerPlant):  
    def __init__(self, PEA_SHOOTER_HEALTH, PEA_SHOOTER_COOL_DOWN, PEA_SHOOTER_PRICE, PEA_SHOOTER_DAMAGE, PEA_SHOOTER_HIT_RATE, PEA_SHOOTER_SPEED, x_pos, y_pos, map, time):  
        super().__init__(PEA_SHOOTER_HEALTH, PEA_SHOOTER_COOL_DOWN, PEA_SHOOTER_PRICE, PEA_SHOOTER_DAMAGE, PEA_SHOOTER_HIT_RATE, PEA_SHOOTER_SPEED, x_pos, y_pos, map, time)  

    def shoot(self):  
        # Implement shooting logic here  
        print("hi")
    
    def get_type(self):  
        print("m") 

    
    def got_hit(self):  
        print("dd") 


class SnowPeaShooter(AttackerPlant):  
    def __init__(self, SNOW_PEA_SHOOTER_HEALTH, SNOW_PEA_SHOOTER_COOL_DOWN, SNOW_PEA_SHOOTER_PRICE, SNOW_PEA_SHOOTER_DAMAGE, SNOW_PEA_SHOOTER_HIT_RATE, SNOW_PEA_SHOOTER_SPEED, x_pos, y_pos, map, time):  
        super().__init__(SNOW_PEA_SHOOTER_HEALTH, SNOW_PEA_SHOOTER_COOL_DOWN, SNOW_PEA_SHOOTER_PRICE, SNOW_PEA_SHOOTER_DAMAGE, SNOW_PEA_SHOOTER_HIT_RATE, SNOW_PEA_SHOOTER_SPEED, x_pos, y_pos, map, time)  

    def shoot(self):  
        # Implement shooting logic here  
        pass  

    def get_type(self):  
        print("m") 

    
    def got_hit(self):  
        print("dd") 

class Sunflower(ProviderPlant):  
    def __init__(self, SUN_FLOWER_HEALTH, SUN_FLOWER_COOL_DOWN, SUN_FLOWER_PRICE, SUN_FLOWER_HIT_RATE, x_pos, y_pos, map, time):  
        super().__init__(SUN_FLOWER_HEALTH, SUN_FLOWER_COOL_DOWN, SUN_FLOWER_PRICE, SUN_FLOWER_HIT_RATE, x_pos, y_pos, map, time)  

    def produce(self):  
        # Implement produce logic here  
        pass  


class Sibzamini(DefenderPlant):  
    def __init__(self, SIB_ZAMINI_HEALTH, SIB_ZAMINI_COOL_DOWN, SIB_ZAMINI_PRICE, x_pos, y_pos, map, time):  
        super().__init__(SIB_ZAMINI_HEALTH, SIB_ZAMINI_COOL_DOWN, SIB_ZAMINI_PRICE, x_pos, y_pos, map, time)

    

 

    

if __name__ == "__main__":  
    #a=Plant()
    a = PeaShooter(1,3,4,10, 2, 4, 4, 6, 1, 0)
    print(a)