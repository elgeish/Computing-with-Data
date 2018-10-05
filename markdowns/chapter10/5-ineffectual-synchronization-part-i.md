# Ineffectual Synchronization - Part I

To illustrate how subtle concurrency issues are and how hard they are to miss,
we will make a very small change that may look extremely inconspicuous:

```java runnable
class Task implements Runnable {
  static int sum = 0;
  synchronized public void run() { ++sum; }
}

public class Main {
  public static void main(String args[]) throws Exception {
    for (int i = 0; i < 10000; i++) {
      new Thread(new Task()).start();
    }
    Thread.sleep(1000); // ad-hoc wait till threads finish
    System.out.println("sum: " + Task.sum);
  }
}
```
