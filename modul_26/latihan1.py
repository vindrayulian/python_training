# Daftar teka-teki dan jawaban

teka_teki = {
    "Aku punya ekor panjang, tapi bukan kucing. Aku suka berayun di pohon. Siapakah aku?": "monyet",
    "Aku bulat, suka memantul, dan sering dimainkan di lapangan. Siapakah aku?": "bola",
    "Aku punya sayap, tapi aku bukan burung, Aku suka menghisap madu. Siapakah aku?": "lebah"
}

print("Selamat datang di kuis Teka-Teki! ☺️")
print("Jawab dengan kata yang tepat, Siap? Yuk kita mulai! \n")

# Variable untuk skor
skor = 0

# Mulai kuis

for pertanyaan, jawaban_benar in teka_teki.items():
    print(pertanyaan)
    jawaban_pemain = input("Jawaban kamu: ").lower() # Mengubah jawaban ke huruf kecil
    if jawaban_pemain == jawaban_benar:
        print("Benar! 🎉")
        skor += 1
        
    else:
        print(f"Salah, jawaban yang benar adalah: {jawaban_benar} ☺️")
    print() # Baris kosong untuk jarak
    
# Tampilan skor akhir
print(f"Kuis selesai! Skor akhir kamu: {skor}/{len(teka_teki)}")
if skor == len(teka_teki):
    print("Kamu luar biasa! 🏆")
else:
    print("Coba lagi untuk skor yang sempurna! 💪")