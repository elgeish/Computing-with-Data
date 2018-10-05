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
