import java.util.stream.IntStream;

public class Main {
  public static void main(String args[]) throws Exception {
    System.out.println("Parallel Sum: " +
      IntStream.range(0, 10000).parallel().sum());
  }
}
