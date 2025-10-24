# Game cerita interaktif dengan cerita yang lebih panjang dan fitu waktu agar lebih smooth

import time

print("🌲 Selamat datang di Hutan Ajaib!")
print("Kamu adalah seorang petualang pemberani yang tersesat di hutan misterius.")
print("Di depanmu, dua jalan membentang...")

time.sleep(1)
print("\n1. Jalan ke kiri — terdengar suara air dan aroma lumut basah.")
print("2. Jalan ke kanan — terlihat sinar cahaya seperti dari obor.")

pilihan = input("Mau pilih jalan mana? (1/2): ")

if pilihan == "1":
    print("\nKamu berjalan ke kiri dan menemukan sungai besar.")
    print("Airnya jernih, tapi arusnya deras.")
    print("1. Menyeberang sungai dengan hati-hati.")
    print("2. Mengikuti sungai ke arah utara.")
    pilihan_sungai = input("Pilih (1/2): ")

    if pilihan_sungai == "1":
        print("\nKamu mulai menyeberang... tiba-tiba buaya muncul! 🐊")
        print("1. Melawan dengan tongkat.")
        print("2. Lompat ke batu besar di tengah sungai.")
        pilihan_buaya = input("Pilih (1/2): ")

        if pilihan_buaya == "1":
            print("\nKamu melawan buaya dengan tongkat dan berhasil membuatnya kabur! 😤")
            print("Setelah menyeberang, kamu menemukan pondok tua di tepi sungai.")
            print("1. Masuk ke pondok.")
            print("2. Lewati saja dan lanjut perjalanan.")
            pilihan_pondok = input("Pilih (1/2): ")

            if pilihan_pondok == "1":
                print("\nDi dalam pondok, kamu menemukan buku sihir kuno. 📖")
                print("Kamu belajar mantra penyembuh. Sekarang kamu bisa menyembuhkan luka!")
                print("✨ Kamu mendapat kemampuan baru!")
            else:
                print("\nKamu melanjutkan perjalanan dan menemukan patung naga emas.")
                print("Tiba-tiba patung itu hidup dan menatapmu... 🐉")
                print("Tapi karena kamu tidak memiliki buku sihir, naga itu mengusirmu. 😞")
        else:
            print("\nKamu lompat ke batu, tapi licin! Kamu hampir jatuh tapi berhasil naik ke tepi.")
            print("Kamu melihat sesuatu berkilau di air — sebuah permata biru! 💎")
            print("Kamu menyimpannya untuk nanti.")
    
    else:
        print("\nKamu mengikuti sungai dan menemukan desa tersembunyi.")
        print("Penduduk menyambutmu dengan hangat dan memberi makanan. 🍲")
        print("Tapi malam harinya, kamu mendengar suara langkah aneh di luar pondok...")
        print("1. Intip dari jendela.")
        print("2. Tetap pura-pura tidur.")
        pilihan_desa = input("Pilih (1/2): ")

        if pilihan_desa == "1":
            print("\nKamu melihat makhluk bayangan berwujud manusia serigala! 🐺")
            print("Untung kamu sempat menutup jendela, tapi desa jadi panik.")
            print("Keesokan paginya, kamu diangkat jadi penjaga desa. 🛡️")
        else:
            print("\nKamu pura-pura tidur, tapi makhluk itu masuk ke pondokmu!")
            print("Untung penduduk datang menolong. Kamu selamat, tapi kehilangan bekalmu. 😮‍💨")

elif pilihan == "2":
    print("\nKamu berjalan ke kanan dan menemukan kuil tua yang diterangi obor. 🕯️")
    print("Pintu kuil terbuka sedikit, kamu bisa mendengar bisikan halus dari dalam...")
    print("1. Masuk ke dalam kuil.")
    print("2. Keliling kuil dari luar.")
    pilihan_kuil = input("Pilih (1/2): ")

    if pilihan_kuil == "1":
        print("\nBegitu masuk, pintu menutup sendiri! 💨")
        print("Kamu melihat altar dan bola kristal yang berkilau.")
        print("1. Sentuh bola kristal.")
        print("2. Cari jalan keluar dulu.")
        pilihan_bola = input("Pilih (1/2): ")

        if pilihan_bola == "1":
            print("\nKamu tersedot ke dunia lain! 🌌")
            print("Di sana kamu bertemu roh penjaga waktu ⏳.")
            print("Roh itu menawarkan dua pilihan:")
            print("1. Kembali ke dunia nyata.")
            print("2. Menjadi penjaga waktu selamanya.")
            pilihan_roh = input("Pilih (1/2): ")

            if pilihan_roh == "1":
                print("\nKamu terbangun di hutan... semua terasa seperti mimpi. 😶")
            else:
                print("\nKamu menjadi legenda baru — sang penjaga waktu. ⏳✨")
        else:
            print("\nKamu menemukan jalan rahasia dan kabur ke luar kuil.")
            print("Di luar, kamu bertemu pedagang keliling yang menawarkan ramuan misterius. 🧪")
            print("1. Minum ramuannya.")
            print("2. Tolak dengan sopan.")
            pilihan_ramuan = input("Pilih (1/2): ")

            if pilihan_ramuan == "1":
                print("\nKamu langsung merasa kuat dan cepat! 💪")
                print("Sekarang kamu bisa berlari secepat angin!")
            else:
                print("\nPedagang itu tersenyum, 'Bijak sekali, anak muda.' katanya.")
                print("Ternyata ramuan itu racun, dan kamu baru saja menyelamatkan dirimu sendiri. 😮‍💨")
    else:
        print("\nSaat kamu berkeliling, kamu menemukan tulisan kuno di dinding kuil.")
        print("Ternyata itu peta menuju harta karun naga! 🗺️")
        print("1. Ikuti petanya.")
        print("2. Abaikan dan kembali ke jalan semula.")
        pilihan_peta = input("Pilih (1/2): ")

        if pilihan_peta == "1":
            print("\nSetelah perjalanan panjang, kamu menemukan gua naga.")
            print("Tapi naga itu sedang tidur nyenyak... 😴")
            print("1. Ambil hartanya diam-diam.")
            print("2. Bangunkan naga dan ajak bicara.")
            pilihan_naga = input("Pilih (1/2): ")

            if pilihan_naga == "1":
                print("\nKamu berhasil mengambil sebagian emas, tapi langkahmu membangunkan naga! 🐉")
                print("Kamu lari secepat mungkin! Selamat tapi jantung hampir copot! 💨😂")
            else:
                print("\nNaga itu ternyata bijak dan memberimu setengah hartanya karena kejujuranmu. 💰✨")
        else:
            print("\nKamu kembali ke jalan awal dan menyadari... kamu sudah berjalan berjam-jam.")
            print("Tapi anehnya, hutan kini terlihat lebih terang — mungkin kamu sudah hampir keluar. 🌅")

else:
    print("\nKamu tidak memilih apa pun. Hutan perlahan menelammu... 🌫️ Game Over.")
