import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class MonthCounter {
  public static void main(String[] args) {
    LocalDate startDate = LocalDate.of(2021, 01, 01);
    LocalDate endDate = LocalDate.of(2022, 12, 31);
    long monthsBetween = ChronoUnit.MONTHS.between(startDate, endDate);
    System.out.println("Jumlah bulan antara " + startDate + " dan " + endDate + " adalah " + monthsBetween);
  }
}
