# Di baris ini, kita membuat sebuah tulisan dan menyimpannya di dalam kotak bernama 'kata'
# Tulisan yang kita simpan adalah "Komputer dan Leptop"
kata = "Komputer dan Leptop"

# Nah, sekarang kita ingin tahu ada berapa banyak huruf di dalam tulisan itu
# Fungsi len() di Python bisa menghitung jumlah semua karakter (huruf, angka, tanda, bahkan spasi!)
# Jadi len(kata) akan menghitung semuanya satu per satu
huruf = len(kata)

# Sekarang kita ingin menampilkan hasil hitungannya ke layar
# print() akan menulis kalimat yang kita mau ke layar
# Jadi nanti di layar akan muncul:
# Jumlah huruf yang ada pada kata Komputer dan Leptop adalah: 19 huruf
print("Jumlah huruf yang ada pada kata", kata, "adalah:", huruf, "huruf")
