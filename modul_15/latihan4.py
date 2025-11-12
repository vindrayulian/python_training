# Mengubah huruf besar dan kecil


# Program ini menunjukkan cara mengubah huruf pada tulisan.
# Komputer bisa membuat semua huruf jadi BESAR atau jadi kecil semua.
# Yuk kita lihat satu per satu!

# Baris pertama:
kata = "Belajar itu seru!"
# Di sini kita membuat variabel bernama "kata".
# Variabel itu seperti kotak penyimpanan, dan isi kotaknya adalah tulisan (teks) "Belajar itu seru!".
# Jadi kalau kita bilang "kata", komputer tahu kalau isinya kalimat itu.

# Baris kedua:
print(kata.upper())  # Semua huruf jadi besar
# "print" artinya: tampilkan hasil di layar.
# Tapi kali ini, sebelum ditampilkan, kita menambahkan ".upper()" di belakang variabel "kata".
# Nah, ".upper()" adalah perintah khusus untuk MENGUBAH semua huruf menjadi huruf BESAR.
# Bayangkan kamu menulis "Belajar itu seru!" di keyboard, lalu pencet tombol CAPS LOCK 😆
# Maka hasilnya akan jadi:
# BELAJAR ITU SERU!

# Jadi "kata.upper()" artinya: ambil isi dari "kata", lalu ubah semua hurufnya jadi huruf besar.

# Baris ketiga:
print(kata.lower())  # Semua huruf jadi kecil
# Ini kebalikannya dari yang tadi.
# ".lower()" artinya: ubah semua huruf menjadi huruf kecil.
# Bayangkan kamu menulis pelan-pelan tanpa menekan tombol Shift atau Caps Lock.
# Jadi hasilnya akan jadi:
# belajar itu seru!

# Jadi "kata.lower()" artinya: ambil isi dari "kata", lalu ubah semua hurufnya jadi huruf kecil.

# Kesimpulan:
# - "upper()" = semua huruf jadi besar (SEPERTI INI!)
# - "lower()" = semua huruf jadi kecil (seperti ini 😄)
# - "print()" = tampilkan hasilnya di layar

# Maka saat program dijalankan, hasil di layar akan seperti ini:
# BELAJAR ITU SERU!
# belajar itu seru!
