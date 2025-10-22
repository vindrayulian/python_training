import random

# Pilihan yang tersedia
pilihan = ["batu", "gunting", "kertas"]

# Inisialisasi skor
skor_pemain = 0
skor_komputer = 0

print("Selamat datang di game Batu-Gunting-Kertas! 🤜🤛")
print("Pilihan: Batu, Gunting, Kertas")
print("Ketik 'exit' untuk keluar dari permainan.\n")

while True: # Tambahkan while untuk perulangan
    pilihan_pemain = input("Masukkan pilihan kamu: ").lower()

    # Cek jika pemain ingin keluar
    if pilihan_pemain == "exit":
        print("\nPermainan berakhir. Terima kasih sudah bermain! 🙌")
        print(f"Skor Akhir — Kamu: {skor_pemain} | Komputer: {skor_komputer}")
        if skor_pemain > skor_komputer:
            print("Kamu lebih unggul kali ini! 🎉")
        elif skor_pemain < skor_komputer:
            print("Komputer lebih unggul, tapi jangan menyerah ya! 🤖")
        else:
            print("Seri! Pertarungan yang seimbang 😎")
        break

    # Validasi input
    if pilihan_pemain not in pilihan:
        print("Pilihan tidak valid, silahkan pilih batu, gunting, atau kertas.\n")
        continue

    # Komputer memilih secara acak
    pilihan_komputer = random.choice(pilihan)
    print(f"Komputer memilih: {pilihan_komputer}")

    # Tentukan hasil
    if pilihan_pemain == pilihan_komputer:
        print("Hasil seri! 😬")
    elif (pilihan_pemain == "batu" and pilihan_komputer == "gunting") or \
         (pilihan_pemain == "gunting" and pilihan_komputer == "kertas") or \
         (pilihan_pemain == "kertas" and pilihan_komputer == "batu"):
        print("Kamu menang! 🎉")
        skor_pemain += 1
    else:
        print("Kamu kalah! 😅")
        skor_komputer += 1

    # Tampilkan skor terkini
    print(f"Skor sementara — Kamu: {skor_pemain} | Komputer: {skor_komputer}\n")
