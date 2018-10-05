# The Producer-Consumer Problem - Part I

Let's talk a look at an example of a bad implementation; first, let's examine
our shared resource, which is a bounded queue in this case that's protected
with busy waiting:

```java
class Shared {
  static final int MAX_BUFFER_SIZE = 3;
  static Queue<String> buffer = new ArrayDeque<>();
  private static volatile boolean shouldWait = true;
  
  static void waitUntilNotified() {
    while (shouldWait);
    shouldWait = true;
  }
  
  static void notifyWaitingThread() {
    shouldWait = false;
  }
}
```
