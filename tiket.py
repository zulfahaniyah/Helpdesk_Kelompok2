from datetime import datetime

from data_faq import KATEGORI_TIKET
from storage import buat_id, muat_tiket, simpan_tiket
from tampilan import garis


def buat_tiket(deskripsi_awal=""):
    garis("BUAT TIKET LAYANAN")
    nama = input("Nama lengkap          : ").strip()
    nim = input("NIM                   : ").strip()
    prodi = input("Program studi         : ").strip()
    email = input("Email kampus/aktif    : ").strip()

    for i, k in enumerate(KATEGORI_TIKET, 1):
        print(f"{i}. {k}")
    pilih = input("Kategori (angka): ").strip()
    kategori = (KATEGORI_TIKET[int(pilih) - 1]
                if pilih.isdigit() and 1 <= int(pilih) <= len(KATEGORI_TIKET)
                else "Lainnya")

    if deskripsi_awal:
        print(f"Keluhan              : {deskripsi_awal}")
        deskripsi = deskripsi_awal
    else:
        deskripsi = input("Ceritakan kendala kamu: ").strip()

    if not nama or not nim or not email or not deskripsi:
        print("Nama, NIM, email, dan keluhan wajib diisi.")
        return

    tiket = muat_tiket()
    baru = {
        "id": buat_id(),
        "nama": nama,
        "nim": nim,
        "prodi": prodi,
        "email": email,
        "kategori": kategori,
        "deskripsi": deskripsi,
        "status": "Open",
        "dibuat": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "balasan": [],
    }
    tiket.append(baru)
    simpan_tiket(tiket)
    print(f"\nTiket berhasil dibuat! ID tiket kamu: {baru['id']}")
    print("Simpan ID ini untuk mengecek status tiket.")

