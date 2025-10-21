# Fungsi untuk setiap operasi
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0: # Pastikan tidak membagi dengan nol
        return a / b
    else:
        return "Tidak bisa membagi dengan nol!"
    
    
# Program Utama
print("Selamat datang di kalkulator Mainan! 😊")
print("Pilih operasi tambah, kurang, kali, bagi")
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
else:
    hasil = "Operasi tidak dikenal"
    
# Menampilkan hasil
print(f"Hasil dari {angka1} di{operasi} {angka2} adalah: {hasil}")

    
