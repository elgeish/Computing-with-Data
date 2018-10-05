# Synchronization vs. Volatility

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

public class Main {
  public static void main(String args[]) throws Exception {
    DeepThoughtTask task = new DeepThoughtTask();
    for (int i = 0; i < 42; i++) {
      new Thread(task).start();
    }
    Thread.sleep(1000); // ad-hoc wait till threads finish
    System.out.println("answer: " + DeepThoughtTask.finalResult);
  }
}
```
