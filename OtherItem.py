import os
from abc import ABC

SPEED = 10
INTERVAL = 10


class OtherItem(ABC):
    SUN_PATH = os.path.join("Image files/sun.png")

    def __init__(self, speed, interval, time, map):
        self.speed = speed
        self.interval = interval
        self.time = time  # Assuming Time is defined elsewhere
        self.map = map    # Assuming Map is defined elsewhere


class Sun(OtherItem):
    def __init__(self, SPEED, INTERVAL, time, map):
        super().__init__(SPEED, INTERVAL, time, map)
