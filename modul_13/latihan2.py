angka_rahasia = 7
tebakan = 0

while tebakan != angka_rahasia: # Selama tebakan salah
    tebakan = int(input("Tebak angka (1-10):"))
    if tebakan == angka_rahasia:
        print("Selamat, Kamu benar!")
    else:
        print("Coba lagi!")