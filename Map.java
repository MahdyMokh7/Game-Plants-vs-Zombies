import java.util.ArrayList;
class Map {  
    private String[][] maap;
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

        this.maap = mapp;
        //this.time = time;
   
    }
} 