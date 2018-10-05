# Thread Pools - Part II

Thread pools can be also be elastic: they scale with increased demand to run
parallel tasks and shrink when said demand diminishes. An example of such
thread pool is called a cached thread pool; to demonstrate the difference, we
replace the statement that creates the thread pool in the previous example
with this one:

```java runnable
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class Main {
  public static void main(String args[]) throws Exception {
    final ExecutorService threadPool = Executors.newCachedThreadPool();
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
