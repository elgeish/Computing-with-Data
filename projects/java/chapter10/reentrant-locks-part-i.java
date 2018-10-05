import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class ReentrantLockExample {
  private final Lock lock = new ReentrantLock();
  
  public void foo() {
    lock.lock();
    try {
      // ...
      bar();
    } finally {
      lock.unlock();
    }
  }
  
  public void bar() {
    lock.lock();
    try {
      // ...
    } finally {
      lock.unlock();
    }
  }
}

public class Main {
  public static void main(String args[]) throws Exception {
    new ReentrantLockExample().foo();
  }
}
