class UI {  
    private string winning_massage;
    private string winning_massage;
    private final Time time;
    private final Map map;

    public UI(string winning_massage, string losing_massage) {  
        this.winning_massage = winning_massage
        this.losing_massage = losing_massage;   
    }  

    public void print_winning_massage() {  
        System.out.println(this.winning_massage);
    }  

    public void print_losing_massage() {  
        System.out.println(this.losing_massage);
 
    }
    
} 