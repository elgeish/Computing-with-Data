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
