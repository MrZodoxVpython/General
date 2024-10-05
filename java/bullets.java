import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Bulat extends JPanel {
  public void paintComponent(Graphics g) {
    super.paintComponent(g);
    g.drawOval(10, 10, 50, 50);
  }

  public static void main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Bulat());
    frame.setSize(400, 400);
    frame.setVisible(true);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  }
}
