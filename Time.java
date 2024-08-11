public class Time {
    private int passed_time;

    // Constructor with default value of 0
    public Time() {
        this.passed_time = 0;
    }
÷
    // Copy Constructor
    public Time(Time other) {
        this.passed_time = other.passed_time;
    }

    // Getter for the time attribute
    public int getTime() {
        return passed_time;
    }

    // Method to increment the time
    public void increment() {
        passed_time++;
    }
}