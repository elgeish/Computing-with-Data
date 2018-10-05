import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Reader extends Consumer implements Runnable {
  public void run() {
    int[] deepCopy;
    
    synchronized (Shared.cache) {
      int[] value = Shared.cache.get("key");
      
      deepCopy = Arrays.copyOf(value, value.length);
    }
    consume(deepCopy);
  }
}

// { autofold
class Writer extends Producer implements Runnable {
  public void run() {
    synchronized (Shared.cache) {
      int[] referenceToValue = Shared.cache.get("key");
      
      for (int i = 0; i < referenceToValue.length; i++) {
        // Update value in-place; sum will add up to length
        referenceToValue[i] = produce();
      }
    }
  }
}

class Simulator {
  static void simulateWork() {
    try {
      Thread.sleep(3); // simulates work being done
    } catch (InterruptedException ex) {
      System.out.println(ex);
    }
  }
}

class Shared {
  static final Map<String, int[]> cache = new HashMap<>();
}

class Producer {
  protected int produce() {
    Simulator.simulateWork();
    return 1;
  }
}

class Consumer {
  protected void consume(int[] value) {
    int sum = Arrays.stream(value).sum();
    
    if (sum != 0 && sum != value.length) {
      throw new IllegalStateException("Partial sum: " + sum);
    }
    
    Simulator.simulateWork();
  }
}

public class Main {
  private static long runTrial() throws Exception {
    long startTime = System.nanoTime();
    final Thread[] threads = new Thread[1000];
    
    Shared.cache.put("key", new int[20]); // sum = 0 at this time
    threads[0] = new Thread(new Writer(), "Writer");
    threads[0].start();
    
    for (int i = 1; i < threads.length; i++) {
      threads[i] = new Thread(new Reader(), "Reader #" + i);
      threads[i].start();
    }
    
    for (int i = 1; i < threads.length; i++) {
      threads[i].join();
    }
    
    return System.nanoTime() - startTime;
  }
  
  public static void main(String args[]) throws Exception {
    long[] trials = new long[11];
    
    for (int i = 0; i < trials.length; i++) {
      trials[i] = runTrial();
    }
    
    Arrays.sort(trials);
    
    long median = trials[trials.length / 2];
    double average = Arrays.stream(trials).
      average().
      getAsDouble();
    
    System.out.printf(
      "Median time in nanoseconds: %1$,d\n",
      median);
    System.out.printf(
      "Average time in nanoseconds: %1$,.2f\n",
      average);
  }
}
// }
