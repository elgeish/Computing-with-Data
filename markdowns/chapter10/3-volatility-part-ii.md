# Volatility - Part II

More importantly, declaring a shared resource as `volatile` can be
misleading as it may give a false sense of thread safety; it's crucial
to know that the mere act of sprinkling the keyword `volatile` on fields
doesn't guarantee thread safety and definitely doesn't protect against
concurrency issues. Let's take the following simple task as an example:

```java runnable
class Task implements Runnable {
  volatile static int sum = 0;
  public void run() { ++sum; }
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
