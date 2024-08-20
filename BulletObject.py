from abc import ABC, abstractmethod
from typing import override


class BulletObject(ABC):
    def __init__(self, map, time, speed):
        self.speed = speed
        self.time = time
        self.maap = maap

    @abstractmethod
    def run_shoot(self):
        pass
    
    def calc_momentary_position(self):
        # Logic to calculate the momentary position
        pass

    def what_row_are_we_in(self):
        row = -1
        # Logic to determine the current row
        return row
    

###################################################
class Pee(BulletObject):
    def __init__(self, map, time, speed):
        super().__init__(map, time, speed)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")


#####################################################
class SnowPee(BulletObject):
    def __init__(self, map, time, speed):
        super().__init__(map, time, speed)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")


#####################################################
class WaterMelon(BulletObject):
    def __init__(self, map, time, speed):
        super().__init__(map, time, speed)

    @override
    def run_shoot(self):
        # Implementation for shooting logic
        raise NotImplementedError("Unimplemented method 'run_shoot'")
