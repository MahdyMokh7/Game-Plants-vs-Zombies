abstract public class BulletObject {  
    private int speed;
    private final Time time;
    private final Map map;


    public BulletObject(Map map , Time time ,int speed) {  
        this.time = time;
        this.map = map;
        this.speed = speed;
     
    } 

    abstract public void run_shoot();

    public void calc_momentary_position() {  
        
    }  

    public int what_row_are_we_in() {  
        int row = -1;


        return row;
    }  
    
} 

//////////////////////////////////////////////////
public class Pee extends BulletObject {

    public Pee(Map map, Time time, int speed) {
        super(map, time, speed);
        //TODO Auto-generated constructor stub
    }

    @Override
    public void run_shoot() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'run_shoot'");
    }
    
}

public class SnowPee extends BulletObject {

    public SnowPee(Map map, Time time, int speed) {
        super(map, time, speed);
        //TODO Auto-generated constructor stub
    }

    @Override
    public void run_shoot() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'run_shoot'");
    }
    
}

public class WaterMelon extends BulletObject {

    public WaterMelon(Map map, Time time, int speed) {
        super(map, time, speed);
        //TODO Auto-generated constructor stub
    }

    @Override
    public void run_shoot() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'run_shoot'");
    }
    
}
