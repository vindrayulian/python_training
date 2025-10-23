import time
import msvcrt
import sys

# Daftar teka-teki
teka_teki = {
    "Aku punya ekor panjang, tapi bukan kucing. Aku suka berayun di pohon. Siapakah aku?": "monyet",
    "Aku bulat, suka memantul, dan sering dimainkan di lapangan. Siapakah aku?": "bola",
    "Aku punya sayap, tapi aku bukan burung, aku suka menghisap madu. Siapakah aku?": "lebah",
    "Aku punya jarum tapi bukan penjahit. Aku bisa menunjukkan waktu. Siapakah aku?": "jam",
    "Aku hidup di air, punya insang, tapi bukan manusia ikan. Siapakah aku?": "ikan",
    "Aku besar, abu-abu, dan punya belalai. Siapakah aku?": "gajah",
    "Aku bisa terbang di langit malam dan suka menggantung terbalik. Siapakah aku?": "kelelawar",
    "Aku punya kulit hijau dan bisa melompat tinggi. Siapakah aku?": "katak",
    "Aku lahir dari telur, punya paruh, dan suka berenang. Siapakah aku?": "bebek",
    "Aku bisa menyala tapi aku bukan lampu. Aku bisa membakar tapi aku bukan matahari. Siapakah aku?": "api"
}

print("Selamat datang di kuis Teka-Teki! ☺️")
print("Jawab setiap pertanyaan sebelum waktu 10 detik habis!\n")

skor = 0
total = len(teka_teki)
TIME_LIMIT = 10

def input_dengan_timer(prompt, limit_waktu):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    jawaban = ""
    start = time.time()

    while True:
        sisa = int(limit_waktu - (time.time() - start))
        sys.stdout.write(f"\r⏳ Waktu tersisa: {sisa:2d} detik. Jawaban: {jawaban} ")
        sys.stdout.flush()

        if sisa <= 0:
            print("\nWaktu habis!")
            return None

        if msvcrt.kbhit():
            char = msvcrt.getwch()
            if char == "\r":
                print()
                return jawaban.strip().lower()
            elif char == "\b": 
                jawaban = jawaban[:-1]
            else:
                jawaban += char

        time.sleep(0.1)

for pertanyaan, jawaban_benar in teka_teki.items():
    print("\n" + pertanyaan)
    jawaban_pemain = input_dengan_timer("\nJawaban kamu: ", TIME_LIMIT)

    if jawaban_pemain is None:
        print("Waktu habis! Tidak dapat poin.")
    elif jawaban_pemain == jawaban_benar:
        print("Benar! 🎉")
        skor += 1
    else:
        print(f"Salah! Jawaban yang benar adalah: {jawaban_benar}")

# Hasil akhir
print("\n=== HASIL AKHIR ===")
print(f"Skor kamu: {skor}/{total}")

# Komentar berdasarkan skor
if skor == 0:
    print("Jangan menyerah, coba lagi ya!")
elif skor <= 5:
    print("Tingkatkan terus, kamu pasti bisa!")
elif skor <= 8:
    print("Bagus! Sedikit lagi jadi jago teka-teki!")
elif skor < total:
    print("Hebat! Hampir sempurna!")
else:
    print("Sempurna! Kamu master teka-teki sejati!")
