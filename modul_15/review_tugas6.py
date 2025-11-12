# Program Latihan Gabungan String dan Perulangan (dengan komentar sangat detail)
# Dibuat untuk anak usia 8-9 tahun — setiap baris diberi penjelasan lengkap di komentar.
# Tujuan program:
# 1) Menerima input nama, lalu menampilkan nama dalam huruf BESAR (semua kapital).
# 2) Menerima 1 kata dari pengguna, mengulang kata itu 3 kali berturut-turut.
# 3) Menghitung panjang nama (jumlah karakter) menggunakan len().
# 4) Mengulang seluruh proses sampai pengguna mengetik "exit" (dengan pengecekan case-insensitive).
#
# Catatan kecil:
# - input() membaca apa saja yang diketik sampai Enter, termasuk spasi.
# - len() menghitung semua karakter dalam string — termasuk spasi dan tanda baca.
# - .upper() dan .lower() tidak mengubah string asli jika kita tidak menyimpan kembali hasilnya.
# - Kita menyimpan hasilnya kembali agar perubahan berlaku (mis. nama = nama.upper()).

# Perulangan utama: while True -> loop tanpa henti sampai kita break
while True:
    # ---------------------------
    # Bagian input nama
    # ---------------------------
    # input("...") -> menampilkan teks di layar dan menunggu anak mengetik lalu tekan Enter.
    # .strip() digunakan untuk menghilangkan spasi di awal dan akhir yang tidak perlu.
    # Contoh: jika anak mengetik "  akas  " maka .strip() -> "akas"
    nama = input("Masukkan nama kamu: ").strip()
    # Jika anak menekan Enter tanpa mengetik apa-apa, nama akan menjadi string kosong "".
    # Kita bisa menambahkan pengecekan agar tidak menerima nama kosong.
    if nama == "":
        # Memberi tahu dan langsung lanjut ke awal loop untuk minta nama lagi.
        print("Kamu belum mengetik nama — coba lagi ya :)")
        # continue langsung lompat ke awal while, tidak menjalankan sisa kode di bawah.
        continue

    # Buat nama tampil SEMUA HURUF BESAR sesuai permintaan.
    # contoh: "akas" -> "AKAS", "Akas" -> "AKAS"
    # alasan: memudahkan konsistensi tampilan dan latihan fungsi .upper()
    nama = nama.upper()

    # ---------------------------
    # Bagian input kata yang akan diulang
    # ---------------------------
    # Kita beri instruksi agar anak mengetik satu kata. Namun jika mereka mengetik beberapa kata,
    # program ini tetap akan mengulang seluruh string yang diketik (kata1 kata2 ...).
    # Jika ingin memaksa hanya kata pertama, bisa pakai: kata.split()[0]
    kata = input("Masukkan satu kata untuk diulang 3x: ").strip()

    # Jika anak tidak mengetik apa-apa, kita beri peringatan dan minta ulang kata.
    if kata == "":
        print("Kamu belum mengetik kata untuk diulang — coba lagi ya :)")
        # Kita minta ulang hanya bagian kata (bukan nama). Untuk sederhana, lakukan loop kecil:
        while kata == "":
            kata = input("Masukkan satu kata untuk diulang 3x (jangan kosong): ").strip()

    # Ulangi kata 3 kali berturut-turut menggunakan operator perkalian string.
    # Contoh: jika kata = "Ayo", maka kata * 3 -> "AyoAyoAyo"
    # Jika ingin ada spasi antar pengulangan: (kata + " ") * 3 lalu .strip() untuk hilangkan spasi akhir.
    ulang = kata * 3
    # contoh alternatif dengan spasi antar pengulangan:
    # ulang_spasi = (kata + " ") * 3
    # ulang_spasi = ulang_spasi.strip()  # menghilangkan spasi terakhir

    # ---------------------------
    # Menghitung panjang nama
    # ---------------------------
    # len(nama) menghitung jumlah karakter dalam string nama.
    # Karena kita sudah mengubah nama menjadi uppercase, panjangnya sama sebelum/ sesudah .upper()
    panjang = len(nama)
    # PENJELASAN DETAIL: jika nama = "A K A S" (ada spasi), len = 7 (termasuk spasi).
    # Jika ingin menghitung hanya huruf (tanpa spasi), bisa:
    # panjang_hanya_huruf = len(nama.replace(" ", ""))

    # ---------------------------
    # Menampilkan hasil ke layar (output)
    # ---------------------------
    # Kita gabungkan teks dengan koma atau +; penggunaan koma otomatis menambahkan spasi antar item.
    # print("Halo,", nama + "!") -> menampilkan "Halo, AKAS!"
    print("Halo,", nama + "!")  # salam dengan nama yang sudah kapital
    # Tampilkan hasil pengulangan kata
    print("Kata yang kamu pilih diulang 3x menjadi:", ulang)
    # Tampilkan panjang nama
    # Kita gunakan koma dalam print agar Python otomatis menambahkan spasi yang rapi.
    print("Nama kamu memiliki panjang", panjang, "huruf.")
    # Jika ingin menjelaskan lebih rinci:
    # print(f"Nama kamu ('{nama}') terdiri dari {panjang} karakter (termasuk spasi jika ada).")

    # ---------------------------
    # Bagian pilihan: lanjut atau keluar
    # ---------------------------
    # Tanyakan apakah anak ingin memasukkan nama lagi atau keluar.
    # Kita minta mereka mengetik 'exit' untuk keluar. Namun agar tidak sensitif huruf besar/kecil:
    pilihan = input("Apakah kamu ingin memasukkan nama lagi? (ketik 'exit' untuk keluar): ").strip()
    # Ubah jawaban menjadi huruf kecil semua agar input seperti "EXIT", "Exit", "eXiT" tetap dikenali.
    pilihan = pilihan.lower()

    # Jika pengguna mengetik "exit" (setelah di-lower), kita break dari loop.
    if pilihan == "exit":
        print("Program selesai. Terima kasih sudah belajar Python! 👋")
        # break keluar dari while True -> program selesai
        break
    else:
        # Jika bukan "exit", maka anggap pengguna ingin mengulangi program.
        # Kita beri tahu dan loop akan kembali dari atas (while True) sehingga minta nama lagi.
        # Note: kita tidak perlu menulis "continue" karena sudah sampai akhir loop; sementara loop akan lanjut.
        print("Oke, kita coba lagi — masukkan data berikutnya. 😊")
        # setelah print, loop otomatis kembali ke awal untuk meminta nama baru.

# ---------------------------
# Catatan tambahan (tidak dijalankan, hanya untuk pembelajaran)
# ---------------------------
# 1) Kenapa pakai .strip()? -> supaya input tidak salah diakibatkan spasi tak sengaja.
# 2) Kenapa pakai .upper() untuk nama? -> agar tampilan seragam dan anak belajar fungsi string.
# 3) Kenapa len(nama) menghitung spasi? -> karena len() menghitung semua karakter; jika mau hitung hanya huruf, hilangkan spasi dulu.
# 4) Operator * untuk string bukan perkalian angka, melainkan pengulangan string pada Python.
# 5) Perbandingan string bersifat case-sensitive kecuali kita ubah case dulu (.lower() atau .upper()).
# 6) Selalu pikirkan kemungkinan input kosong — bagus untuk dilatih menangani error sederhana.
#
# Contoh interaksi program:
# Masukkan nama kamu: akas
# Masukkan satu kata untuk diulang 3x: ayo
# Halo, AKAS!
# Kata yang kamu pilih diulang 3x menjadi: ayoayoayo
# Nama kamu memiliki panjang 4 huruf.
# Apakah kamu ingin memasukkan nama lagi? (ketik 'exit' untuk keluar): exit
# Program selesai. Terima kasih sudah belajar Python!
#
# Sekian penjelasan detailnya — jika mau, aku bisa ubah:
# - agar pengulangan kata ada spasi antar kata,
# - menghitung panjang hanya huruf (tanpa spasi),
# - atau menampilkan nomor urut percobaan (Percobaan ke-1, ke-2, dst).
