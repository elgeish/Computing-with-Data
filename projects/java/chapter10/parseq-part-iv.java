import com.linkedin.parseq.Engine;
import com.linkedin.parseq.EngineBuilder;
import com.linkedin.parseq.Task;
import com.linkedin.parseq.httpclient.HttpClient;
import com.linkedin.parseq.trace.TraceUtil;

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;


public class Main {
  public static void main(String args[]) throws Exception {
    final int availableProcessors =
      Runtime.getRuntime().availableProcessors();
    final ScheduledExecutorService scheduler =
      Executors.newScheduledThreadPool(availableProcessors + 1);
    final Engine engine = new EngineBuilder().
      setTaskExecutor(scheduler).
      setTimerScheduler(scheduler).
      build();
    final Task<Task<Void>> get = Task.par(
      getContentType("a://a"), // causes an exception
      getContentType("http://www.bing.com"),
      getContentType("http://www.facebook.com"),
      getContentType("http://www.google.com"),
      getContentType("http://www.yahoo.com"))
      .map((a, b, f, g, y) -> print(a, b, f, g, y));
    
    engine.run(Task.flatten(get));
    get.await();
    engine.shutdown();
    scheduler.shutdown();
    System.out.println(TraceUtil.getJsonTrace(get));
  }
  
  private static Task<String> getContentType(String url) {
    return HttpClient.get(url).task()
      .withTimeout(1, TimeUnit.SECONDS)
      .toTry()
      .map(t -> t.isFailed() ?
        "Failed to get " + url : t.get().getContentType());
  }
  
  private static Task<Void> print(String... strings) {
    return Task.action(() -> {
      for (final String s : strings) System.out.println(s);
    });
  }
}
