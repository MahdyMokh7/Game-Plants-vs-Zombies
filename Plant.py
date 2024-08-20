from abc import ABC, abstractmethod  


class Plant(ABC):  
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
    def __init__(self, health, cool_down, price, damage, hit_rate, speed, x_pos, y_pos, map_instance, time_instance):  
        super().__init__(health, cool_down, price, damage, hit_rate, speed, x_pos, y_pos, map_instance, time_instance)  

    def shoot(self):  
        # Implement shooting logic here  
        print("hi")
    
    def get_type(self):  
        print("m") 

    
    def got_hit(self):  
        print("dd") 


class SnowPeaShooter(AttackerPlant):  
    def __init__(self, health, cool_down, price, damage, hit_rate, speed, x_pos, y_pos, map_instance, time_instance):  
        super().__init__(health, cool_down, price, damage, hit_rate, speed, x_pos, y_pos, map_instance, time_instance)  

    def shoot(self):  
        # Implement shooting logic here  
        pass  


class Sunflower(ProviderPlant):  
    def __init__(self, health, cool_down, price, hit_rate, x_pos, y_pos, map_instance, time_instance):  
        super().__init__(health, cool_down, price, hit_rate, x_pos, y_pos, map_instance, time_instance)  

    def produce(self):  
        # Implement produce logic here  
        pass  


class Sibzamini(DefenderPlant):  
    def __init__(self, health, cool_down, price, x_pos, y_pos, map_instance, time_instance):  
        super().__init__(health, cool_down, price, x_pos, y_pos, map_instance, time_instance)

    

 

    

if __name__ == "__main__":  
    #a=Plant()
    a = PeaShooter(1,3,4,10, 2, 4, 4, 6, 1, 0)
    print(a)