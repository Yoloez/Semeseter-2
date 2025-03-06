public class Main {
    public static void main(String[] args) {
            Keranjang keranjang = new Keranjang();
            keranjang.tambahItem(new Roti("Sari Roti", 15000));
            keranjang.tambahItem(new Obat("Paracetamol", 5000));
            keranjang.tambahItem(new Mainan("Mobil Remote", 75000));

            System.out.println("Total Harga: " + keranjang.totalHarga());
            System.out.println("Total Item: " + keranjang.totalItem());
            System.out.println("Daftar Item: " + keranjang.daftarItem());
        }
    }

