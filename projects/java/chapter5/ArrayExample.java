public class ArrayExample {
  public static void main(final String[] args) {
    final int n = 10;
    final int[] ar = new int[n];

    for (int i = 0; i < ar.length; i++) {
      ar[i] = i;
    }
    for (final int e : ar) {
      System.out.print(e + " ");
    }
  }
}
