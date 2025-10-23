# TRY-EXCEPT
try:
    angka = int(input("Masukan angka: "))
    hasil = 10 / angka
    print(f"Hasilnya adalah: {angka}")
except ZeroDivisionError:
    print("Ups! Angka tidak boleh nol. Coba lagi!")