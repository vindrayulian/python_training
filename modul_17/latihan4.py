import random
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Daftar kata berdasarkan kategori
kategori_kata = {
    "Hewan": ["BURUNG", "PANDA", "KUCING", "GAJAH", "ULAR"],
    "Benda": ["SEPEDA", "MOBIL", "KOMPUTER", "BUKU", "JAM"],
    "Buah": ["APEL", "PISANG", "MANGGA", "JERUK", "ANGGUR"]
}

# Inisialisasi skor
skor = 0

# Header permainan
print(Fore.CYAN + Style.BRIGHT + "==============================")
print(Fore.CYAN + Style.BRIGHT + "   Permainan Tebak Huruf ")
print(Fore.CYAN + Style.BRIGHT + "==============================\n")
print(Fore.YELLOW + "Tersedia kategori: Hewan, Benda, Buah")
print(Fore.GREEN + "Dapatkan 10 poin setiap kali berhasil menebak kata!\n")

# Pilih kategori
while True:
    print(Fore.BLUE + "Pilih kategori:")
    for kategori in kategori_kata.keys():
        print("-", kategori)
    pilihan = input(Fore.YELLOW + "Masukkan kategori pilihanmu: ").capitalize()
    
    if pilihan in kategori_kata:
        print(Fore.CYAN + "\nKamu memilih kategori:", pilihan)
        break
    else:
        print(Fore.RED + " Kategori tidak valid, coba lagi!\n")

# Pilih kata rahasia dari kategori yang dipilih
kata = random.choice(kategori_kata[pilihan])

# Buat daftar untuk melacak huruf yang sudah ditebak
tebakan = ["_"] * len(kata)
huruf_tertebak = []

# Jumlah maksimal tebakan salah
kesempatan = 10

print(Fore.YELLOW + "\nKata rahasia memiliki", len(kata), "huruf.")
print(Fore.YELLOW + "Kamu punya", kesempatan, "kesempatan salah.")
print(Fore.CYAN + "Ayo mulai menebak!\n")

# Mulai permainan
while kesempatan > 0 and "_" in tebakan:
    print(Fore.MAGENTA + "Kategori:", pilihan)
    print(Fore.WHITE + "Kata saat ini:", " ".join(tebakan))
    huruf = input(Fore.YELLOW + "Tebak satu huruf: ").upper()
    
    # Periksa apakah huruf sudah ditebak sebelumnya
    if huruf in huruf_tertebak:
        print(Fore.RED + " Kamu sudah menebak huruf ini, coba huruf lain!\n")
        continue
    
    huruf_tertebak.append(huruf)
    
    # Periksa apakah huruf ada di kata rahasia
    if huruf in kata:
        print(Fore.GREEN + " Betul! Huruf", huruf, "ada di kata.\n")
        for i in range(len(kata)):
            if kata[i] == huruf:
                tebakan[i] = huruf
    else:
        print(Fore.RED + " Maaf, huruf", huruf, "tidak ada di kata.")
        kesempatan -= 1
        print(Fore.YELLOW + "Kesempatan tersisa:", kesempatan, "\n")
    
    # Periksa hasil akhir
    if "_" not in tebakan:
        print(Fore.GREEN + Style.BRIGHT + "\n Selamat! Kamu berhasil menebak kata:", kata)
        skor += 10  # Tambahkan skor jika berhasil menebak seluruh kata
        print(Fore.CYAN + f"Kamu mendapat {skor} poin!\n")
        break
else:
    print(Fore.RED + Style.BRIGHT + "\n Kesempatan habis.")
    print(Fore.YELLOW + "Kata rahasianya adalah:", Fore.WHITE + kata)

# Tampilkan skor akhir
print(Fore.CYAN + Style.BRIGHT + "\n Skor akhir kamu:", skor)
print(Fore.GREEN + "Terima kasih sudah bermain!\n")
print(Fore.CYAN + "==============================")
print(Fore.CYAN + "        Permainan Selesai      ")
print(Fore.CYAN + "==============================")
