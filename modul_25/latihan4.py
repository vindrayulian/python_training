import random
from colorama import Fore, Style, init
import time

# Inisialisasi colorama
init(autoreset=True)

# Pilihan yang tersedia
pilihan = ["batu", "gunting", "kertas"]

# Inisialisasi skor
skor_pemain = 0
skor_komputer = 0

print(Fore.CYAN + Style.BRIGHT + "🎮 Selamat datang di game Batu-Gunting-Kertas! 🤜🤛")
print(Fore.YELLOW + "Pilihan tersedia: Batu 🪨, Gunting ✂️, Kertas 📄")
print(Fore.MAGENTA + "Ketik 'exit' untuk keluar dari permainan.\n")

while True:
    pilihan_pemain = input(Fore.WHITE + "Masukkan pilihan kamu: ").lower()

    # Cek jika pemain ingin keluar
    if pilihan_pemain == "exit":
        print(Fore.CYAN + "\nPermainan berakhir... Menghitung skor akhir 🧮")
        time.sleep(1)
        print(Fore.CYAN + f"📊 Skor Akhir — Kamu: {skor_pemain} | Komputer: {skor_komputer}")
        if skor_pemain > skor_komputer:
            print(Fore.GREEN + "🏆 Kamu lebih unggul kali ini! Luar biasa! 🎉")
        elif skor_pemain < skor_komputer:
            print(Fore.RED + "🤖 Komputer lebih unggul kali ini, tapi jangan menyerah ya!")
        else:
            print(Fore.YELLOW + "⚖️ Seri! Pertarungan yang seimbang banget 😎")
        print(Fore.CYAN + "Terima kasih sudah bermain! 👋")
        break

    # Validasi input
    if pilihan_pemain not in pilihan:
        print(Fore.RED + "❌ Pilihan tidak valid! Pilih hanya antara: Batu, Gunting, atau Kertas.\n")
        continue

    # Komputer memilih secara acak
    print(Fore.CYAN + "Komputer sedang memilih", end="")
    for _ in range(3):
        print(Fore.CYAN + ".", end="", flush=True)
        time.sleep(0.5)
    print()

    pilihan_komputer = random.choice(pilihan)
    print(Fore.BLUE + f"🤖 Komputer memilih: {pilihan_komputer.upper()}")

    # Tentukan hasil
    if pilihan_pemain == pilihan_komputer:
        print(Fore.YELLOW + "😬 Hasil seri! Tidak ada yang kalah kali ini.")
    elif (pilihan_pemain == "batu" and pilihan_komputer == "gunting") or \
         (pilihan_pemain == "gunting" and pilihan_komputer == "kertas") or \
         (pilihan_pemain == "kertas" and pilihan_komputer == "batu"):
        print(Fore.GREEN + "🎉 Kamu menang! Hebat banget!")
        skor_pemain += 1
    else:
        print(Fore.RED + "😅 Kamu kalah! Komputer lebih beruntung kali ini.")
        skor_komputer += 1

    # Tampilkan skor terkini
    print(Fore.MAGENTA + f"📈 Skor sementara — Kamu: {skor_pemain} | Komputer: {skor_komputer}\n")
    time.sleep(1)
