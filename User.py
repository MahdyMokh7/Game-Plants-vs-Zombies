class User:
    def __init__(self, maap, time):
        self.is_brain_eaten = False
        self.nums_of_sun = 0
        self.time = time
        self.maap = maap

    def place_the_plant(self):
        # Implementation for placing the plant goes here
        pass

    def increment_nums_of_sun(self):
        self.nums_of_sun += 1
