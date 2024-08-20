from abc import ABC


class OtherItem(ABC):
    def __init__(self, speed, interval, time, map):
        self.speed = speed
        self.interval = interval
        self.time = time  # Assuming Time is defined elsewhere
        self.map = map    # Assuming Map is defined elsewhere


class Sun(OtherItem):
    def __init__(self, speed, interval, time, map):
        super().__init__(speed, interval, time, map)
