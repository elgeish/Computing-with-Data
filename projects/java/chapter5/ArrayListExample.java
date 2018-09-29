import java.util.ArrayList;

public class ArrayListExample {
  public static void main(final String[] args) {
    final ArrayList<Double> a = new ArrayList<>();
    
    // Insert three elements
    a.add(1.0);
    a.add(3.0);
    a.add(2.0);
    
    // Traverse collection and print elements
    for (final double d : a) {
      System.out.print(d + " ");
    }
    System.out.println();
    
    a.set(1, 3.5); // modify 2nd element
    // Print 2nd element (random access)
    System.out.println(a.get(1));
    // Traverse collection and print elements
    for (final double d : a) {
      System.out.print(d + " ");
    }
    System.out.println();
  }
}
