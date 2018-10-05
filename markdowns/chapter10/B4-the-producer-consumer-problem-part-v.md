# The Producer-Consumer Problem - Part V

In Java, it's idiomatic to use `wait` and `notify`, which require acquiring
a lock on the object for which those methods are called:

```java runnable
class Shared {
  static final int MAX_BUFFER_SIZE = 3;
  static Queue<String> buffer = new ArrayDeque<>();
  private static final Object lock = new Object();
  
  static void waitUntilNotified() {
    try {
      synchronized (lock) {
        lock.wait();
      }
    } catch (InterruptedException ex) {
      System.out.println(ex);
    }
  }
  
  static void notifyWaitingThread() {
    synchronized (lock) {
      lock.notify();
    }
  }
}

// { autofold
class Consumer implements Runnable {
  public void run() {
    while (true) {
      if (Shared.buffer.size() == 0) {
        Shared.waitUntilNotified();
      }
      
      consume();
      
      if (shouldNotifyProducers()) {
        Shared.notifyWaitingThread();
      }
    }
  }
  
  private void consume() {
    System.out.println("Consumed: " + Shared.buffer.remove());
  }
  
  private boolean shouldNotifyProducers() {
    return Shared.buffer.size() == Shared.MAX_BUFFER_SIZE - 1;
  }
}

class Producer implements Runnable {
  private static int i = 0;
  
  public void run() {
    while (true) {
      if (Shared.buffer.size() == Shared.MAX_BUFFER_SIZE) {
        Shared.waitUntilNotified();
      }
      
      Shared.buffer.add(produce());
      
      if (shouldNotifyConsumers()) {
        Shared.notifyWaitingThread();
      }
    }
  }
  
  private String produce() {
    return String.valueOf(i++);
  }
  
  private boolean shouldNotifyConsumers() {
    return Shared.buffer.size() == 1;
  }
}
// }

public class Main {
  public static void main(String args[]) throws Exception {
    new Thread(new Producer(), "produce").start();
    new Thread(new Consumer(), "consume").start();
  }
}
```
