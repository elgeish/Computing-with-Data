# The Producer-Consumer Problem - Part IV

Running the following program will result into a race condition:

```java runnable
// { autofold
class Shared {
  static final int MAX_BUFFER_SIZE = 3;
  static Queue<String> buffer = new ArrayDeque<>();
  private static volatile boolean shouldWait = true;
  
  static void waitUntilNotified() {
    while (shouldWait);
    shouldWait = true;
  }
  
  static void notifyWaitingThread() {
    shouldWait = false;
  }
}

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
