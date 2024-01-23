package SimplePaint;

import javax.swing.*;
import java.awt.event.*;
import java.awt.*;





public class paint {
    private static Graphics g;
    private static int x1,y1,x2,y2;
    public static void main(String[] args) {
        JFrame frame = new JFrame("new frame");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        frame.setSize(500, 400);
        


        frame.addMouseMotionListener(new MouseMotionAdapter() {
            @Override
            public void mouseDragged(MouseEvent e) {
                int x2 = e.getX();
                int y2 = e.getY();

                
                 g.setColor(Color.RED);
                
                 g.drawLine(x1, y1, x2, y2);
                 x1 = x2;
                y1 = y2;

                
            }
        });
       
        frame.setVisible(true);
        g = frame.getContentPane().getGraphics();
    }
}
