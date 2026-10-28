"""Fungsi untuk membantu tampilan di terminal"""


def garis(judul=""):
    print("\n" + "=" * 60)
    if judul:
        print(judul.center(60))
        print("=" * 60)

def tanya_kembali_menu():
    """Tanya apakah user ingin kembali ke menu utama. True = kembali, False = keluar."""
    while True:
        jawab = input("\nKembali ke menu utama? (y/n): ").strip().lower()
        if jawab in ("y", "ya"):
            return True
        if jawab in ("n", "tidak"):
            return False
        print("Masukkan y atau n.")