import org.testng.annotations.Test;
import org.testng.Assert;
import org.testng.collections.Lists;

import java.util.ArrayList;
import java.util.List;

interface DataLayer {
  void insertReminder(final Reminder reminder);

  Reminder getReminder(final String reminderID);

  void updateReminder(
    final String reminderID, final Reminder reminder);

  void deleteReminder(final String reminderID);
}

class Reminder {
  // Reminder fields go here
}

class Orchestrator {
  private final DataLayer dataLayer;

  public Orchestrator(final DataLayer dataLayer) {
    this.dataLayer = dataLayer;
  }

  public void addReminder(final Reminder reminder) {
    // Validation and pre-processing code goes here
    dataLayer.insertReminder(reminder);
    // ...
  }
}

public class OrchestratorTest {
  @Test
  public void testAddReminder() throws Exception {
    final Reminder reminderToAdd = new Reminder();
    final List<String> methodsCalled = new ArrayList<>();
    final Orchestrator orchestrator =
      new Orchestrator(new DataLayer() {
      @Override
      public void insertReminder(final Reminder reminder) {
        methodsCalled.add("dataLayer.insertReminder");
        Assert.assertSame(
          reminder,
          reminderToAdd,
          "reminder mismatch in dataLayer.insertReminder");
      }

      @Override
      public Reminder getReminder(String reminderID) {
        Assert.fail("dataLayer.getReminder is not expected");
        return null;
      }

      @Override
      public void updateReminder(
        String reminderID, Reminder reminder) {
        Assert.fail("dataLayer.updateReminder is not expected");
      }

      @Override
      public void deleteReminder(String reminderID) {
        Assert.fail("dataLayer.deleteReminder is not expected");
      }
    });

    orchestrator.addReminder(reminderToAdd);

    Assert.assertEquals(
      methodsCalled,
      Lists.newArrayList("dataLayer.insertReminder"),
      "expected methods not called");
  }
}
