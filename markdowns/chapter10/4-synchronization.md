# Synchronization

Here's the new code snippet with a single keyword addition, `synchronized`,
to fix the race condition:

```java runnable
class Task implements Runnable {
  static int sum = 0;
  synchronized public void run() { ++sum; }
}

public class Main {
  public static void main(String args[]) throws Exception {
    Task task = new Task();
    for (int i = 0; i < 10000; i++) {
      new Thread(task).start();
    }
    Thread.sleep(1000); // ad-hoc wait till threads finish
    System.out.println("sum: " + Task.sum);
  }
}
```
