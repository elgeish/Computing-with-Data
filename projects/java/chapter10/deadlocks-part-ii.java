import java.util.concurrent.atomic.AtomicInteger;

class DeepThoughtTask implements Runnable {
  static AtomicInteger finalResult = new AtomicInteger(0);
  
  private int computeResult() {
    return 1; // assume this is a long-running task
  }
  
  public void run() {
    // This is lock-free on modern CPUs
    finalResult.addAndGet(computeResult());
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
