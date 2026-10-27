"""Fitur Pusat Bantuan (FAQ) dan pencarian jawaban."""

from data_faq import FAQ
from tampilan import garis


def tampilkan_faq():
    garis("PUSAT BANTUAN KAMPUS")
    kategori = list(FAQ.keys())
    for i, k in enumerate(kategori, 1):
        print(f"{i}. {k}")
    pilih = input("\nPilih kategori (angka, Enter untuk kembali): ").strip()
    if not pilih .isdigit() or not 1 <=int(pilih) <=len(kategori):
        return
    daftar = FAQ[kategori[int(pilih) - 1]]
    garis(kategori[int(pilih) - 1])
    for i, (tanya, _, _) in enumerate(daftar, 1):
        print(f"{i}. {tanya}") 
    p = input("\nPilih pertanyaan (angka): ").strip()
    if p.isdigit() and 1 <= int(p) <= len(daftar):
        tanya, jawab, _ = daftar[int(p) - 1]   
        print(f"\nQ: {tanya}\nA {jawab}")


    