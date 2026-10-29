"""Fitur tiket: membuat tiket, mencetak detail, dan cek status."""

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


def cetak_tiket(t):
    garis(f"TIKET {t['id']}")
    print(f"Nama     : {t['nama']} ({t['nim']})")
    print(f"Prodi    : {t['prodi'] or '-'}")
    print(f"Email    : {t['email']}")
    print(f"Kategori : {t['kategori']}")
    print(f"Status   : {t['status']}")
    print(f"Dibuat   : {t['dibuat']}")
    print(f"Keluhan  : {t['deskripsi']}")
    if t["balasan"]:
        print("\nBalasan Staf:")
        for b in t["balasan"]:
            print(f"  [{b['waktu']}] {b['staf']}: {b['pesan']}")
    else:
        print("\nBelum ada balasan dari staf.")


def cek_status():
    garis("CEK STATUS TIKET")
    kunci = input("Masukkan ID tiket / NIM: ").strip().upper()
    ditemukan = [t for t in muat_tiket()
                 if t["id"].upper() == kunci or t["nim"].upper() == kunci]
    if not ditemukan:
        print("Tiket tidak ditemukan.")
        return
    for t in ditemukan:
        cetak_tiket(t)


def hapus_tiket(daftar, t):
    """Hapus tiket dari daftar. Hanya tiket berstatus Selesai, dengan konfirmasi."""
    if t["status"] != "Selesai":
        print("Tiket hanya dapat dihapus jika berstatus Selesai.")
        return False
    yakin = input(f"Yakin hapus tiket {t['id']}? (y/n): ").strip().lower()
    if yakin != "y":
        print("Penghapusan dibatalkan.")
        return False
    daftar.remove(t)
    print("Tiket berhasil dihapus.")
    return True