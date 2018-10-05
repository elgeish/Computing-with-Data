# Streams

The previous example can be simplified using parallel streams to be much more
succinct:

```java runnable
import java.util.stream.IntStream;

public class Main {
  public static void main(String args[]) throws Exception {
    System.out.println("Parallel Sum: " +
      IntStream.range(0, 10000).parallel().sum());
  }
}
```
