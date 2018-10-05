import org.apache.curator.RetryPolicy;
import org.apache.curator.framework.CuratorFramework;
import org.apache.curator.framework.CuratorFrameworkFactory;
import org.apache.curator.retry.ExponentialBackoffRetry;

public class Main {
  private static final String HOST = "127.0.0.1:2181";
  
  public static void main(String args[]) throws Exception {
    final RetryPolicy retryPolicy = new ExponentialBackoffRetry(1000, 3);
    try (final CuratorFramework client = CuratorFrameworkFactory.newClient(HOST, retryPolicy)) {
      client.start();
      client.createContainers​("/path/to/counter");

      final int version = client.inTransaction().
        setData().forPath("/path/to/counter").and().
        commit().iterator().next().
        getResultStat().getVersion();
      
      System.out.println("Version: " + version);
    }
  }
}
