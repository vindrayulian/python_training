try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    hasil = angka1 / angka2
    print("Hasilnya adalah:", hasil)

except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")

except:
    print("Masukkan harus berupa angka ya!")
