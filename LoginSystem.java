import java.util.logging.*;

public class LoginSystem {
    private static final Logger logger = Logger.getLogger(LoginSystem.class.getName());

    public static void main(String[] args) {
        login("admin", "password123");
        login("user", "wrongpassword");
    }

    public static void login(String username, String password) {
        String correctUsername = "admin";
        String correctPassword = "password123";

        if (username.equals(correctUsername) && password.equals(correctPassword)) {
            logger.info("Login berhasil untuk pengguna: " + username);
        } else {
            logger.warning("Percobaan login gagal untuk pengguna: " + username);
        }
    }
}
