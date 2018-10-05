# Reentrant Locks - Part IV

The locks created using the `synchronized` keyword in Java are reentrant;
they are also known as intrinsic or monitor locks. Here's how reentrant
synchronization works:

```java
class ReentrantIntrinsicLockExample {
  private final Object intrinsicLock = new Object();
  
  public void foo() {
    synchronized (intrinsicLock) {
      // ...
      bar();
    }
  }
  
  public void bar() {
    synchronized (intrinsicLock) {
      // ...
    }
  }
}
```
