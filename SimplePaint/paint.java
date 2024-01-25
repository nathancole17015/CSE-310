package SimplePaint;

import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class paint {
    private static Graphics2D g;
    private static int lineSize;
    private static JComboBox<String> cb;
    private static JComboBox<String> cb2;


    public static void main(String[] args) {
        JFrame frame = new JFrame("New Frame");
        JPanel panel = new JPanel();

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);
        frame.setLocation(430, 100);
        frame.add(panel);

        String [] choices = {"Red", "Black", "Blue", "White"};
        String [] choices2 = {"Small","Medium","Large"};
        cb = new JComboBox<>(choices);
        cb2 = new JComboBox<>(choices2);
        cb.setVisible(true);
        panel.add(cb);
        panel.add(cb2);

        frame.getContentPane().setBackground(Color.WHITE);

        frame.addMouseMotionListener(new MouseMotionAdapter() {
            

            @Override
            public void mouseDragged(MouseEvent e) {
                int x1 = e.getX();
                int y1 = e.getY();
                int x2 = e.getX();
                int y2 = e.getY();

                ChooseColor();
                ChooseSize();
                g.setStroke(new BasicStroke(lineSize));

                g.drawLine(x1, y1, x2, y2);
                x1 = x2;
                y1 = y2;
            }
        });

        frame.setVisible(true);
        g = (Graphics2D) frame.getContentPane().getGraphics();
    }

    public static void ChooseColor() {
        String selectedOption = (String) cb.getSelectedItem();
        switch (selectedOption) {
            case "Red":
                g.setColor(Color.RED);
                break;
            case "Black":
                g.setColor(Color.BLACK);
                break;
            case "Blue":
                g.setColor(Color.BLUE);
                break;
            case "White":
                g.setColor(Color.WHITE);
                break;
            default:
                g.setColor(Color.BLACK);
                break;
        }
    }
    public static void ChooseSize() {
        String selectedOption = (String) cb2.getSelectedItem();
        switch (selectedOption) {
            case "Small":
                lineSize = 5;
                break;
            case "Medium":
                lineSize = 10;
                break;
            case "Large":
                lineSize = 15;
                break;
          
            default:
                lineSize = 10;
                break;
        }
    }

}
