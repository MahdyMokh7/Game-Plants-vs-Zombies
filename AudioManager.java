class AudioManager{
    private static final String VICTORY_AUDIO_PATH = ;
    private static final String DEFEAT_AUDIO_PATH = ;
    private static final String IN_GAME_AUDIO_PATH = ;
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

}

