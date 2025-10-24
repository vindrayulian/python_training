# Program tebak nama rahasia teman dengan membuat permainan lebih interaktif

import random

# Daftar nama teman
daftar_nama = ["budi", "sinta", "andi", "rani", "dika", "lina", "agus"]

# Memilih satu nama secara acak
nama_rahasia = random.choice(daftar_nama)

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

# Jumlah kesempatan
kesempatan = 3

# Menyapa pemain
print("🎯 Selamat datang di permainan Tebak Nama Rahasia Teman!")
print("Saya sudah memikirkan salah satu nama teman saya dari daftar rahasia.")
print("Coba tebak siapa dia!\n")

# Perulangan untuk percobaan menebak
while kesempatan > 0:
    tebakan = input("Masukkan tebakan kamu: ").lower()
    
    if tebakan == nama_rahasia:
        print(random.choice(pesan_benar))
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(random.choice(pesan_salah))
            print(f"Kesempatan tersisa: {kesempatan}\n")
        else:
            print(f"😢 Yah, kesempatan habis! Nama rahasianya adalah {nama_rahasia.capitalize()}.")
            print("Coba lagi nanti ya, siapa tahu keberuntunganmu naik level! 😉")
