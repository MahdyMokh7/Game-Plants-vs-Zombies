//package game;


abstract public class Zombie {  
    protected int damage; 
    protected int health;  
    protected int hit_rate;  
    protected int speed;  
    private final Time time;
    private final Map map;

    public Zombie(int damage, int health, int hit_rate, int speed) {  
        this.damage = damage;
        this.health = health;  
        this.hit_rate = hit_rate;  
        this.speed = speed;  
    }  

    public boolean is_still_alive() {  
        if(this.health == 0){
            return false;
        }
        return true;
    }  

    abstract public void hit();
    
}  

//////////////////////////////////////////////////////////////////////////////////////// 
class RegularZombie extends Zombie {  
    
    public RegularZombie(int damage, int health, int hit_rate, int speed) {  
        super(damage, health, hit_rate, speed);  
        
    }  

    @Override


}  

///////////////////////////////////////////////////////////////////////////////////
class GiantZombie extends Zombie {  
   
    public GiantZombie(int damage, int health, int hit_rate, int speed) {  
        super(damage, health, hit_rate, speed);  
        
    }  
    
    @Override

}  