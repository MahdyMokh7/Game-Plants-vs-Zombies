import random

class Bot:
    def __init__(self, maap, time):
        self.types_of_zombies = []  # List to hold types of zombies
        self.total_attack_time = 0
        self.total_attack_remain_time = 100  # Initial remaining attack time
        self.number_of_zombies_per_10_second = 1  # Initial zombies per 10 seconds
        self.how_often_is_sun_produce = 5  # Sun production frequency
        self.time = time
        self.maap = maap

    def calc_amount_of_increasment_number_of_zombies_per_10_second(self):
        # Logic to calculate the increase in number of zombies
        pass

    def is_time_to_create_zombie(self):
        ans = True
        # Logic to determine if it's time to create a zombie
        return ans

    def create_random_zombie(self):
        # Logic to create a random zombie
        pass

    def calc_position_of_created_zombie(self):
        # Logic to calculate the position of the created zombie
        pass

    def is_time_to_produce_sun(self):
        ans = True
        # Logic to determine if it's time to produce sun
        return ans

    def create_sun(self):
        # Logic to create sun
        pass

    def zombies_attack(self):
        # Logic for zombies to attack
        pass

    def run(self):
        # Main logic to run the bot
        pass
