import calendar

# Meminta pengguna memasukan tahun dan bulan
tahun = int(input("Masukan tahun: "))

# Menampilkan kalender kecil
print("\nKalender untuk Tahun tersebut:\n")
print(calendar.calendar(tahun))