//package com;

import java.util.jar.Attributes.Name;

abstract public class Plant {  
    protected int health;  
    protected int cool_down;  
    protected int price;  
    private final Time time;
    private final Map map;
    private final int x_position;
    private final int y_position;

    public Plant(int health, int cool_down, int price , int x_pos , int y_pos , Map map , Time time ) {  
        this.health = health;  
        this.cool_down = cool_down;  
        this.price = price;  
        this.x_position = x_pos;
        this.y_position = y_pos;
        this.time = time;
        this.map = map;
    }  

    abstract public String get_type();

    public boolean is_alive() {  
        if(this.health == 0){
            return false;
        }
        return true;
    
    }  

    public void got_hit() {

    }
    
}  

//////////////////////////////////////////////////////////////////////////////////////// 
abstract class AttackerPlant extends Plant {  
    protected int damage;  
    protected int hit_rate;  
    protected int speed;  
    protected boolean attack;  

    public AttackerPlant(int health, int cool_down, int price, int damage, int hit_rate, int speed , int x_pos , int y_pos , Map map , Time time ) {  
        super(health, cool_down, price , x_pos , y_pos , map , time );  
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


    public ProviderPlant(int health, int cool_down, int price, int hit_rate , int x_pos , int y_pos , Map map , Time time ) {  
        super(health, cool_down, price , x_pos , y_pos , map , time );  
        this.hit_rate = hit_rate;  
    }  

    protected boolean is_time_to_produce() {  
        
    }  

    abstract public void produce();
}  

////////////////////////////////////////////////////////////////////////////////////
abstract class DefenderPlant extends Plant {    

    public DefenderPlant(int health, int cool_down, int price , int x_pos , int y_pos , Map map , Time time) {  
        super(health, cool_down, price, x_pos , y_pos , map , time);  
    }  
}  
////////////////////////////////////////////////////////////////////////////////////
abstract class OtherPlant extends Plant {    

    public OtherPlant(int health, int cool_down, int price , int x_pos , int y_pos , Map map , Time time) {  
        super(health, cool_down, price, x_pos , y_pos , map , time);  
    }  
} 
////////////////////////////////////////////////////////////////////////////////////

// Subclass for attackerPlant 
class PeaShooter extends AttackerPlant {  
    public static final String NAME = "PeaShooter";
    private static final String IMG_PATH = "Image files/";  ///////////////

    public PeaShooter(int health, int cool_down, int price, int damage, int hit_rate, int speed , int x_pos , int y_pos , Map map , Time time) {  
        super(health, cool_down, price, damage, hit_rate, speed, x_pos , y_pos , map , time);   
    } 

    @Override  
    public void shoot() {  
         
    }

    @Override
    public String get_type() {
        return PeaShooter.NAME;
    }

}  

class SnowPeaShooter extends AttackerPlant {  

    public static String NAME = "SnowPeaShooter";
    private static final String IMG_PATH = "Image files/";  ///////////////

    public SnowPeaShooter(int health, int cool_down, int price, int damage, int hit_rate, int speed , int x_pos , int y_pos , Map map , Time time) {  
        super(health, cool_down, price, damage, hit_rate, speed, x_pos , y_pos , map , time);   
    }  

    @Override  
    public void shoot() {  
         
    }

    @Override
    public String get_type() {
        return SnowPeaShooter.NAME;
    }

}  

/////////////////////////////////////////////////////////////////////////////////////
class Sunflower extends ProviderPlant {  

    public static String NAME = "Sunflower";
    private static final String IMG_PATH = "Image files/";  ///////////////

    public Sunflower(int health, int cool_down, int price, int hit_rate, int x_pos , int y_pos , Map map , Time time) {  
        super(health, cool_down, price, hit_rate, x_pos , y_pos , map , time);   
    }  

    @Override
    public String get_type() {
        return Sunflower.NAME;
    }

    @Override
    public void produce() {
        if (!super.is_time_to_produce()) {

        }
        else {

        }
    }
 
}  

/////////////////////////////////////////////////////////////////////////////////////
class Sibzamini extends DefenderPlant {  

    public static String NAME = "Sibzamini";
    private static final String IMG_PATH = "Image files/";  ///////////////

    public Sibzamini(int health, int cool_down, int price, int x_pos , int y_pos , Map map , Time time) {  
        super(health, cool_down, price, x_pos , y_pos , map , time);  
    } 

    @Override
    public String get_type() {
        return Sibzamini.NAME;
    }
 
}  


