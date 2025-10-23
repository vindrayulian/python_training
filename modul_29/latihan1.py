import calendar

# Meminta pengguna memasukan tahun dan bulan
tahun = int(input("Masukan tahun: "))
bulan = int(input("Masukan bulan (1-12): "))

# Menampilkan kalender kecil
print("\nKalender untuk bulan tersebut:\n")
print(calendar.month(tahun, bulan))