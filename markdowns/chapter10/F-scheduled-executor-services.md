# Scheduled Executor Services

Here's an example where we create three schedulers and run them using a thread
pool that always keeps 3 threads in the pool (even if they're idle):

```java runnable
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class Main {
  public static void main(String args[]) throws Exception {
    final ScheduledExecutorService threadPool = Executors.newScheduledThreadPool(3);
    final long startTime = System.nanoTime();
    
    for (int i = 0; i < 3; i++) {
      final int id = i;
      
      threadPool.scheduleAtFixedRate(() ->
        doWork(id, startTime), 0, 100, TimeUnit.MILLISECONDS);
    }
    threadPool.schedule(threadPool::shutdown, 300, TimeUnit.MILLISECONDS);
    
    if (threadPool.awaitTermination(1, TimeUnit.SECONDS)) {
      System.out.println("Thread pool terminated gracefully.");
    } else {
      System.err.println("Thread pool timed out!");
    }
  }
  
  private static void doWork(final int id, final long start) {
    System.out.println("ID: " + id + "\tTimestamp: " + (System.nanoTime() - start));
  }
}
```
