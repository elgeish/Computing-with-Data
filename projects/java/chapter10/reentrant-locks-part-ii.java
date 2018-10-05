import java.util.concurrent.Semaphore;

class ReentrantLockExample {
  private final Semaphore lock = new Semaphore(1);
  
  public void foo() throws InterruptedException {
    lock.acquire();
    try {
      // ...
      bar();
    } finally {
      lock.release();
    }
  }
  
  public void bar() throws InterruptedException {
    lock.acquire();
    try {
      // ...
    } finally {
      lock.release();
    }
  }
}

public class Main {
  public static void main(String args[]) throws Exception {
    new ReentrantLockExample().foo();
  }
}
