public class UninitializedVariableExample {
  public static void main(final String[] args) {
    final int a = 3;
    final int b;
    final int c;

    System.out.println(a); // ok; prints 3
    b = 3;
    System.out.println(b); // ok; prints 3
    System.out.println(c); // error: c is not initialized
  }
}
