import org.apache.curator.RetryPolicy;
import org.apache.curator.framework.CuratorFramework;
import org.apache.curator.framework.CuratorFrameworkFactory;
import org.apache.curator.framework.recipes.locks.*;
import org.apache.curator.retry.ExponentialBackoffRetry;

import java.lang.management.ManagementFactory;

public class Main {
  public static void main(String args[]) throws Exception {
    final RetryPolicy retryPolicy = new ExponentialBackoffRetry(1000, 3);
    final CuratorFramework client = CuratorFrameworkFactory.newClient("127.0.0.1:2181", retryPolicy);
    final InterProcessMutex lock = new InterProcessMutex(client, "/path/to/lock");
    final String processID = ManagementFactory.getRuntimeMXBean().getName();
    
    try {
      client.start();
      lock.acquire();
      System.out.println(processID + " acquired the lock");
      Thread.sleep(1000); // simulates other work being done
      System.out.println(processID + " is releasing the lock");
    } finally {
      if (lock.isAcquiredInThisProcess()) {
        lock.release();
      }
      client.close();
    }
  }
}
