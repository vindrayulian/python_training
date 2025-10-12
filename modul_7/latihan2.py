# Program Menghitung Umur
tahun_sekarang = 2025 # Sesuaikan dengan tahun sekarang
tahun_lahir = int(input("Masukan tahun lahir kamu:")) # Input untuk memasukan tahun lahir kamu
umur = tahun_sekarang - tahun_lahir # menghitung umur kamu dengan cara mengurangi tahun sekarang dengan tahun lahir

if umur < 10:
    print("Kamu masih Anak-anak, umur kamu:", umur, "Tahun.")
elif umur < 18:
    print("Kamu Remaja, umur kamu:", umur, "Tahun.")
else:
    print("Umur Kamu Sudah Dewasa, umur kamu:", umur, "Tahun.") # Menampilkan hasil perhitungan umur