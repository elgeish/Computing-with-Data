import org.easymock.EasyMock;
import org.testng.annotations.Test;

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
    final DataLayer dataLayerMock =
      EasyMock.createStrictMock(DataLayer.class);
    final Orchestrator orchestrator =
      new Orchestrator(dataLayerMock);

    dataLayerMock.insertReminder(reminderToAdd); // expect
    EasyMock.replay(dataLayerMock); // switch to replay state

    orchestrator.addReminder(reminderToAdd);
    // Assert the above mock conditions
    EasyMock.verify(dataLayerMock);
  }
}
