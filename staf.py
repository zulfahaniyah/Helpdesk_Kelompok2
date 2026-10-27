"""Fitur Mode Staf: lihat tiket, balas, dan ubah status."""

from datetime import datetime

from data_faq import STATUS
from storage import muat_tiket, simpan_tiket
from tampilan import garis
from tiket import cetak_tiket

SANDI_STAF = "staf123"  # ganti sandi ini untuk produksi


def mode_staf():
    garis("MODE STAF KAMPUS")
    sandi = input("Masukkan sandi staf: ")
    if sandi != SANDI_STAF:
        print("Sandi salah.")
        return
    nama_staf = input("Nama staf: ").strip() or "Staf Kampus"

    while True:
        tiket = muat_tiket()
        garis("DAFTAR TIKET")
        if not tiket:
            print("Belum ada tiket.")
        for i, t in enumerate(tiket, 1):
            print(f"{i}. {t['id']} | {t['kategori']:<24} | {t['status']:<9} | {t['nama']}")
        pilih = input("\nPilih tiket (angka) atau Enter untuk keluar: ").strip()
        if not pilih.isdigit() or not 1 <= int(pilih) <= len(tiket):
            return
        t = tiket[int(pilih) - 1]
        cetak_tiket(t)

        print("\n1. Balas tiket\n2. Ubah status\n3. Kembali")
        aksi = input("Pilih aksi: ").strip()
        if aksi == "1":
            pesan = input("Pesan balasan: ").strip()
            if pesan:
                t["balasan"].append({
                    "staf": nama_staf,
                    "pesan": pesan,
                    "waktu": datetime.now().strftime("%Y-%m-%d %H:%M"),
                })
                if t["status"] == "Open":
                    t["status"] = "Diproses"
        elif aksi == "2":
            for i, s in enumerate(STATUS, 1):
                print(f"{i}. {s}")
            s = input("Status baru (angka): ").strip()
            if s.isdigit() and 1 <= int(s) <= len(STATUS):
                t["status"] = STATUS[int(s) - 1]
        simpan_tiket(tiket)