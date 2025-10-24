# Game cerita interaktif dengan menambahkan banyak pilihan

print("🌲 Kamu sedang berjalan di hutan lebat dan menemukan dua jalan misterius.")
print("1. Jalan ke kiri (terdengar suara gemericik air)")
print("2. Jalan ke kanan (ada aroma bunga yang kuat)")

pilihan = input("Mau pilih yang mana? (1/2): ")

if pilihan == "1":
    print("\nKamu mengikuti suara air dan tiba di sungai yang jernih.")
    print("1. Menyeberangi sungai.")
    print("2. Mengikuti aliran sungai.")
    pilihan_sungai = input("Pilih (1/2): ")

    if pilihan_sungai == "1":
        print("\nKamu mencoba menyeberang... tapi tiba-tiba buaya muncul! 🐊")
        print("1. Melawan dengan tongkat.")
        print("2. Lari secepat mungkin!")
        pilihan_buaya = input("Pilih (1/2): ")
        if pilihan_buaya == "1":
            print("Tongkatmu patah... tapi buaya kabur! Kamu selamat! 😅")
        else:
            print("Kamu berhasil kabur, tapi kehilangan tas makananmu! 😭")
    else:
        print("\nKamu mengikuti aliran sungai dan menemukan perahu kecil.")
        print("1. Naiki perahunya.")
        print("2. Abaikan dan lanjut jalan kaki.")
        pilihan_perahu = input("Pilih (1/2): ")
        if pilihan_perahu == "1":
            print("Perahu itu membawamu ke desa tersembunyi yang damai. Kamu disambut dengan hangat. 🏡")
        else:
            print("Kamu tersesat di hutan tapi menemukan gua penuh kristal. 🌌")

elif pilihan == "2":
    print("\nKamu mengikuti aroma bunga dan menemukan taman indah.")
    print("1. Petik bunganya.")
    print("2. Cari siapa yang menanam taman ini.")
    pilihan_taman = input("Pilih (1/2): ")

    if pilihan_taman == "1":
        print("\nBegitu kamu memetik bunga, tanah bergetar dan roh penjaga taman muncul! 👻")
        print("1. Minta maaf.")
        print("2. Kabur!")
        pilihan_roh = input("Pilih (1/2): ")
        if pilihan_roh == "1":
            print("Rohnya tersenyum dan memberimu bunga ajaib. 🌸")
        else:
            print("Kamu kabur, tapi aroma bunga masih mengikutimu... 😨")
    else:
        print("\nKamu bertemu dengan peri taman. 🧚‍♀️")
        print("1. Berbicara dengan peri.")
        print("2. Minta panduan keluar dari hutan.")
        pilihan_peri = input("Pilih (1/2): ")
        if pilihan_peri == "1":
            print("Peri itu memberimu ramuan penyembuh dan menjadi temanmu. 💖")
        else:
            print("Peri menunjukkan jalan pulang. Kamu selamat dan belajar banyak tentang alam. 🌿")

else:
    print("\nKamu ragu dan tidak memilih apa pun... hutan menelammu perlahan... 🌫️ Game Over.")
