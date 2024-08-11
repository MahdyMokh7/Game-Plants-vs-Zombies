abstract public class BulletObject {  
    private int speed;
    private final Time time;
    private final Map map;


    public BulletObject(Map map , Time time ,int speed) {  
        this.time = time;
        this.map = map;
        this.speed = 2; //?

     
    } 

    public void throw() {   //should overright
           
    }  

    public void calc_momentary_position() {  
        
    }  

    public int what_row_are_we_in() {  
        
    }  
    
} 
