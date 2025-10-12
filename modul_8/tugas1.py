# Mmebuat game sederhana tebak angka
angka = 10

tebakan = int(input("Masukan Angka yang kamu tebak dari 1 sampai 10: "))

if tebakan == angka:
    print("Yeay, Kamu menebak angka yang benar")
else:
    print("Yah.. tebakan kamu belum tepat")
    
    
# ====== Bisa lebih Kompleks pakai random dari python ======

# Mmebuat game sederhana tebak angka menggunakan random
import random

angka = random.randint(1, 10)

tebakan = int(input("Masukan Angka yang kamu tebak dari 1 sampai 10: "))

if tebakan == angka:
    print("Yeay, Kamu menebak angka yang benar")
else:
    print("Yah.. tebakan kamu belum tepat")