# Gabungkan String dengan Nama

# Program ini tujuannya untuk menyapa seseorang dengan menuliskan namanya.
# Jadi nanti komputer akan bilang "Halo, Akas!" di layar.

# Baris pertama:
nama = "Akas"
# Di sini kita membuat sebuah "variabel" bernama "nama".
# Variabel itu seperti kotak tempat menyimpan sesuatu.
# Nah, isi kotak ini adalah tulisan (teks) "Akas".
# Tanda kutip (" ") menunjukkan bahwa isinya adalah teks, bukan angka.
# Jadi sekarang kalau kita bilang "nama", komputer tahu kalau isinya adalah "Akas".

# Baris kedua:
salam = "Halo, " + nama + "!"
# Nah, sekarang kita buat variabel baru bernama "salam".
# Di dalamnya kita gabungkan beberapa potongan teks menjadi satu.
# Tanda plus (+) di sini bukan untuk menjumlahkan angka, tapi untuk MENYAMBUNG teks.
# Jadi "Halo, " + nama + "!" artinya:
#   - Ambil teks "Halo, "
#   - Tambahkan isi dari "nama" (yaitu "Akas")
#   - Tambahkan tanda seru "!"
# Kalau kita sambung semuanya jadi satu kalimat: "Halo, Akas!"
# Itulah isi dari variabel "salam".

# Baris ketiga:
print(salam)
# "print" artinya: tampilkan di layar.
# Jadi komputer akan menulis isi dari variabel "salam".
# Karena tadi "salam" isinya "Halo, Akas!", maka yang muncul di layar adalah:

# Halo, Akas!
