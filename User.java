import java.util.ArrayList;

class User {  
    private boolean is_brain_eaten;
    private int nums_of_sun;
    private final Time time;
    private final Map map;


    public User(Map map , Time time ) {  
        this.time = time;
        this.map = map;
        this.is_brain_eaten = false;
        this.nums_of_sun = 0;
     
    } 

    public void place_the_plant() {  
           
    }  

    public void increment_nums_of_sun() {  
        this.nums_of_sun++; 
    }  

    
    
} 