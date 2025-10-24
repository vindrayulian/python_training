# Program tebak nama rahasia teman dengan menambahkan list teman

import random

# Daftar nama teman
daftar_nama = ["budi", "sinta", "andi", "rani", "dika", "lina", "agus"]

# Memilih satu nama secara acak dari daftar
nama_rahasia = random.choice(daftar_nama)

# Menyapa pemain
print("Selamat datang di permainan Tebak Nama Rahasia Teman!")
print("Saya sudah memikirkan salah satu nama teman saya dari daftar rahasia.")
print("Coba tebak siapa dia!\n")

# Meminta pemain untuk menebak
tebakan = input("Masukkan tebakan kamu: ").lower()

# Memeriksa tebakan
if tebakan == nama_rahasia:
    print("Selamat! Kamu menebak dengan benar!")
else:
    print(f"Oops, tebakan kamu salah. Nama rahasianya adalah {nama_rahasia.capitalize()}.")
