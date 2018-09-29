public class FunctionArgumentExample {
  private static void foo1(int a) {
    a = 1;
  }
  
  private static void foo2(final int[] arr) {
    arr[0] = 1;
  }

  public static void main(final String[] args) {
    final int a = 3;
    final int[] b = new int[1];

    System.out.println("primitive variable a before foo1: " + a);
    foo1(a);
    System.out.println("primitive variable a after foo1: " + a);
    b[0] = 3;
    System.out.println("b[0] before foo2: " + b[0]);
    foo2(b);
    System.out.println("b[0] after foo2: " + b[0]);
  }
}
