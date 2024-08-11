import java.util.ArrayList;
class Map {  
    private String[][] map;
    private ArrayList<ArrayList<Plant>> plants;
   // private final Time time;

    public Map() {  

        String[][] mapp = {  
            {" ", " ", " ", " ", " ", " ", " ", " "},  
            {" ", " ", " ", " ", " ", " ", " ", " "},  
            {" ", " ", " ", " ", " ", " ", " ", " "},  
            {" ", " ", " ", " ", " ", " ", " ", " "},  
            {" ", " ", " ", " ", " ", " ", " ", " "},  
            {" ", " ", " ", " ", " ", " ", " ", " "},  
            {" ", " ", " ", " ", " ", " ", " ", " "},  
            {" ", " ", " ", " ", " ", " ", " ", " "}  
        };  

        this.map = mapp;
        //this.time = time;
   
    }
} 