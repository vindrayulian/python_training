# Program kalkulator dengan menambahkan fitur sapaan sesuai jam

from datetime import datetime

# Fungsi untuk menyapa pengguna berdasarkan waktu
def sapa_pengguna():
    jam_sekarang = datetime.now().hour

    if 5 <= jam_sekarang < 12:
        return "Selamat pagi! 🌅"
    elif 12 <= jam_sekarang < 15:
        return "Selamat siang! ☀️"
    elif 15 <= jam_sekarang < 18:
        return "Selamat sore! 🌇"
    else:
        return "Selamat malam! 🌙"


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
        return "Tidak bisa membagi dengan nol!"

def pangkat(a, b):
    return a ** b


# Program Utama
print("====================================")
print(sapa_pengguna())
print("Selamat datang di kalkulator Mainan! 😊")
print("Pilih operasi: tambah, kurang, kali, bagi, pangkat")
print("====================================")

operasi = input("Masukan operasi yang diinginkan: ").lower()

# Meminta angka dari pengguna
angka1 = float(input("Masukan angka pertama: "))
angka2 = float(input("Masukan angka kedua: "))

# Menentukan Operasi
if operasi == "tambah":
    hasil = tambah(angka1, angka2)
elif operasi == "kurang":
    hasil = kurang(angka1, angka2)
elif operasi == "kali":
    hasil = kali(angka1, angka2)
elif operasi == "bagi":
    hasil = bagi(angka1, angka2)
elif operasi == "pangkat":
    hasil = pangkat(angka1, angka2)
else:
    hasil = "Operasi tidak dikenal"

# Menampilkan hasil
print("------------------------------------")
print(f"Hasil dari {angka1} di{operasi} {angka2} adalah: {hasil}")
print("Terima kasih sudah menggunakan kalkulator Mainan! 🤖")
