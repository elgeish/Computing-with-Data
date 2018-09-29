public class MultidimensionalArrayExample {
  public static void main(final String[] args) {
    final int[][] ar = new int[10][10];

    for (int i = 0; i < ar.length; ++i) {
      for (int j = 0; j < ar[i].length; ++j) {
        ar[i][j] = i * 10 + j;
      }
    }

    for (int i = 0; i < ar.length; ++i) {
      for (int j = 0; j < ar[i].length; ++j) {
        System.out.print(ar[i][j] + " ");
      }
      System.out.print("\n");
    }
  }
}
