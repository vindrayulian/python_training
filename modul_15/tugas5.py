while True:
    nama = input("Ketik nama kamu: ")
    if nama.islower():
        print("Program selesai! Kamu mengetik huruf kecil semua.")
        break
    else:
        print("Nama kamu belum huruf kecil semua, coba lagi ya!\n")