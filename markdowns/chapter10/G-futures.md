# Futures

Here's an example that shows how to return the results of tasks run in parallel:

```java runnable
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.stream.IntStream;

public class Main {
  public static void main(String args[]) throws Exception {
    final ExecutorService threadPool = Executors.newCachedThreadPool();
    final List<Future<Integer>> futures = new ArrayList<>();
    final int[] data = IntStream.range(0, 10000).toArray();
    int sum = 0;
    
    for (int i = 0, step = 1000; i < data.length; i += step) {
      final IntStream chunk = Arrays.stream(data, i, i + step);
      
      futures.add(threadPool.submit(chunk::sum));
    }
    
    for (final Future<Integer> f : futures) {
      sum += f.get();
    }
    
    System.out.println("Parallel Sum: " + sum);
    threadPool.shutdown();
  }
}
```
