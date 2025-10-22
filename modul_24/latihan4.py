from datetime import datetime
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Fungsi untuk menyapa pengguna berdasarkan waktu
def sapa_pengguna():
    jam_sekarang = datetime.now().hour

    if 5 <= jam_sekarang < 12:
        return f"{Fore.YELLOW}Selamat pagi! 🌅"
    elif 12 <= jam_sekarang < 15:
        return f"{Fore.GREEN}Selamat siang! ☀️"
    elif 15 <= jam_sekarang < 18:
        return f"{Fore.MAGENTA}Selamat sore! 🌇"
    else:
        return f"{Fore.BLUE}Selamat malam! 🌙"

# Fungsi untuk setiap operasi
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return f"{Fore.RED}⚠️ Tidak bisa membagi dengan nol!"

def pangkat(a, b):
    return a ** b

# Program Utama
print(f"{Fore.CYAN}{'='*45}")
print(sapa_pengguna())
print(f"{Fore.CYAN}Selamat datang di {Style.BRIGHT}Kalkulator Mainan! 🤖")
print(f"{Fore.LIGHTBLACK_EX}{'-'*45}")
print(f"{Fore.YELLOW}Pilih operasi: {Fore.WHITE}tambah ➕ | kurang ➖ | kali ✖️  | bagi ➗ | pangkat 🔼")
print(f"{Fore.CYAN}{'='*45}")

# Input pengguna
operasi = input(f"{Fore.LIGHTBLUE_EX}Masukan operasi yang diinginkan: ").lower()
angka1 = float(input(f"{Fore.LIGHTBLUE_EX}Masukan angka pertama: "))
angka2 = float(input(f"{Fore.LIGHTBLUE_EX}Masukan angka kedua: "))

# Menentukan operasi
if operasi == "tambah":
    hasil = tambah(angka1, angka2)
    simbol = "➕ "
elif operasi == "kurang":
    hasil = kurang(angka1, angka2)
    simbol = "➖ "
elif operasi == "kali":
    hasil = kali(angka1, angka2)
    simbol = "✖️ "
elif operasi == "bagi":
    hasil = bagi(angka1, angka2)
    simbol = "➗ "
elif operasi == "pangkat":
    hasil = pangkat(angka1, angka2)
    simbol = "🔼 "
else:
    hasil = f"{Fore.RED}Operasi tidak dikenal ❌"
    simbol = "❓"

# Menampilkan hasil
print(f"\n{Fore.CYAN}{'-'*45}")
print(f"{Fore.GREEN}📊 Hasil: {Fore.WHITE}{angka1} {simbol} {angka2} = {Fore.YELLOW}{hasil}")
print(f"{Fore.CYAN}{'-'*45}")
print(f"{Fore.LIGHTMAGENTA_EX}Terima kasih sudah menggunakan Kalkulator Mainan! 🎉")
