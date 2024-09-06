import pygame
import time
import os
import random


### if the loads take much time optimize them to load only once but can be palyed multiple times

class AudioManager:

    NUMBER_OF_IN_GAME_MUSIC = 11

    VICTORY = "victory"
    DEFEAT = "defeat"
    IN_GAME = "in_game"
    SUN_PICKUP = "sun_pickup"
    EATING_PLANT = "eating_plant"
    LAYOUT_PAGE_MUSIC = "layout_page_music"
    PAUSE = "puase"
    START_GAME = "start_game"
    ZOMBIES_COMING = "zombise coming"
    BULLET_HIT_ZOMBIE = "bullet_hit_zombie"
    PLACE_PLANT = "place_plant"
    IN_GAME_STARTED = "in_game_started"

    VICTORY_AUDIO_PATH = os.path.join("Audio files", "plants-vs-zombies-victory-theme-made-with-Voicemod.mp3")
    DEFEAT_AUDIO_PATH = os.path.join("Audio files", "game-over-from-plants-vs-zombies-made-with-Voicemod.mp3")
    LAYOUT_PAGE_MUSIC_AUDIO_PATH = os.path.join("Audio files", "plants-vs-zombies-main-theme-made-with-Voicemod.mp3")
    SUN_PICKUP_EFFECT_PATH = os.path.join("Audio files", "plants-vs-zombies-sun-pickup.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "plants-vs-zombies-eating-sfx-made-with-Voicemod.mp3")
    PAUSE_EFFECT_PATH = os.path.join("Audio files", "puase.mp3")
    START_GAME_EFFECT_PATH = os.path.join("Audio files", "start-game-evil-laugh.mp3")
    ZOMBIES_ARE_COMING_EFFECT_PATH = os.path.join("Audio files", "the-zombies-are-coming-sound-effect-made-with-Voicemod.mp3")
    BULLET_HIT_ZOMBIE_EFFECT_PATH = os.path.join("Audio files", "plants-vs-zombies-hit.mp3")
    PLACE_PLANT_EFFECT_PATH = os.path.join("Audio files", "plants-vs-zombies-planting-sound.mp3")
    IN_GAME_STARTED_EFFECT_PATH = os.path.join("Audio files", "plants-vs-zombies-ready-set-plant.mp3")


    @staticmethod
    def __process_background_music():
        temp = []
        for i in range(9):
            temp.append(os.path.join("Audio files", f"Main Music 0{i}.mp3"))

        return temp
    
    IN_GAME_AUDIO_PATHS = __process_background_music()


    def __init__(self):
        self.is_sound_enable = True
        self.already_playing = False  # New field to track if music is playing
        self.sound_got_played = False
        pygame.mixer.init()

    def play_pause_sound(self):
        if self.is_sound_enable:
            self.is_sound_enable = False
            pygame.mixer.music.pause()
            print("Audio muted.")
        else:
            self.is_sound_enable = True
            pygame.mixer.music.unpause()
            print("Audio unmuted.")

    def play_music(self, music_type, loop=True):  # if the loop is True it will loop indefinitely

        # dont run the function if it is mute
        if not self.is_sound_enable:
            return

        # dont run the function if a music is already playing
        if self.already_playing:
            return 
        else:
            self.already_playing = True

        audio_file_path = {
            AudioManager.VICTORY: AudioManager.VICTORY_AUDIO_PATH,
            AudioManager.DEFEAT: AudioManager.DEFEAT_AUDIO_PATH,
            AudioManager.IN_GAME: AudioManager.IN_GAME_AUDIO_PATHS,
            AudioManager.LAYOUT_PAGE_MUSIC: AudioManager.LAYOUT_PAGE_MUSIC_AUDIO_PATH
        }.get(music_type, None)

        if audio_file_path is None:
            print("ERROR: Not a Correct Music Type...")
            return
            
        if isinstance(audio_file_path, list):
            audio_file_path = random.choice(audio_file_path)

        try:
            pygame.mixer.music.load(audio_file_path)
            pygame.mixer.music.play(-1 if loop else 0)  # Loop indefinitely if loop is True
            self.already_playing = True  # Set to True when music starts playing
            print("Playing background music...")

        except pygame.error as e:
            print("Error playing the audio file:", e)

    def play_sound_effect(self, sound_effect_type):
        if not self.is_sound_enable:
            return

        sound_effect_path = {
            AudioManager.SUN_PICKUP: AudioManager.SUN_PICKUP_EFFECT_PATH,
            AudioManager.EATING_PLANT: AudioManager.EATING_PLANT_EFFECT_PATH,
            AudioManager.PAUSE: AudioManager.PAUSE_EFFECT_PATH,
            AudioManager.START_GAME: AudioManager.START_GAME_EFFECT_PATH,
            AudioManager.ZOMBIES_COMING: AudioManager.ZOMBIES_ARE_COMING_EFFECT_PATH,
            AudioManager.BULLET_HIT_ZOMBIE: AudioManager.BULLET_HIT_ZOMBIE_EFFECT_PATH,
            AudioManager.PLACE_PLANT: AudioManager.PLACE_PLANT_EFFECT_PATH,
            AudioManager.IN_GAME_STARTED: AudioManager.IN_GAME_STARTED_EFFECT_PATH
        }.get(sound_effect_type, None)

        if sound_effect_path is None:
            print("ERROR: Not a Correct Sound Effect Type...")
            return

        try:
            sound = pygame.mixer.Sound(sound_effect_path)
            
            # Check if the sound is already playing
            if sound.get_num_channels() > 0:
                print(f"{sound_effect_type} sound is already playing.")
                return

            sound.play()
            print("Playing sound effect...")

        except pygame.error as e:
            print("Error playing the sound effect:", e)

    def play_music_and_wait(self, music_type):  
        """Play a given music track and wait until it finishes before continuing."""

        audio_file_path = {
            AudioManager.START_GAME: AudioManager.START_GAME_EFFECT_PATH
        }.get(music_type, None)

        if audio_file_path is None:
            print("ERROR: Not a Correct Music Type...")
            return

        try:
            # Load and play the selected music file
            pygame.mixer.music.load(audio_file_path)
            pygame.mixer.music.play(0)  # Play once (no loop)
            print("Playing music of start game and waiting for it to finish...")

            # Wait until the music finishes playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)  # Wait 10ms and check again

            print("Music finished. Continuing program...")

        except pygame.error as e:
            print("Error playing the audio file:", e)


    def stop_music(self):
        """Stop the currently playing music."""
        pygame.mixer.music.stop()
        self.already_playing = False
        print("Music stopped.")

# Example usage
if __name__ == "__main__":
    audio_manager = AudioManager()
    audio_manager.play_music(AudioManager.IN_GAME, loop=True)  # Play in-game music in a loop
    time.sleep(6)
    audio_manager.stop_music()

    audio_manager.play_music(AudioManager.LAYOUT_PAGE_MUSIC, loop=True)  # Play layout-page music in a loop
    time.sleep(5)
    audio_manager.play_pause_sound()
    time.sleep(5)
    audio_manager.play_pause_sound()
    time.sleep(2)

    # Play a sound effect while the music is still playing
    audio_manager.play_sound_effect(AudioManager.SUN_PICKUP)

    print("Music and sound effects are playing in the background.")
    
    # Simulating other tasks
    for i in range(5):
        print(f"Doing something else... {i + 1}")
        time.sleep(1)  # Simulate some work being done
