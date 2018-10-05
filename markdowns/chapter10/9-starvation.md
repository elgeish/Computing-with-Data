# Starvation

```java runnable
class DeepThoughtTask implements Runnable {
  static int finalResult = 0;
  
  private int computeResult() {
    return 1; // assume this is a long-running task
  }
  
  public void run() {
    long partialResult = computeResult(); // lock-free
    synchronized (DeepThoughtTask.class) {
      finalResult += partialResult;
    }
  }
}

class ProcessorHog implements Runnable {
  public void run() {
    synchronized (DeepThoughtTask.class) {
      try {
        Thread.sleep(3000); // keep the CPU busy
      } catch(InterruptedException ex) {
        System.out.println(ex);
      }
    }
  }
}

public class Main {
  public static void main(String args[]) throws Exception {
    new Thread(new ProcessorHog()).start();
    Thread.sleep(1000); // simulates other work being done
    DeepThoughtTask task = new DeepThoughtTask();
    for (int i = 0; i < 42; i++) {
      new Thread(task).start();
    }
    Thread.sleep(1000); // ad-hoc wait till threads finish
    System.out.println("answer: " + DeepThoughtTask.finalResult);
  }
}
```
