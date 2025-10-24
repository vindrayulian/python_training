# Kalender 1 tahun full

import calendar

print("Selamat datang di program kalender kecil\n")

# Meminta pengguna memasukan tahun dan bulan
tahun = int(input("Masukan tahun: "))
bulan = int(input("Masukan bulan (1-12): "))
if bulan < 1 or bulan > 12:
    print("Bulan tidak valid, masukan angka antara 1 dan 12.")
else:
    # Menampilkan kalender kecil
    print("\nKalender untuk bulan tersebut:\n")
    print(calendar.month(tahun, bulan))