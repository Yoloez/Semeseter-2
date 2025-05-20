import javax.swing.*;
import java.awt.*;

    public class LoginPage extends JFrame {
        public LoginPage(){

            setTitle("login page");
            setSize(300,200);
            setLocationRelativeTo(null);
            setLayout(new BorderLayout());
            JLabel titleLabel = new JLabel("Welcome to our platform, please login first");
            titleLabel.setFont(new Font("Arial", Font.BOLD, 13));
            add(titleLabel,BorderLayout.NORTH);


        JButton loginButton = new JButton("login");
        add(loginButton, BorderLayout.SOUTH);

        //input center
        JPanel inputPanel = new JPanel(new GridLayout(2,2));
        add(inputPanel);
        JLabel labelUsername = new JLabel("Username");
        inputPanel.add(labelUsername);
        JTextField usernameField = new JTextField();
        inputPanel.add(usernameField);
        JLabel labelpassword = new JLabel("Password");
        inputPanel.add(labelpassword);
        JPasswordField passwordField = new JPasswordField();
        inputPanel.add(passwordField);

        //loginfunction
        loginButton.addActionListener(e -> {
            String username = usernameField.getText();
            String password = String.valueOf(passwordField.getPassword());
            if (username.equals("Admin") && password.equals("1234")){
                JOptionPane.showMessageDialog(this, "Login success");
                dispose();
            }else JOptionPane.showMessageDialog(this, "username atau password salah");


        });

    }
}
