def tambah_lima(angka):
    hasil = angka + 5
    return hasil

angka_masuk = int(input("Masukan angka untuk ditambahkan 5: "))
jawaban = tambah_lima(angka_masuk)
print(f"Hasil dari {angka_masuk} ditambahkan 5 adalah {jawaban}")