# Program ini membuat komputer menyapa seseorang dengan menyebutkan namanya.
# Jadi nanti hasilnya seperti: "Hallo Vindra Arya Yulian!"

# Baris pertama:
nama = "Vindra Arya Yulian"
# Di sini kita membuat variabel bernama "nama".
# Variabel itu seperti kotak kecil tempat menyimpan sesuatu.
# Nah, isi kotak ini adalah teks (tulisan) "Vindra Arya Yulian".
# Tanda kutip (" ") menunjukkan bahwa yang disimpan adalah tulisan, bukan angka.
# Jadi sekarang kalau kita tulis "nama", komputer tahu bahwa isinya adalah tulisan nama lengkap itu.

# Baris kedua:
salam = "Hallo " + nama + "!"
# Nah, di sini kita membuat variabel baru bernama "salam".
# Variabel ini akan menyimpan kalimat sapaan yang digabung dari beberapa bagian.
#
# Perhatikan ada tanda plus (+) di sini.
# Dalam teks, tanda plus digunakan bukan untuk menjumlahkan angka,
# tapi untuk **menyambungkan (menggabungkan)** beberapa potongan tulisan jadi satu kalimat.
#
# Mari kita lihat satu per satu potongannya:
#   "Hallo "   → kata sapaan (dengan spasi di belakang supaya nanti tidak menempel dengan nama)
#   + nama      → ambil isi dari variabel "nama" (yaitu "Vindra Arya Yulian")
#   + "!"       → tambahkan tanda seru di akhir kalimat biar terdengar semangat 😄
#
# Jadi kalau semua digabung hasilnya menjadi:
# "Hallo Vindra Arya Yulian!"

# Baris ketiga:
print(salam)
# "print" artinya: tampilkan hasil di layar.
# Jadi komputer akan menampilkan isi dari variabel "salam".
#
# Karena isi "salam" adalah "Hallo Vindra Arya Yulian!",
# maka yang muncul di layar adalah:
#
# Hallo Vindra Arya Yulian!
