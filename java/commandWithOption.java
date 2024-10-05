import java.util.Scanner;

public class Bentuk {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Masukkan bentuk yang diinginkan (segitiga, lingkaran, persegi): ");
    String bentuk = sc.nextLine();
    switch (bentuk) {
      case "segitiga":
        System.out.println("Anda memilih segitiga");
        int jumlahBaris = 5;
        for (int i = 1; i <= jumlahBaris; i++) {
          for (int j = 1; j <= i; j++) {
            System.out.print("*");
          }
          System.out.println();
        }
        break;
      case "lingkaran":
        System.out.println("Anda memilih lingkaran");
        System.out.println("Belum dapat diterapkan pada konsol");
        break;
      case "persegi":
        System.out.println("Anda memilih persegi");
        int panjang = 5;
        for (int i = 1; i <= panjang; i++) {
          for (int j = 1; j <= panjang; j++) {
            System.out.print("*");
          }
          System.out.println();
        }
        break;
      default:
        System.out.println("Bentuk yang dimasukkan tidak valid");
        break;
    }
  }
}
