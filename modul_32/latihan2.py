# Membuat game carita interaktif

print("Kamu sedang berjalan di hutan dan menemukan dua jalan.")
print("1. Jalan ke kiri")
print("2. Jalan ke kanan")

pilihan = input("Mau pilih yang mana? (1/2): ")

if pilihan == "1":
    print("Kamu bertemu dengan seekor naga! 🐉")
    print("Apa yang akan kamu lakukan?")
    print("1. Lari!")
    print("2. Bicara dengan naga.")
    pilihan_naga = input("Pilih (1/2): ")
    if pilihan_naga == "1":
        print("Kamu selamat! Tapi... kamu terjebak di gua! 😱")
    else:
        print("Naga itu ternyata ramah dan memberimu emas! 💰")
        
else:
    print("Kamu menemukan harta karun! 🎁 selamat!")