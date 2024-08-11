import java.util.ArrayList;

class Bot {  
    private ArrayList<Zombie> types_of_zombies;
    private int total_attack_time;
    private int total_attack_remain_time;
    private int number_of_zombies_per_10_second;
    private int how_often_is_sun_produce;
    private final Time time;
    private final Map map;


    public Bot() {  
        this.types_of_zombies = new ArrayList<>();
        this.total_attack_time = 0;
        this.total_attack_remain_time = 100; /////?
        this.number_of_zombies_per_10_second = 1; /////?
        this.how_often_is_sun_produce = 5; ///?
        this.time = new Time();
        this.map = new Map();
        
     
    } 

    public void calc_amaunt_of_increasment_number_of_zombies_per_10_second() {  
           
    }  

    public boolean is_time_to_create_zombie() {  
        
    } 

    public void crate_random_zombie() {  
        
    }  

    public void calc_position_of_created__zombie() {  
        
    }  

    public  boolean is_time_to_produce_sun() {  
        
    }  

    public void crate_sun() {  
        
    }  

    public void zombies_attack() {  
        
    }  

    public void run() {  
        
    } 

} 