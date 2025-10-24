# Program tebak nama rahasia teman dengan menambahkan kesempatan menebak

import random

# Daftar nama teman (bisa kamu ubah sesuka hati)
daftar_nama = ["budi", "sinta", "andi", "rani", "dika", "lina", "agus"]

# Memilih satu nama secara acak dari daftar
nama_rahasia = random.choice(daftar_nama)

# Menyapa pemain
print("Selamat datang di permainan Tebak Nama Rahasia Teman!")
print("Saya sudah memikirkan salah satu nama teman saya dari daftar rahasia.")
print("Coba tebak siapa dia!\n")

# Menentukan jumlah kesempatan
kesempatan = 3

# Perulangan untuk percobaan menebak
while kesempatan > 0:
    tebakan = input("Masukkan tebakan kamu: ").lower()
    
    if tebakan == nama_rahasia:
        print("Selamat! Kamu menebak dengan benar!")
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f"Salah! Coba lagi. Kesempatan tersisa: {kesempatan}\n")
        else:
            print(f"Kesempatan habis! Nama rahasianya adalah {nama_rahasia.capitalize()}.")
