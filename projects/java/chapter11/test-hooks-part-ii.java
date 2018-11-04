import com.google.common.annotations.VisibleForTesting;
import org.easymock.EasyMock;
import org.testng.annotations.Test;

import java.time.Clock;
import java.time.Instant;
import java.time.ZoneId;

interface DataLayer {
  void insertReminder(
    final Reminder reminder,
    final long creationTimestampInMillis);
}

class Reminder {
  // Reminder fields go here
}

class Orchestrator {
  private final DataLayer dataLayer;
  private Clock clock = Clock.systemUTC(); // for testability

  public Orchestrator(final DataLayer dataLayer) {
    this.dataLayer = dataLayer;
  }

  @VisibleForTesting
  void setClock(final Clock clock) {
    this.clock = clock;
  }

  public void addReminder(final Reminder reminder) {
    // Validation and pre-processing code goes here
    dataLayer.insertReminder(reminder, this.clock.millis());
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
    final long creationTimestampInMillis =
      System.currentTimeMillis();

    orchestrator.setClock(
      Clock.fixed(Instant.now(),
      ZoneId.systemDefault()));

    dataLayerMock.insertReminder(
      reminderToAdd,
      creationTimestampInMillis);
    EasyMock.replay(dataLayerMock);

    orchestrator.addReminder(reminderToAdd);
    EasyMock.verify(dataLayerMock);
  }
}
