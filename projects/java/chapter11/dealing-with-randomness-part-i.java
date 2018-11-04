import org.testng.annotations.Test;

import java.util.Random;

import static org.testng.Assert.*;

class CoinFlipper {
  public enum Face {HEAD, TAIL}
  
  private final Random random = new Random();
  
  public Face flip() {
    return random.nextBoolean() ? Face.HEAD : Face.TAIL;
  }
}

public class CoinFlipperTest {
  @Test
  public void testFlip() {
    final CoinFlipper flipper = new CoinFlipper();
    final int trialsCount = 100;
    int headsCount = 0;
    
    for (int i = 0; i < trialsCount; i++) {
      if (flipper.flip() == CoinFlipper.Face.HEAD) {
        ++headsCount;
      }
    }
    
    assertTrue(Math.abs(headsCount - trialsCount / 2) <= 5);
  }
}
