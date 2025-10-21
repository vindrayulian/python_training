import random

# Daftar kata yang akan digunakan dalam permainan
kata_rahasia = ["BURUNG", "SEPEDA", "BUNGA", "PANDA", "MOBIL"]

# Pilih kata rahasia secara acak
kata = random.choice(kata_rahasia)

# Buat daftar untuk melacak huruf yang sudah ditebak
tebakan = ["_"] * len(kata)
huruf_tertebak = []

# Jumlah maksimal tebakan salah
kesempatan = 6

print("Selamat datang di permainan Tebak Huruf pada Kata!")
print("Tebak kata rahasia dengan menebak huruf satu per satu.")
print("Kata rahasia memiliki", len(kata), "huruf.")
print("Kamu punya", kesempatan, "kesempatan salah. Ayo mulai!\n")

# Mulai permainan
while kesempatan > 0 and "_" in tebakan:
    print("Kata saat ini:", "".join(tebakan))
    huruf = input("Tebak satu huruf: ").upper()
    
    # Periksa apakah huruf sudah ditebak sebelumnya
    if huruf in huruf_tertebak:
        print("Kamu sudah menebak huruf ini, coba huruf lain!")
        continue
    
    huruf_tertebak.append(huruf)
    
    # Periksa apakah huruf ada di kata rahasia
    if huruf in kata:
        print("Betul! Huruf", huruf, "ada di kata.")
        for i in range(len(kata)):
            if kata[i] == huruf:
                tebakan[i] = huruf
    else:
        print("Maaf, huruf", huruf, "tidak ada di kata.")
        kesempatan -= 1
        print("Kesempatan tersisa:", kesempatan)
    
    # Periksa hasil akhir
    if "_" not in tebakan:
        print("\n🎉 Selamat! Kamu berhasil menebak kata:", kata)
        break
else:
    print("\n😢 Kesempatan habis. Kata rahasianya adalah:", kata)

print("\nTerima kasih sudah bermain!")


