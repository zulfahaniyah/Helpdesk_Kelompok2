"""Fitur chatbot sederhana berbasis pencocokan FAQ."""

from faq import cari_jawaban
from tampilan import garis
from tiket import buat_tiket


def chatbot():
    garis("CHATBOT HELPDESK KAMPUS (ketik 'selesai' untuk keluar)")
    print("Bot: Halo, mahasiswa! Ada yang bisa saya bantu?")
    while True:
        tanya = input("Kamu: ").strip()
        if tanya.lower() in ("selesai", "exit", "keluar"):
            print("Bot: Terima kasih, semangat kuliahnya!")
            return
        hasil = cari_jawaban(tanya)
        if hasil:
            print(f"Bot: {hasil[1]}")
        else:
            print("Bot: Maaf, saya belum menemukan jawabannya. "
                  "Silakan buat tiket agar staf kampus bisa membantu.")
            if input("Buat tiket sekarang? (y/n): ").lower() == "y":
                buat_tiket(deskripsi_awal=tanya)
                return