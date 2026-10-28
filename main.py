from chatbot import chatbot
from faq import tampilkan_faq
from staf import mode_staf
from tampilan import garis, tanya_kembali_menu
from tiket import buat_tiket, cek_status


def main():
    menu = {
        "1": ("Pusat Bantuan (FAQ)", tampilkan_faq),
        "2": ("Chat dengan Bot", chatbot),
        "3": ("Buat Tiket Layanan", buat_tiket),
        "4": ("Cek Status Tiket", cek_status),
        "5": ("Mode Staf Kampus", mode_staf),
    }