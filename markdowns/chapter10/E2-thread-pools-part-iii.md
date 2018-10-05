# Thread Pools - Part III

Another way to create an elastic thread pool is to use a work-stealing one,
which allows worker threads with nothing left to do to steal work from those
that are still busy with work. To demonstrate the difference:

```java runnable
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class Main {
  public static void main(String args[]) throws Exception {
    final ExecutorService threadPool = Executors.newWorkStealingPool(3);
    final long startTime = System.nanoTime();
    
    for (int i = 0; i < 10; i++) {
      threadPool.submit(() ->doWork(startTime));
    }
    
    threadPool.shutdown();
    
    if (threadPool.awaitTermination(1, TimeUnit.SECONDS)) {
      System.out.println("Thread pool terminated gracefully.");
    } else {
      System.err.println("Thread pool timed out!");
    }
  }
  
  private static void doWork(final long startTime) {
    System.out.println("Timestamp: " + (System.nanoTime() - startTime));
    try {
      Thread.sleep(100);
    } catch (InterruptedException ex) {
      System.out.println(ex);
    }
  }
}
```
