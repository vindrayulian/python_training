daftar_belanja = []

while True:
    print("\nApa yang ingin kamu lakukan?")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Lihat daftar belanja")
    print("4. Selesai")
    
    pilihan = input("Pilih 1, 2, 3, atau 4: ")
    
    if pilihan == "1":
        barang = input("Masukan nama barang yang ingin ditambahkan: ")
        daftar_belanja.append(barang)
        print(f"{barang} sudah ditambahkan ke daftar.")
    elif pilihan == "2":
        print(daftar_belanja)
        barang = input("Masukan nama barang yang ingin dihapus: ")
        if barang in daftar_belanja:
            daftar_belanja.remove(barang)
            print(f"{barang} sudah berhasil di hapus dari daftar.")
        else:
            print(f"{barang} tidak ada pada daftar belanja.")
    elif pilihan == "3":
        print("Daftar belanja Kamu:", daftar_belanja)
    elif pilihan == "4":
        print("Selesai belanja. Daftar akhir kamu:", daftar_belanja)
        break
    else:
        print("Pilihan tidak valid. Coba lagi!")