import org.easymock.EasyMock;
import org.testng.annotations.Test;


interface DataLayer {
  void insertReminder(
    final Reminder reminder, long creationTimestampInMillis);
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
    dataLayer.insertReminder(
      reminder,
      System.currentTimeMillis());
    // ...
  }
}

public class OrchestratorTest {
  @Test
  public void testAddReminder() throws Exception {
    final Reminder reminderToAdd = new Reminder();
    final DataLayer dataLayerMock =
      EasyMock.createStrictMock(DataLayer.class);
    final Orchestrator orchestrator =
      new Orchestrator(dataLayerMock);

    dataLayerMock.insertReminder(
      EasyMock.same(reminderToAdd), EasyMock.anyLong());
    EasyMock.replay(dataLayerMock);

    orchestrator.addReminder(reminderToAdd);
    EasyMock.verify(dataLayerMock);
  }
}
