# Program tebak nama rahasia teman

# Menyembunyikan nama teman
nama_rahasia = "budi"

# Menyapa pemain
print("Selamat datang di permainan Tebak Nama Rahasia Teman!")
print("Saya sudah memikirkan sebuah nama teman saya. Coba tebak siapa!")

# Meminta pemain untuk menebak
tebakan = input("Masukan tebakan kamu: ").lower()

# Memeriksa tebakan
if tebakan == nama_rahasia:
    print("Selamat! Kamu menebak dengan benar!")
else:
    print("Oops, tebakan kamu salah. Nama rahasianya adalah", nama_rahasia)