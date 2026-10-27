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

def cari_jawaban(pertanyaan):
    """Cocokkan pertanyaan user dengan FAQ berdasarkan kata kunci."""
    teks = pertanyaan.lower()
    terbaik, skor_terbaik = None, 0
    for daftar in FAQ.values():
        for tanya, jawab, kunci in daftar:
            skor = sum(1 for k in kunci if k in teks)
            skor += sum(1 for kata in tanya.lower().split()
                        if len(kata) > 4 and kata in teks) * 0.5
            if skor > skor_terbaik:
                terbaik, skor_terbaik = (tanya, jawab), skor
    return terbaik if skor_terbaik >= 1 else None
    