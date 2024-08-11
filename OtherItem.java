abstract public class OtherItem {  
    protected int speed;  
    protected int interval;  
    private final Time time;
    private final Map map;
    
    public OtherItem(int speed, int interval , Time time , Map map) {  
        this.time = time;
        this.map = map;
        this.speed = speed;  
        this.interval = interval;  
     
    }  
} 
/////////////////////////////////////////////////////////////////
class Sun extends OtherItem {  
    
    public Sun(int speed, int interval) {  
        super(speed, interval);   
    }  
    
}