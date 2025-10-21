def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    return luas

sisi_persegi = int(input("Masukan Panjang persegi: "))
hasil = hitung_luas_persegi(sisi_persegi)

print(f"Hasil luas persegi dari panjang sisi {sisi_persegi} cm adalah {hasil} cm2")