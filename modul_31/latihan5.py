# Program tebak nama rahasia teman dengan membuat pemain mendapatkan skor setiap kali menebak dengan benar

import random

# Daftar nama teman
daftar_nama = ["budi", "sinta", "andi", "rani", "dika", "lina", "agus"]

# Daftar pesan jika tebakan benar
pesan_benar = [
    "🎉 Wah, kamu kayak cenayang! Tepat banget!",
    "🔥 Gokil! Insting kamu tajam juga!",
    "😎 Betul sekali! Kamu pasti sering baca pikiran orang ya?",
    "👏 Hebat! Kamu berhasil menebak nama rahasia!"
]

# Daftar pesan jika tebakan salah
pesan_salah = [
    "😅 Salah, tapi jangan sedih... mungkin kamu butuh kopi dulu ☕",
    "🙈 Waduh, belum tepat. Coba pakai jurus 'feeling kuat' deh!",
    "😂 Hahaha... hampir, tapi belum kena!",
    "😬 Salah lagi... tenang, masih ada kesempatan kok!"
]

# Inisialisasi skor pemain
skor = 0

print("🎯 Selamat datang di permainan Tebak Nama Rahasia Teman!")
print("Saya sudah memikirkan nama teman-teman saya secara acak.")
print("Coba tebak siapa dia! Kamu punya 3 kesempatan setiap ronde.\n")

while True:
    # Memilih nama rahasia acak setiap ronde
    nama_rahasia = random.choice(daftar_nama)
    kesempatan = 3

    # Loop untuk tiap ronde
    while kesempatan > 0:
        tebakan = input("Masukkan tebakan kamu: ").lower()

        if tebakan == nama_rahasia:
            print(random.choice(pesan_benar))
            skor += 1  # Tambah skor jika benar
            print(f"🏆 Skor kamu sekarang: {skor}\n")
            break
        else:
            kesempatan -= 1
            if kesempatan > 0:
                print(random.choice(pesan_salah))
                print(f"Kesempatan tersisa: {kesempatan}\n")
            else:
                print(f"😢 Yah, kesempatan habis! Nama rahasianya adalah {nama_rahasia.capitalize()}.\n")

    # Tanya apakah mau lanjut ronde berikutnya
    lanjut = input("Mau main lagi? (lanjut/udahan): ").lower()
    if lanjut != "y":
        print(f"\n✨ Permainan selesai! Skor akhir kamu: {skor}")
        if skor == 0:
            print("😜 Wah, belum hoki nih. Coba lagi nanti!")
        elif skor < 3:
            print("👍 Lumayan! Feeling kamu udah mulai tajam.")
        else:
            print("🔥 Keren banget! Kamu benar-benar master tebak nama!")
        break
    print("\n=== Ronde berikutnya! ===\n")
