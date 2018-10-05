class Consumer implements Runnable {
  public void run() {
    while (true) {
      if (Shared.buffer.size() == 0) {
        Shared.waitUntilNotified();
      }
      
      consume();
      
      if (shouldNotifyProducers()) {
        Shared.notifyWaitingThread();
      }
    }
  }
  
  private void consume() {
    System.out.println("Consumed: " + Shared.buffer.remove());
  }
  
  private boolean shouldNotifyProducers() {
    return Shared.buffer.size() == Shared.MAX_BUFFER_SIZE - 1;
  }
}
