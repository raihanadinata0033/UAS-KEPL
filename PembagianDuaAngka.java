import java.util.logging.*;

public class PembagianDuaAngka {
    private static final Logger logger = Logger.getLogger(PembagianDuaAngka.class.getName());

    public static void main(String[] args) {
        try {
            int hasil = bagi(10, 2);
            logger.info("Pembagian berhasil: " + hasil);

            hasil = bagi(10, 0);
            logger.info("Pembagian berhasil: " + hasil);
        } catch (Exception e) {
            logger.severe("Terjadi kesalahan: " + e.getMessage());
        }
    }

    public static int bagi(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Pembagian oleh nol tidak diperbolehkan");
        }
        return a / b;
    }
}