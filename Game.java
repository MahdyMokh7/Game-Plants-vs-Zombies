import java.util.ArrayList;

class Game {  
    private ArrayList<User> users;
    private ArrayList<Bot> bots;
    private ArrayList<UI> uls;
    private final Time time;
    private final Map map;


    public Game() {  
        this.time = new Time();
        this.map = new Map();
        this.users = new ArrayList<>();
        this.bots = new ArrayList<>();
        this.uls = new ArrayList<>();
     
    } 

    public void handle_events() {  
           
    }  

    public void run() {  
        
    }  

    private void initialization() {  //ساخت تایم و مپ
        
    } 
    
} 