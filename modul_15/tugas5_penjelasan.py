# Kita buat program yang akan terus meminta nama dari pengguna (anak yang mengetik)
# Program baru akan berhenti kalau nama yang diketik semuanya huruf kecil, misalnya "budi"

while True:  # Artinya: lakukan terus-menerus tanpa berhenti
    nama = input("Ketik nama kamu: ")  # Minta pengguna mengetik nama

    # Sekarang kita cek, apakah semua huruf di nama itu huruf kecil?
    # Fungsi .islower() akan mengembalikan 'True' kalau semuanya huruf kecil
    if nama.islower():
        print("Program selesai! Kamu mengetik huruf kecil semua.")
        break  # 'break' artinya: keluar dari perulangan (berhenti)
    else:
        print("Nama kamu belum huruf kecil semua, coba lagi ya!\n")
