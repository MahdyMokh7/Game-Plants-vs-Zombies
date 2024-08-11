class UI {  
    private String winning_massage;
    private String losing_massage;
    private final Time time;
    private final Map map;

    public UI(String winning_massage, String losing_massage , Map map , Time time) {  
        this.winning_massage = winning_massage;
        this.losing_massage = losing_massage;   
        this.time = time;
        this.map = map;
    }  

    public void print_winning_massage() {  
        System.out.println(this.winning_massage);
    }  

    public void print_losing_massage() {  
        System.out.println(this.losing_massage);
 
    }
    
} 