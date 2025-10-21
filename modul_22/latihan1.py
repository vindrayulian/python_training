# Membuat fungsi untuk menghitung luas persegi
def hitung_luas_persegi(sisi):
    luas = sisi * sisi # Menghitung luas
    return luas # Mengembalikan hasil

# Memanggil fungsi
sisi_persegi = 4 # Panjang sisi persegi
hasil = hitung_luas_persegi(sisi_persegi)
print(f"Luas persegi dengan sisi {sisi_persegi} cm adalah {hasil} cm2")