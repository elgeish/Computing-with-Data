class Point {
  private double x = 0;
  private double y = 0;

  public Point() {} // empty constructor

  public Point(final int x, final int y) {
    this.x = x;
    this.y = y;
  }

  public void setX(final double x) {
    this.x = x;
  }

  public void setY(final double y) {
    this.y = y;
  }

  public double getX() {
    return this.x;
  }

  public double getY() {
    return this.y;
  }

  public void reflect() {
    this.x = -this.x;
    this.y = -this.y;
  }

  public String toString() {
    return "(" + this.x + ", " + this.y + ")";
  }
}

public class PointExample {
  public static void main(final String[] args) {
    final Point p = new Point(1, 2);

    System.out.println(p);
    p.reflect();
    System.out.println(p);
  }
}
