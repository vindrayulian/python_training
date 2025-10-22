import random  # Mengimpor modul random untuk pilihan komputer

# Membuat pilihan yang tersedia
pilihan = ["batu", "gunting", "kertas"]

print("Selamat datang di game Batu-Gunting-Kertas! ☺️")
print("Pilihan: Batu, Gunting, Kertas")

# Pemain memilih
pilihan_pemain = input("Masukkan pilihan kamu: ").lower()

# Cek apakah pilihan pemain valid
if pilihan_pemain not in pilihan:
    print("Pilihan tidak valid, silahkan pilih batu, gunting, atau kertas")
else:
    # Komputer memilih secara acak
    pilihan_komputer = random.choice(pilihan)
    print(f"Komputer memilih : {pilihan_komputer}")

    # Menentukan pemenang
    if pilihan_pemain == pilihan_komputer:
        print("Hasil seri! 😬")
    elif (pilihan_pemain == "batu" and pilihan_komputer == "gunting") or \
         (pilihan_pemain == "gunting" and pilihan_komputer == "kertas") or \
         (pilihan_pemain == "kertas" and pilihan_komputer == "batu"):
        print("Kamu menang! 🎉")
    else:
        print("Kamu kalah! 😅")
