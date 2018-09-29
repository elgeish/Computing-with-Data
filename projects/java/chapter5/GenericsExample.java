class Point<T> {
  private T x;
  private T y;

  public Point(final T x, final T y) {
    this.x = x;
    this.y = y;
  }

  public String toString() {
    return "(" + this.x + ", " + this.y + ")";
  }
}

public class GenericsExample {
  public static void main(final String[] args) {
    Point<Double> p = new Point<>(3.0, 1.0);

    System.out.println(p);
    System.out.println(new Point<>(4, 2));
    System.out.println(new Point<>(1.3, 4.2));
    System.out.println(new Point<>("x", "y"));
  }
}
