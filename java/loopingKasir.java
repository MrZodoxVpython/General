import java.util.Scanner;

public class loopingKasir {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int jumlahBelanja = 0;
    while (true) {
      System.out.print("Masukkan harga barang atau ketik '0' untuk mengakhiri: ");
      int harga = sc.nextInt();
      if (harga == 0) {
        break;
      }
      jumlahBelanja += harga;
    }
    System.out.println("Total belanja: " + jumlahBelanja);
  }
}
