from datetime import date

# Ambil tanggal hari ini
today = date.today()

print("=== Program Menghitung Umur ===")
# Input tanggal lahir
tahun_lahir = int(input("Masukkan tahun lahir kamu: "))
bulan_lahir = int(input("Masukkan bulan lahir kamu (1-12): "))
hari_lahir = int(input("Masukkan tanggal lahir kamu (1-31): "))

# Buat objek tanggal lahir
tgl_lahir = date(tahun_lahir, bulan_lahir, hari_lahir)

# Hitung selisih tanggal
umur_tahun = today.year - tgl_lahir.year
umur_bulan = today.month - tgl_lahir.month
umur_hari = today.day - tgl_lahir.day

# Koreksi jika bulan/hari belum lewat
if umur_hari < 0:
    umur_bulan -= 1
    # Hitung jumlah hari di bulan sebelumnya
    bulan_sebelumnya = today.month - 1 or 12
    tahun_sebelumnya = today.year if today.month != 1 else today.year - 1
    hari_dalam_bulan = (date(tahun_sebelumnya, bulan_sebelumnya % 12 + 1, 1) - date(tahun_sebelumnya, bulan_sebelumnya, 1)).days
    umur_hari += hari_dalam_bulan

if umur_bulan < 0:
    umur_tahun -= 1
    umur_bulan += 12

# Tentukan kategori umur
if umur_tahun < 10:
    kategori = "Anak-anak"
elif umur_tahun < 18:
    kategori = "Remaja"
else:
    kategori = "Dewasa"

# Tampilkan hasil
print("\n=== Hasil Perhitungan ===")
print(f"Kamu {kategori}. Umur kamu: {umur_tahun} tahun, {umur_bulan} bulan, dan {umur_hari} hari.")

# Cek apakah hari ini ulang tahun
if today.day == hari_lahir and today.month == bulan_lahir:
    print("🎉 Selamat Ulang Tahun!!! Semoga panjang umur dan bahagia selalu! 🥳")
