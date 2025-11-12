# Program ini akan menampilkan angka 1 sampai 10.
# Tapi nanti programnya akan berhenti kalau sudah sampai angka 5.

# Sekarang kita bahas satu per satu, dengan cara yang mudah dipahami ya! 😄

# "for" artinya: lakukan sesuatu berulang-ulang.
# Jadi kalau kamu lihat "for" di Python, bayangkan kamu sedang menyuruh komputer:
# "Hei komputer, tolong ulangi hal ini beberapa kali ya!"

# Setelah "for" ada kata "angka".
# Nah, "angka" ini seperti wadah atau kotak kecil.
# Kotak ini nanti akan berisi angka yang berganti setiap kali perulangan.
# Jadi pertama isi kotaknya 1, lalu 2, lalu 3, dan seterusnya.

# Sekarang kita lihat bagian "in range(1, 11)".
# "range" itu seperti alat pembuat daftar angka.
# Kalau ditulis "range(1, 11)", artinya:
# "Buat daftar angka mulai dari 1 sampai sebelum 11."
# Loh, kenapa sebelum 11? Kok nggak sampai 11 juga?
# Karena Python itu menghitung dari angka pertama, tapi BERHENTI sebelum angka terakhir.
# Jadi "range(1, 11)" hasilnya adalah:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# Angka 11-nya tidak ikut, karena Python menganggap angka terakhir (11) adalah "batas berhenti".
# Ibaratnya kayak kamu bilang ke teman:
# "Lari dari tiang nomor 1 sampai sebelum tiang nomor 11" — berarti kamu cuma lari sampai tiang nomor 10 😄

for angka in range(1, 11):
    # Sekarang, setiap kali perulangan, isi "angka" berubah.
    # Di putaran pertama: angka = 1
    # Di putaran kedua: angka = 2
    # Di putaran ketiga: angka = 3
    # ... dan begitu terus sampai 10.

    # "if angka == 5:" dibaca "kalau angka sama dengan 5"
    # Tanda "==" artinya kita sedang membandingkan, bukan memberi nilai.
    # Jadi ini bukan "angka jadi 5", tapi "apakah angka sekarang 5?"

    if angka == 5:
        # Kalau benar (angka memang 5), maka jalankan "break".
        # "break" artinya: berhenti total dari perulangan.
        # Bayangkan kamu lagi menghitung "1... 2... 3... 4..." lalu seseorang bilang "STOP!"
        # Nah, kamu langsung berhenti dan nggak lanjut ke 5, 6, 7, 8, 9, 10.

        break  # artinya berhenti dari pengulangan sekarang juga

    # Kalau belum sampai 5, maka program lanjut ke baris ini.
    # "print(angka)" artinya tampilkan isi "angka" di layar.
    # Jadi di layar nanti muncul angka-angka yang sudah dilewati.

    print(angka)

# Karena kita tadi berhenti saat angka = 5,
# hasil yang muncul di layar cuma:
# 1
# 2
# 3
# 4

# Setelah itu, komputer tidak mencetak apa-apa lagi karena "break" sudah menghentikan perulangan.

# Jadi kesimpulannya:
# - "for" = ulangi terus sesuatu
# - "angka" = tempat menyimpan angka sementara
# - "range(1, 11)" = daftar angka dari 1 sampai sebelum 11 (yaitu sampai 10)
# - "if angka == 5" = kalau angka sekarang adalah 5
# - "break" = stop, hentikan perulangan!
# - "print(angka)" = tampilkan angka di layar
