# The Producer-Consumer Problem - Part III

```java
class Producer implements Runnable {
  private static int i = 0;
  
  public void run() {
    while (true) {
      if (Shared.buffer.size() == Shared.MAX_BUFFER_SIZE) {
        Shared.waitUntilNotified();
      }
      
      Shared.buffer.add(produce());
      
      if (shouldNotifyConsumers()) {
        Shared.notifyWaitingThread();
      }
    }
  }
  
  private String produce() {
    return String.valueOf(i++);
  }
  
  private boolean shouldNotifyConsumers() {
    return Shared.buffer.size() == 1;
  }
}
```
