import com.google.common.annotations.VisibleForTesting;
import org.testng.annotations.Test;

import java.util.Random;

import static org.testng.Assert.*;

class CoinFlipper {
  public enum Face {HEAD, TAIL}
  
  private Random random = new Random();
  
  public Face flip() {
    return random.nextBoolean() ? Face.HEAD : Face.TAIL;
  }
  
  @VisibleForTesting
  void setRandom(final Random random) {
    this.random = random;
  }
}

public class CoinFlipperTest {
  @Test
  public void testFlip() {
    final CoinFlipper flipper = new CoinFlipper();
    final Random random = new Random(42);
    
    flipper.setRandom(random);
    assertEquals(flipper.flip(), CoinFlipper.Face.HEAD);
    assertEquals(flipper.flip(), CoinFlipper.Face.TAIL);
    assertEquals(flipper.flip(), CoinFlipper.Face.HEAD);
  }
}
