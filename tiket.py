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