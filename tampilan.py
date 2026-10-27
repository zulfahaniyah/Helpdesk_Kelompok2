"""Fungsi untuk meembantu tampilan di terminal"""


def garis(judul=""):
    print("\n" + "=" * 60)
    if judul:
        print(judul.center(60))
        print("=" * 60)