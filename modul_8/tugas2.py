# Program memberikan saran saat cuaca yang sedang terjadi

# Membuat variabel untuk menyimpan cuaca

cuaca = int(input("Masukan suhu cuaca hari ini: "))

if cuaca < 35:
    print("Sejuk, Nikmati Cuaca")
else:
    print("Panas, Minum es teh")