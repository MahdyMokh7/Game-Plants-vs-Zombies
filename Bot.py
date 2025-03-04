import random
from Map import Map
from Time import Time
from Zombie import Zombie, RegularZombie, GiantZombie
from Consts import *
from OtherItem import Sun
from User import User
from Plant import *
from UI import UI
from AudioManager import AudioManager


class Bot:

    TOTAL_GAME_TIME = GAME_TIME_IN_SEC  # (sc)
    WON_STATE = "won" 
    LOST_STATE = "lost"
    IN_GAME_STATE = "in_game"

    def __init__(self, maap: Map, time: Time, ui: UI, audioManager: AudioManager):
        self.types_of_zombies = {
            RegularZombie.NAME: RegularZombie,
            GiantZombie.NAME: GiantZombie
        }  # Dictionary to hold types of zombies

        self.audioManager = audioManager

        self.weighted_zombie_list = self.__creat_weighted_zombie_list()
        self.total_attack_time = 0
        self.number_of_zombies_per_10_second = 3  # Initial zombies per 10 seconds
        self.number_of_zombies_added_per_10_second = 1  
        self.zombie_production_freq = DISTANCE_ZOMBIE_PLANT_EAT / self.number_of_zombies_per_10_second 
        self.sun_production_freq = SUN_INTERVAL  # Sun production frequency in (sec)
        self.time = time
        self.maap = maap
        self.start_game_time = 0
        self.last_sun_production_time = 0
        self.last_zombie_production_time = 0
        self.last_10sec_update_time = 0
        self.game_state = Bot.IN_GAME_STATE
        self.time_spent = self.time.get_current_time()
        self.ui = ui

        self.did_first_zombie_came = False
        self.did_game_start = False

    def upadate_zombie_produciton_freq(self):  # its called when the number of zombies get changed per 10 seconds
        self.zombie_production_freq = TIME_ZOMBIE_CREATION_UPDATE / self.number_of_zombies_per_10_second

    def update_number_of_zombies_per_second(self):
        if self.time.get_current_time() - self.last_10sec_update_time >= TIME_ZOMBIE_CREATION_UPDATE:
            self.last_10sec_update_time = self.time.get_current_time()
            self.number_of_zombies_per_10_second += self.number_of_zombies_added_per_10_second
            self.upadate_zombie_produciton_freq()


    def __creat_weighted_zombie_list(self):
        return [RegularZombie.NAME] * 3 +  [GiantZombie.NAME]
    
    def is_mouse_pos_in_any_sun(self, mouse_pos):
        for sun in self.maap.all_suns_1d:
            if sun.colide_with_mouse_click(mouse_pos):
                return True
        return False


    def calc_amount_of_increasment_number_of_zombies_per_10_second(self):
        # Logic to calculate the increase in number of zombies
        pass

    def is_time_to_produce_zombie(self):
        return self.time.get_current_time() - self.last_zombie_production_time >= self.zombie_production_freq

    def create_zombie(self): 
        try:
            if not self.did_first_zombie_came:
                self.audioManager.play_sound_effect(AudioManager.ZOMBIES_COMING)
                self.did_first_zombie_came = True
            row_num = self.create_random_position_for_zombie()
            new_zombie = self.create_random_zombie()(
                self.maap, self.time, Zombie.X_START_POS, DICT_ROW_Y_POS[row_num], row_num, self.ui)
            self.maap.add_zombie(zombie=new_zombie, row_num=row_num)
            self.last_zombie_production_time = self.time.get_current_time()

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
        new_sun = Sun(self.time, self.maap , SUN_SPEED, x_pos, 0, self.ui)      
        self.maap.add_sun(new_sun)

    def zombies_attack(self):
        # Logic for zombies to attack
        pass

    def move_all_zombies(self):
        for zombie_row in self.maap.all_zombies_2d:
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


    def collisions_zombie_with_plant(self):
        for row_num in range(Map.NUM_OF_ROWS):
            for zombie in self.maap.all_zombies_2d[row_num]:
                for plant in self.maap.all_plants_2d[row_num]:
                    if zombie.did_colide(plant):   ######################
                        zombie.stop_movement()   #####
                        if zombie.is_time_to_hit():
                            zombie.hit(plant)
                            self.audioManager.play_sound_effect(AudioManager.EATING_PLANT)
                        if not plant.is_alive():
                            print("plantttt has died")
                            zombie.start_movement()


    def collisions_bullet_with_zombie(self):
        for row_num in range(Map.NUM_OF_ROWS):
            for bullet in self.maap.all_bullets_2d[row_num]:
                for zombie in self.maap.all_zombies_2d[row_num]:
                    if bullet.did_colide(zombie):   ######################
                        print(zombie.health)
                        bullet.hit(zombie)
                        # self.audioManager.play_sound_effect(AudioManager.BULLET_HIT_ZOMBIE)
                        self.maap.remove_bullet(bullet, row_num)   #####
                        
    def update_all_zombies(self):   # returns the game state (1: still running 0: lost)
        for zombie_row in self.maap.all_zombies_2d:
            for zombie in zombie_row:
                zombie.update()
                if zombie.did_arrive_home():
                    self.game_state = Bot.LOST_STATE

    def get_game_state(self):
        if self.time.get_current_time() >= Bot.TOTAL_GAME_TIME:
            self.game_state = Bot.WON_STATE

        return self.game_state
    
    def render_all(self):
        for plant_row in self.maap.all_plants_2d:
            for plant in plant_row:
                plant.render()

        for zombie_row in self.maap.all_zombies_2d:
            for zombie in zombie_row:
                zombie.render()

        for bullet_row in self.maap.all_bullets_2d:
            for bullet in bullet_row:
                bullet.render()

        for sun in self.maap.all_suns_1d:    
            sun.render()
                    

    def print_all_debug(self):
        print("PLNATS PRINT:\n")
        for plant_row in self.maap.all_plants_2d:
            for plant in plant_row:
                print((plant.x_pos, plant.y_pos))
        print('---------------------------------\n')

        print("ZOMBIES PRINT:\n")
        for zombie_row in self.maap.all_zombies_2d:
            for zombie in zombie_row:
                print((zombie.x_pos, zombie.y_pos))
        print('---------------------------------\n')

        print("BULLETS PRINT:\n")
        for bullet_row in self.maap.all_bullets_2d:
            for bullet in bullet_row:
                print((bullet.x_pos, bullet.y_pos))
        print('---------------------------------\n')

        print("SUNS PRINT:\n")
        for sun in self.maap.all_suns_1d:
            print((sun.x_pos, sun.y_pos))
        print('---------------------------------\n')


    def run(self):  # runs the bot and returns the game state
        """
        if its time for creating zombie or sun then create (check the condition here)
        move all the zombies and suns available
        """
        if not self.did_game_start:
            self.audioManager.play_sound_effect(AudioManager.IN_GAME_STARTED)
            self.did_game_start = True


        if self.is_time_to_produce_sun():
            print("sun added")
            self.create_sun()
        if self.is_time_to_produce_zombie():
            print("zombie added")
            self.create_zombie()
        

        self.check_all_plants()
        self.move_all_suns()
        self.move_all_bullets()
        self.update_all_zombies()
        self.move_all_zombies()
        self.collisions_zombie_with_plant()
        self.collisions_bullet_with_zombie()

        self.render_all()
        return self.get_game_state()

