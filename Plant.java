//package com;


abstract public class Plant {  
    protected int health;  
    protected int cool_down;  
    protected int price;  
    private final Time time;
    private final Map map;
    private final int x_position;
    private final int y_position;

    public Plant(int health, int cool_down, int price) {  
        this.health = health;  
        this.cool_down = cool_down;  
        this.price = price;  
    }  

    abstract public void get_type();

    public boolean is_alive() {  
        if(this.health == 0){
            return false;
        }
        return true;
    
    }  

    abstract public void got_hit();
    
}  

//////////////////////////////////////////////////////////////////////////////////////// 
abstract class AttackerPlant extends Plant {  
    protected int damage;  
    protected int hit_rate;  
    protected int speed;  
    protected boolean attack;  

    public AttackerPlant(int health, int cool_down, int price, int damage, int hit_rate, int speed) {  
        super(health, cool_down, price);  
        this.damage = damage;  
        this.hit_rate = hit_rate;  
        this.speed = speed;  
    }  

    private void should_plant_shoot() {  
        
    }  

    abstract public void shoot();
        //should override
    
}  

///////////////////////////////////////////////////////////////////////////////////
abstract class ProviderPlant extends Plant {  
    protected int hit_rate;
    protected int production_time_left;  


    public ProviderPlant(int health, int cool_down, int price, int hit_rate) {  
        super(health, cool_down, price);  
        this.hit_rate = hit_rate;  
    }  

    private boolean is_time_to_produce() {  
         
    }  

    abstract public void produce();
}  

////////////////////////////////////////////////////////////////////////////////////
abstract class DefenderPlant extends Plant {    

    public DefenderPlant(int health, int cool_down, int price) {  
        super(health, cool_down, price);  
    }  
}  
////////////////////////////////////////////////////////////////////////////////////
abstract class OtherPlant extends Plant {    

    public OtherPlant(int health, int cool_down, int price) {  
        super(health, cool_down, price);  
    }  
} 
////////////////////////////////////////////////////////////////////////////////////

// Subclass for attackerPlant 
class PeaShooter extends attackerPlant {  

    public peaShooter(int health, int cool_down, int price, int damage, int hit_rate, int speed) {  
        super(health, cool_down, price, damage, hit_rate, speed);   
    }  

    @Override  
    public void shoot() {  
        super.shoot();  //?
         
    }  
}  

class SnowPeaShooter extends attackerPlant {  

    public SnowPeaShooter(int health, int cool_down, int price, int damage, int hit_rate, int speed) {  
        super(health, cool_down, price, damage, hit_rate, speed);   
    }  

    @Override  
    public void shoot() {  
        //super.shoot();  //?
         
    }  
}  
/////////////////////////////////////////////////////////////////////////////////////
class Sunflower extends providerPlant {  

    public Sunflowers(int health, int cool_down, int price, int hit_rate) {  
        super(health, cool_down, price, hit_rate);   
    }  
 
}  
/////////////////////////////////////////////////////////////////////////////////////
class Sibzamini extends defenderPlant {  

    public sibzamini(int health, int cool_down, int price) {  
        super(health, cool_down, price);  
    } 
 
}  


