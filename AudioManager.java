import java.io.File;
import java.io.IOException;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.UnsupportedAudioFileException;

class AudioManager{

    private static final String VICTORY = "victory";
    private static final String DEFEAT = "defeat";
    private static final String IN_GAME = "in_game";

    private static final String VICTORY_AUDIO_PATH = "Audio files/game-over-from-plants-vs-zombies-made-with-Voicemod.mp3";
    private static final String DEFEAT_AUDIO_PATH = "Audio files/game-over-from-plants-vs-zombies-made-with-Voicemod.mp3";
    private static final String IN_GAME_AUDIO_PATH = "Audio files/plants-vs-zombies-garden-warfare-1-main-theme-made-with-Voicemod.mp3";
    private boolean is_sound_enable;
    private final Time time;
    private final Map map;


    public AudioManager(Map map , Time time ) {  
        this.is_sound_enable = true;     
        this.map = map;
        this.time = time;
    } 

    public void mute_sound() {  
           
    }  

    public static void play_music(String music_type) {
        String audio_file_path = "";

        switch (music_type) {
            case AudioManager.DEFEAT:
                audio_file_path = AudioManager.DEFEAT_AUDIO_PATH;
                break;

            case AudioManager.VICTORY:
                audio_file_path = AudioManager.VICTORY_AUDIO_PATH;
                break;

            case AudioManager.IN_GAME:
                audio_file_path = AudioManager.IN_GAME_AUDIO_PATH;
                break;
        
            default:
                System.err.println("ERROR: Not a Correct Music Type...");
                break;
        }
        try {
            File audioFile = new File(audio_file_path);
            
            AudioInputStream audioStream = AudioSystem.getAudioInputStream(audioFile);
            
            Clip clip = AudioSystem.getClip();
            clip.open(audioStream);
            clip.start(); 
            
            System.out.println("Playing audio...");
            while (clip.isRunning()) {
                Thread.sleep(1000); // Sleep for a while to allow audio to play/////////////////////////////
            }
            
            // Close the clip and audio stream
            clip.close();
            audioStream.close();
        } catch (UnsupportedAudioFileException e) {
            System.err.println("The specified audio file is not supported.");
            e.printStackTrace();
        } catch (IOException e) {
            System.err.println("Error playing the audio file.");
            e.printStackTrace();
        } catch (LineUnavailableException e) {
            System.err.println("Audio line for playing back is unavailable.");
            e.printStackTrace();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

}

