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
    Thread[] threads = new Thread[42];
    for (int i = 0; i < threads.length; i++) {
      threads[i] = new Thread(task);
      threads[i].start(); // fork; non-blocking
    }
    for (int i = 0; i < threads.length; i++) {
      threads[i].join(); // wait; blocking
    }
    System.out.println("answer: " + DeepThoughtTask.finalResult);
  }
}
