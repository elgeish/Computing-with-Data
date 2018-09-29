import java.util.Date;

public class DateExample {
  public static void main(final String[] args) {
    final Date date1 = new Date(); // define a new object date1
    final Date date2 = date1; // point date2 to date1
    
    // print both objects
    System.out.println(date1);
    System.out.println(date2);
    // Both objects date1 and date2 refer to the same memory 
    // Modifying date2 changes date1 as well
    date2.setTime(1);
    // print both objects
    System.out.println(date1);
    System.out.println(date2);
  }
}
