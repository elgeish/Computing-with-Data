import java.lang.management.ManagementFactory;
import java.nio.channels.FileChannel;
import java.nio.channels.FileLock;
import java.nio.file.FileSystems;
import java.nio.file.Path;

import static java.nio.file.StandardOpenOption.*;


public class Main {
  public static void main(String args[]) throws Exception {
    final Path lockPath =
      FileSystems.getDefault().getPath(".lock");
    final String processID =
      ManagementFactory.getRuntimeMXBean().getName();
    
    try (final FileLock lock =
      FileChannel.open(lockPath, WRITE, CREATE).lock()) {
      System.out.println(processID + " acquired the lock");
      Thread.sleep(1000); // simulates other work being done
      System.out.println(processID + " is releasing the lock");
    }
  }
}
