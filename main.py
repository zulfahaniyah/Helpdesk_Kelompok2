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
    while True:
        garis("HELPDESK KAMPUS")
        for k, (nama, _) in menu.items():
            print(f"{k}. {nama}")
        print("0. Keluar")
        pilih = input("\nPilih menu: ").strip()
        if pilih == "0":
            print("Terima kasih sudah menghubungi Helpdesk Kampus!")
            break
        if pilih in menu:
            menu[pilih][1]()
            if not tanya_kembali_menu():
                print("Terima kasih sudah menghubungi Helpdesk Kampus!")
                break
        else:
            print("Pilihan tidak valid.")

        
if __name__ == "__main__":
    main()
