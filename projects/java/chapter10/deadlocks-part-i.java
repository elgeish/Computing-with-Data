class A implements Runnable {
  public void run() {
    synchronized (A.class) {
      System.out.println("A has A.class and now wants B.class");
      try {
        Thread.sleep(500); // simulates some work being done
      } catch (InterruptedException ex) {
        System.out.println(ex);
      }
      synchronized (B.class) {
        System.out.println("A got both locks and made progress");
      }
    }
  }
}

class B implements Runnable {
  public void run() {
    synchronized (B.class) {
      System.out.println("B has B.class and now wants A.class");
      synchronized (A.class) {
        System.out.println("B got both locks and made progress");
      }
    }
  }
}

public class Main {
  public static void main(String args[]) throws Exception {
    new Thread(new A()).start();
    new Thread(new B()).start();
    Thread.sleep(1000); // ad-hoc wait till threads finish
  }
}
