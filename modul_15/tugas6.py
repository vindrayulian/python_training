while True:
    nama = input("Masukkan nama kamu: ").strip()
    if nama == "":
        print("Kamu belum mengetik nama — coba lagi ya :)")
        continue
    nama = nama.upper()
    
    kata = input("Masukkan satu kata untuk diulang 3x: ").strip()
    if kata == "":
        print("Kamu belum mengetik kata untuk diulang — coba lagi ya :)")
        while kata == "":
            kata = input("Masukkan satu kata untuk diulang 3x (jangan kosong): ").strip()
    ulang = kata * 3
    
    panjang = len(nama)
    
    print("Halo,", nama + "!") 
    print("Kata yang kamu pilih diulang 3x menjadi:", ulang)
    print("Nama kamu memiliki panjang", panjang, "huruf.")
    
    pilihan = input("Apakah kamu ingin memasukkan nama lagi? (ketik 'exit' untuk keluar): ").strip()
    pilihan = pilihan.lower()

    if pilihan == "exit":
        print("Program selesai. Terima kasih sudah belajar Python! 👋")
        break
    else:
        print("Oke, kita coba lagi — masukkan data berikutnya. 😊")
