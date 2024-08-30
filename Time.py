import time
import datetime
import math


class Time:
    def __init__(self):
        self._start_time = None  # To store the start time
        self._elapsed_time = 0  # To store the accumulated elapsed time
        self._running = False   # Flag to check if the timer is running

    @staticmethod
    def get_global_time():
        return time.time()

    def start_time_counting(self):
        """Start counting time."""
        if not self._running:
            self._start_time = time.time()  # Record the start time
            self._running = True

    def finish_time(self):
        """Stop the timer and update the elapsed time."""
        if self._running:
            self._elapsed_time += time.time() - self._start_time  # Update the elapsed time
            self._running = False

    def get_current_time(self):
        """Return the current elapsed time in seconds, rounded down."""
        if self._running:
            # If the timer is running, return the sum of the elapsed time and the time since the last start, rounded down
            return math.floor(time.time() - self._start_time)
        else:
            return math.floor(self._elapsed_time)

if __name__ == "__main__":
    time.sleep(2)
    game_timer = Time()
    game_timer.start_time_counting()

    time.sleep(2)  # Simulate some gameplay time
    print(f"Elapsed Time: {game_timer.get_current_time()} seconds")

    time.sleep(3)  # Simulate more gameplay time
    print(f"Elapsed Time: {game_timer.get_current_time()} seconds")

    game_timer.finish_time()
    print(f"Final Elapsed Time: {game_timer.get_current_time()} seconds")
