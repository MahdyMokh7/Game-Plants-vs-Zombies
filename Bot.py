import random
from Map import Map
from Time import Time
from Zombie import Zombie, RegularZombie, GiantZombie
from Consts import *
from OtherItem import Sun
from User import User
from Plant import *


class Bot:
    def __init__(self, maap: Map, time: Time):
        self.types_of_zombies = {
            RegularZombie.NAME: RegularZombie,
            GiantZombie.NAME: GiantZombie
        }  # Dictionary to hold types of zombies

        self.user = User()

        self.weighted_zombie_list = self.__creat_weighted_zombie_list()
        self.total_attack_time = 0
        self.number_of_zombies_per_10_second = 3  # Initial zombies per 10 seconds
        self.number_of_zombies_added_per_10_second = 1  
        self.zombie_production_freq = 10 / self.number_of_zombies_per_10_second 
        self.sun_production_freq = 5  # Sun production frequency in (sec)
        self.time = time
        self.maap = maap
        self.start_game_time = 0
        self.last_sun_production_time = 0
        self.last_zombie_production_time = 0
        self.last_10sec_update_time = 0

    def upadate_zombie_produciton_freq(self):  # its called when the number of zombies get changed per 10 seconds
        self.zombie_production_freq = 10 / self.number_of_zombies_per_10_second

    def update_number_of_zombies_per_second(self):
        if self.time.get_current_time() - self.last_10sec_update_time >= 10:
            self.last_10sec_update_time = self.time.get_current_time()
            self.number_of_zombies_per_10_second += self.number_of_zombies_added_per_10_second
            self.upadate_zombie_produciton_freq()


    def __creat_weighted_zombie_list(self):
        return [RegularZombie.NAME * 3 +  GiantZombie.NAME]

    def calc_amount_of_increasment_number_of_zombies_per_10_second(self):
        # Logic to calculate the increase in number of zombies
        pass

    def is_time_to_produce_zombie(self):
        ans = True
        # Logic to determine if it's time to create a zombie
        return ans

    def create_zombie(self):
        try: 
            row_num = self.create_random_position_for_zombie()
            new_zombie = self.create_random_zombie()(
                self.maap, self.time, Zombie.X_START_POS, DICT_ROW_Y_POS[row_num], row_num)
            self.maap.add_zombie(zombie=new_zombie, row_num=row_num)
        except Exception as e:
            print(e)
            print("ERROR:  Could not create random zombie")
            exit()

        
    def create_random_zombie(self):
        zombie_name = random.choice(self.weighted_zombie_list)
        if zombie_name == RegularZombie.NAME:
            return RegularZombie
        elif zombie_name == GiantZombie.NAME:
            return GiantZombie
        else :
            return None

    def create_random_position_for_zombie(self) -> int:
        # Generate a random number between 0 and 4 (inclusive)
        return random.randint(0, 4)

    def calc_position_of_created_zombie(self):
        # Logic to calculate the position of the created zombie
        pass

    def is_time_to_produce_sun(self):
        return self.time.get_current_time() - self.last_sun_production_time >= self.sun_production_freq
    

    def create_random_x_in_map(self):
        return random.randint(Map.START_MAP_POS_X, Map.END_MAP_POS_X)

    def create_sun(self):
        self.last_sun_production_time = self.time.get_current_time()
        x_pos = self.create_random_x_in_map()
        new_sun = Sun(self.maap, self.time, x_pos, 0)
        self.maap.add_sun(new_sun)

    def zombies_attack(self):
        # Logic for zombies to attack
        pass

    def move_all_zombies(self):
        for zombie_row in self.map_all_zombies:
            for zombie in zombie_row:
                zombie.move()

    def move_all_suns(self):
        for sun in self.maap.all_suns_1d:
            sun.move()

    def in_game_running(self):
        return self.time.get_current_time() - self.start_game_time >= GAME_TIME_IN_SEC

    def initial_before_run(self):
        self.start_game_time = self.time.get_current_time()

    def move_all_bullets(self):
        for bullet_row in self.maap.all_bullets_2d:
            for bullet in bullet_row:
                bullet.move()

    def check_all_plants(self):
        for row_num, plant_row in enumerate(self.maap.all_plants_2d):
            for plant in plant_row:
                if isinstance(plant, AttackerPlant):
                    if plant.is_time_to_shoot():
                        new_bullet = plant.make_bullet()   # returns a bullet object
                        self.maap.add_bullet(new_bullet, row_num)

                elif isinstance(plant, ProviderPlant):
                    if plant.is_time_to_provide():
                        new_sun = plant.make_sun()
                        self.maap.add_sun(new_sun)


    def collision_zombie_with_plant(self):
        for row_num in range(Map.NUM_OF_ROWS):
            for zombie in self.maap.all_zombies_2d[row_num]:
                for plant in self.maap.all_plants_2d[row_num]:
                    if zombie.did_colide(plant):   ######################
                        zombie.stop_movement()   #####
                        zombie.hit(plant)
                        



    def collision_bullet_with_zombie(self):
        pass########################


    def run(self):
        """
        if its time for creating zombie or sun then create (check the condition here)
        move all the zombies and suns available
        
        
        """
        if self.is_time_to_produce_sun():
            self.create_sun()
        if self.is_time_to_produce_zombie():
            self.create_zombie()
        

        self.check_all_plants()
        self.move_all_zombies()
        self.move_all_suns()
        self.move_all_bullets()

        

