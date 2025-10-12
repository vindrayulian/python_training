for i in range(1, 6):        # Baris (angka pertama)
    for j in range(1, 6):    # Kolom (angka kedua)
        hasil = i * j
        print(f"{hasil:4}", end="")  # Cetak dengan jarak supaya rapi
    print()  # Ganti baris setelah satu baris selesai
