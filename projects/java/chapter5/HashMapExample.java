import java.util.HashMap;

public class HashMapExample {
  public static void main(final String[] args) {
    HashMap<String, Double> hm = new HashMap<>();
    
    // Insert three elements
    hm.put("John", 1.0);
    hm.put("Mary", 3.0);
    hm.put("Jane", 2.0);

    System.out.println(hm); // print all entries
    hm.remove("Jane"); // remove an entry
    System.out.println(hm); // print all entries
    // Lookup based on key
    System.out.println("John: " + hm.get("John"));
  }
}
