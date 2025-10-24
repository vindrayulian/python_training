# Game tebak angka

import random

angka_rahasia = random.randint(1, 10)
tebakan = 0

print("Halo! Aku punya angka rahasia dari 1 sampai 10, Coba tebak!")

while tebakan != angka_rahasia:
    tebakan = int(input("Masukan tebakanmu: "))
    if tebakan < angka_rahasia:
        print("Terlalu kecil! Coba lagi.")
    elif tebakan > angka_rahasia:
        print("Terlalu besar! Coba lagi.")
    else:
        print("Hore! Kamu benar!")