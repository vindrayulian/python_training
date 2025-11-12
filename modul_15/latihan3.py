# Mengukur Panjang String

# Program ini akan menampilkan nama seseorang dan menghitung
# berapa banyak huruf yang ada di dalam nama tersebut.

# Baris pertama:
nama = "Akasyah"
# Di sini kita membuat variabel bernama "nama".
# Variabel itu seperti kotak penyimpanan.
# Nah, isi kotak ini adalah tulisan (teks) "Akasyah".
# Tanda kutip (" ") menunjukkan bahwa isinya adalah teks, bukan angka.

# Jadi sekarang, kalau kita bilang "nama",
# komputer tahu bahwa isinya adalah tulisan "Akasyah".

# Baris kedua:
panjang = len(nama)
# Nah, ini bagian penting! Kita pakai fungsi "len()".
# "len" berasal dari kata "length" dalam bahasa Inggris, yang artinya "panjang".
# Tapi jangan salah — di sini "panjang" bukan ukuran baju 😄,
# tapi jumlah huruf dalam tulisan!
#
# Jadi "len(nama)" artinya: hitung berapa banyak huruf di dalam kata "Akasyah".
# Kalau kita hitung satu-satu:
# A (1), k (2), a (3), s (4), y (5), a (6), h (7)
# Jumlahnya ada 7 huruf.
#
# Jadi hasil dari "len(nama)" adalah angka 7.
# Angka ini kemudian disimpan di dalam variabel "panjang".

# Baris ketiga:
print("Nama Kamu adalah", nama, "dan nama kamu memiliki panjang", panjang, "Huruf")
# "print" artinya: tampilkan di layar.
# Di sini kita menampilkan beberapa hal sekaligus:
# - Tulisan "Nama Kamu adalah"
# - Isi dari variabel "nama" (yaitu "Akasyah")
# - Tulisan "dan nama kamu memiliki panjang"
# - Isi dari variabel "panjang" (yaitu 7)
# - Dan tulisan "Huruf"
#
# Python akan menampilkan semuanya dengan memberi spasi otomatis di antaranya.
# Jadi hasilnya nanti akan terlihat seperti ini:

# Nama Kamu adalah Akasyah dan nama kamu memiliki panjang 7 Huruf
