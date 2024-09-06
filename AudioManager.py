import pygame
import time
import os


### if the loads take much time optimize them to load only once but can be palyed multiple times

class AudioManager:
    VICTORY = "victory"
    DEFEAT = "defeat"
    IN_GAME = "in_game"
    SUN_PICKUP = "sun_pickup"
    EATING_PLANT = "eating_plant"
    LAYOUT_PAGE_MUSIC = "layout_page_music"

    NUMBER_OF_IN_GAME_MUSIC = 11

    VICTORY_AUDIO_PATH = os.path.join("Audio files", "plants-vs-zombies-victory-theme-made-with-Voicemod.mp3")
    DEFEAT_AUDIO_PATH = os.path.join("Audio files", "game-over-from-plants-vs-zombies-made-with-Voicemod.mp3")
    IN_GAME_AUDIO_PATH = os.path.join("Audio files", "Plants_vs_Zombies_Soundtrack_(Day_Stage).mp3")
    LAYOUT_PAGE_MUSIC_AUDIO_PATH = os.path.join("Audio files", "plants-vs-zombies-main-theme-made-with-Voicemod.mp3")
    SUN_PICKUP_EFFECT_PATH = os.path.join("Audio files", "plants-vs-zombies-sun-pickup.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "plants-vs-zombies-eating-sfx-made-with-Voicemod.mp3")

    IN_GAME_AUDIO_PATH_1 = os.path.join("Audio files", "Main Music 00.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "Main Music 01.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "Main Music 02.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "Main Music 04.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "Main Music 06.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "Main Music 07.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "Main Music 09.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "Main Music 10.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "Main Music 11.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "Main Music 12.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "puase.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "start-game-evil-laugh.mp3")
    EATING_PLANT_EFFECT_PATH = os.path.join("Audio files", "the-zombies-are-coming-sound-effect-made-with-Voicemod.mp3")


    @staticmethod
    def __process_background_music():
        for _ in range(AudioManager.NUMBER_OF_IN_GAME_MUSIC):


    def __init__(self):
        self.is_sound_enable = True
        self.already_playing = False  # New field to track if music is playing
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
            AudioManager.IN_GAME: AudioManager.IN_GAME_AUDIO_PATH,
            AudioManager.LAYOUT_PAGE_MUSIC: AudioManager.LAYOUT_PAGE_MUSIC_AUDIO_PATH
        }.get(music_type, None)

        if audio_file_path is None:
            print("ERROR: Not a Correct Music Type...")
            return

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
            AudioManager.EATING_PLANT: AudioManager.EATING_PLANT_EFFECT_PATH
        }.get(sound_effect_type, None)

        if sound_effect_path is None:
            print("ERROR: Not a Correct Sound Effect Type...")
            return

        try:
            sound = pygame.mixer.Sound(sound_effect_path)
            sound.play()
            print("Playing sound effect...")

        except pygame.error as e:
            print("Error playing the sound effect:", e)

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
