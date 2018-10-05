import com.linkedin.parseq.Engine;
import com.linkedin.parseq.EngineBuilder;
import com.linkedin.parseq.Task;
import com.linkedin.parseq.trace.TraceUtil;

import java.util.Arrays;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.stream.IntStream;


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
    final int[] data = IntStream.range(0, 10000).toArray();
    final int chunkSize = data.length / 4;
    final Task<Integer> sum = Task.par(
      Task.callable(
        "a",
        Arrays.stream(data, 0 * chunkSize, 1 * chunkSize)::sum),
      Task.callable(
        "b",
        Arrays.stream(data, 1 * chunkSize, 2 * chunkSize)::sum),
      Task.callable(
        "c",
        Arrays.stream(data, 2 * chunkSize, 3 * chunkSize)::sum),
      Task.callable(
        "d",
        Arrays.stream(data, 3 * chunkSize, 4 * chunkSize)::sum)
    ).map("sum", (a, b, c, d) -> a + b + c + d);
    
    engine.run(sum);
    sum.await();
    System.out.println("Parallel Sum: " + sum.get());
    engine.shutdown();
    scheduler.shutdown();
    System.out.println(TraceUtil.getJsonTrace(sum));
  }
}
