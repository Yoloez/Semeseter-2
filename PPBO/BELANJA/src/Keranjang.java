import java.util.ArrayList;
import java.util.List;

public class Keranjang {
    private List<Belanjaan> items;

    public Keranjang() {
        items = new ArrayList<>();
    }

    public void tambahItem(Belanjaan item) {
        items.add(item);
    }

    public int totalHarga() {
        int total = 0;
        for (Belanjaan item : items) {
            total += item.getHarga();
        }
        return total;
    }

    public int totalItem() {
        return items.size();
    }

    public List<String> daftarItem() {
        List<String> daftar = new ArrayList<>();
        for (Belanjaan item : items) {
            daftar.add(item.getNama());
        }
        return daftar;
    }
}