import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import static org.testng.Assert.*;

class Adder {
  public int add(int x, int y) {
    return x + y;
  }
}

public class AdderTest {
  @DataProvider(name = "testAdd")
  private static Object[][] provideTestData() {
    return new Integer[][]{
      new Integer[]{0, 0, 0},
      new Integer[]{2, 3, 5},
      new Integer[]{-3, 5, 2},
      new Integer[]{-5, -3, -8},
      new Integer[]{-5, 3, -2},
      new Integer[]{0, Integer.MAX_VALUE, Integer.MAX_VALUE},
      new Integer[]{0, Integer.MIN_VALUE, Integer.MIN_VALUE},
      // ...
    };
  }
  
  @Test(dataProvider = "testAdd")
  public void testAdd(int x, int y, int expected) {
    final int z = new Adder().add(x, y);
    assertEquals(z, expected, "failed for " + x + " and " + y);
  }
}
