# TRY-EXCEPT
try:
    angka = int(input("Masukan angka Favorit kamu: "))
    print(f"Wow angka favorit kamu adalah {angka}")
    hasil = 10 / angka
except ValueError:
    print("Ups! yang kamu masukan bukan angka, Coba lagi, ya!!")