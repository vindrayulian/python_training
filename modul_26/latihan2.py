# Menambah banyak pertanyaan

# Daftar teka-teki dan jawaban
teka_teki = {
    "Aku punya ekor panjang, tapi bukan kucing. Aku suka berayun di pohon. Siapakah aku?": "monyet",
    "Aku bulat, suka memantul, dan sering dimainkan di lapangan. Siapakah aku?": "bola",
    "Aku punya sayap, tapi aku bukan burung. Aku suka menghisap madu. Siapakah aku?": "lebah",
    "Aku putih, keluar dari sapi, dan sering diminum saat sarapan. Siapakah aku?": "susu",
    "Aku bersinar di langit malam, tapi aku bukan bulan. Siapakah aku?": "bintang",
    "Aku bisa menampung air, tapi bukan ember. Aku besar dan biru. Siapakah aku?": "laut",
    "Aku punya jarum tapi bukan tukang jahit. Aku berputar setiap waktu. Siapakah aku?": "jam",
    "Aku bisa dimakan, kulitku berwarna kuning, dan monyet suka padaku. Siapakah aku?": "pisang",
    "Aku selalu datang di pagi hari dan menghilang saat malam. Siapakah aku?": "matahari",
    "Aku bisa membuatmu basah, turun dari langit, tapi bukan embun. Siapakah aku?": "hujan",
    "Aku punya roda dan berjalan di jalan, tapi bukan sepeda motor. Siapakah aku?": "mobil",
    "Aku kecil, tapi bisa menyala di kegelapan. Siapakah aku?": "lilin",
    "Aku bisa terbang, tapi aku bukan burung. Aku punya baling-baling. Siapakah aku?": "helikopter",
    "Aku terbuat dari karet dan dipakai di kaki. Siapakah aku?": "sandal",
    "Aku berwarna hijau, hidup di air dan darat. Siapakah aku?": "katak",
    "Aku digunakan untuk menulis, tapi bukan pensil. Siapakah aku?": "pena",
    "Aku tumbuh di tanah, daunku hijau, dan sering dimasak. Siapakah aku?": "sayur",
    "Aku berwarna merah, rasanya manis, dan sering dijadikan jus. Siapakah aku?": "stroberi",
    "Aku berbunyi ketika dipukul, dan sering digunakan di sekolah. Siapakah aku?": "bel",
    "Aku selalu berputar di atas kepala saat panas terik. Siapakah aku?": "kipas"
}

print("Selamat datang di kuis Teka-Teki! ☺️")
print("Jawab dengan kata yang tepat, Siap? Yuk kita mulai! \n")

# Variable untuk skor
skor = 0

# Mulai kuis
for pertanyaan, jawaban_benar in teka_teki.items():
    print(pertanyaan)
    jawaban_pemain = input("Jawaban kamu: ").lower()  # Mengubah jawaban ke huruf kecil
    if jawaban_pemain == jawaban_benar:
        print("Benar! 🎉")
        skor += 1
    else:
        print(f"Salah, jawaban yang benar adalah: {jawaban_benar} ☺️")
    print()  # Baris kosong untuk jarak

# Tampilan skor akhir
print(f"Kuis selesai! Skor akhir kamu: {skor}/{len(teka_teki)}")
if skor == len(teka_teki):
    print("Kamu luar biasa! 🏆")
else:
    print("Coba lagi untuk skor yang sempurna! 💪")
