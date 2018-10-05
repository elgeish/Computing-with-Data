# The Producer-Consumer Problem - Part VI

The following program fixes the deadlock issue and works correctly:

```java runnable
import java.util.ArrayDeque;
import java.util.Queue;

class Shared {
  private static final int MAX_BUFFER_SIZE = 3;
  private static Queue<String> buffer = new ArrayDeque<>();
  private static final Object lock = new Object();
  
  static String remove() throws InterruptedException {
    final String message;
    
    synchronized (lock) {
      while (buffer.size() == 0) {
        lock.wait();
      }
      message = buffer.remove();
      lock.notify();
    }
    return message;
  }
  
  static void add(String message) throws InterruptedException {
    synchronized (lock) {
      while (buffer.size() == MAX_BUFFER_SIZE) {
        lock.wait();
      }
      buffer.add(message);
      lock.notify();
    }
  }
}

class Consumer implements Runnable {
  public void run() {
    while (true) {
      try {
        System.out.println("Consumed: " + Shared.remove());
      } catch (Exception ex) {
        System.out.println(ex);
      }
    }
  }
}

class Producer implements Runnable {
  private static int i = 0;
  
  public void run() {
    while (true) {
      try {
        Shared.add(String.valueOf(i++));
      } catch (Exception ex) {
        System.out.println(ex);
      }
    }
  }
}

public class Main {
  public static void main(String args[]) throws Exception {
    new Thread(new Producer(), "Producer").start();
    new Thread(new Consumer(), "Consumer").start();
  }
}
```
