# Program ini akan menampilkan angka dari 1 sampai 10,
# tapi kali ini, kalau ketemu angka 5, dia TIDAK berhenti total.
# Dia cuma "melewati" angka 5 dan lanjut ke angka berikutnya.

# "for" artinya: lakukan sesuatu berulang-ulang (kayak main berulang-ulang 😄)
# Setelah "for" ada kata "angka", yang artinya sebuah wadah untuk menyimpan angka yang sedang dikerjakan.
# Jadi setiap kali komputer mengulang, isi wadah "angka" akan berubah:
# pertama 1, lalu 2, lalu 3, dan seterusnya.

# Sekarang lihat bagian "in range(1, 11)".
# "range(1, 11)" artinya: buat daftar angka mulai dari 1 sampai sebelum 11.
# Kenapa "sebelum 11"? Karena Python selalu BERHENTI satu angka sebelum batas yang kamu tulis.
# Jadi hasilnya: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# Ibaratnya kamu bilang ke teman: “Hitung dari 1 sampai sebelum 11,”
# berarti kamu cuma sampai 10 aja 😄

for angka in range(1, 11):
    # Sekarang komputer akan mulai membaca satu per satu angka dari daftar itu.
    # Pertama angka = 1, lalu 2, lalu 3, dan seterusnya sampai 10.

    # Di sini kita punya perintah "if angka == 5:"
    # Artinya: kalau angka yang sedang dibaca adalah 5, maka lakukan sesuatu.
    if angka == 5:
        # Nah, di sini ada perintah "continue".
        # "continue" artinya: lewati yang ini, lanjut ke langkah berikutnya.
        # Jadi komputer akan bilang:
        # "Oh, ini angka 5 ya? Oke, aku nggak mau cetak angka 5, aku lanjut aja ke angka selanjutnya!"
        continue  # artinya: lompat ke atas lagi dan lanjut ke angka berikutnya

    # Kalau angka-nya bukan 5, maka perintah "print(angka)" dijalankan.
    # "print" artinya: tampilkan angka di layar.
    print(angka)

# Jadi hasilnya di layar adalah:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
# Karena angka 5 dilewati oleh "continue", dia tidak muncul di layar.

# Yuk kita simpulkan satu per satu dengan cara mudah:
# ---------------------------------------------------
# - "for" = ulangi terus sesuatu
# - "angka" = tempat menyimpan angka sementara
# - "range(1, 11)" = daftar angka dari 1 sampai sebelum 11 (jadi sampai 10)
# - "if angka == 5" = kalau angka sekarang 5
# - "continue" = lewati angka ini, lanjut ke angka berikutnya
# - "print(angka)" = tampilkan angka di layar
