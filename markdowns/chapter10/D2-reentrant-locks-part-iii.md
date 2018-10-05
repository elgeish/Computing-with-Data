# Reentrant Locks - Part III

That doesn't mean that reentrant locks are safer than non-reentrant ones:

```java runnable
import java.util.concurrent.locks.ReentrantLock;

class NonReentrantLockExample {
  private final ReentrantLock lock = new ReentrantLock();
  
  public void foo() throws InterruptedException {
    assert !lock.isHeldByCurrentThread() :
      "lock is held by current thread";
    lock.lock();
    try {
      // ...
      threadUnsafeBar();
    } finally {
      lock.unlock();
    }
  }
  
  public void bar() throws InterruptedException {
    assert !lock.isHeldByCurrentThread() :
      "lock is held by current thread";
    lock.lock();
    try {
      threadUnsafeBar();
    } finally {
      lock.unlock();
    }
  }
  
  private void threadUnsafeBar() {
    assert lock.isHeldByCurrentThread() :
      "caller must hold the lock first";
    // ...
  }
}

public class Main {
  public static void main(String args[]) throws Exception {
    new NonReentrantLockExample().foo();
  }
}
```
