public class bintang {
  public static void main(String[] args) {
    int jumlahBaris = 5;
    for (int i = 1; i <= jumlahBaris; i++) {
      for (int j = 1; j <= i; j++) {
        System.out.print("*");
      }
      System.out.println();
    }
  }
}
