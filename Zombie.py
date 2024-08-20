from abc import ABC, abstractmethod  


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
    def hit(self):  
        pass  

class RegularZombie(Zombie):  
    def __init__(self, damage, health, hit_rate, speed, map_instance, time_instance):  
        super().__init__(damage, health, hit_rate, speed, map_instance, time_instance)  

    def hit(self):  
        # Implement the hit logic for RegularZombie  
        pass  

class GiantZombie(Zombie):  
    def __init__(self, damage, health, hit_rate, speed, map_instance, time_instance):  
        super().__init__(damage, health, hit_rate, speed, map_instance, time_instance)  

    def hit(self):  
        # Implement the hit logic for GiantZombie  
        pass