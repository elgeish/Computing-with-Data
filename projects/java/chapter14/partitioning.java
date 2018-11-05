import java.util.Random;
import java.util.concurrent.TimeUnit;

class ProbabilisticExponentialBackoffPoller {
  public Object[] poll(
      final TimeUnit timeUnit,
      final int initialDelay,
      final int maxTotalDelay,
      final double delayResetProbability)
        throws InterruptedException {
    final Random random = new Random();
    Object[] messages = readMessages();
    int currentDelay = initialDelay;
    int totalDelay = 0;
    
    while (messages.length == 0 && totalDelay <= maxTotalDelay) {
      System.out.printf(
        "Sleeping for %d %s\n", currentDelay, timeUnit);
      timeUnit.sleep(currentDelay);
      totalDelay += currentDelay;
      currentDelay *= 2;
      
      if (delayResetProbability > random.nextDouble()) {
        System.out.println("Resetting delay interval");
        currentDelay = initialDelay;
      }
      
      messages = readMessages();
    }
    return messages;
  }
  
  private Object[] readMessages() {
    return new Object[0];
  }
}

public class Main {
  public static void main(String args[]) throws Exception {
    final Object[] messages =
      new ProbabilisticExponentialBackoffPoller().poll(
      TimeUnit.MILLISECONDS, 2, 60, 0.42);
  }
}
