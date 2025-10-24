from colorama import Fore, Style, init
from playsound import playsound
from PIL import Image
import time
import os

# Inisialisasi Colorama
init(autoreset=True)

# (Opsional) Folder tempat suara & gambar disimpan
SOUND_PATH = "./sounds/"
IMAGE_PATH = "./images/"

def play_sound(filename, block=False):
    """Putar suara jika file ada"""
    path = os.path.join(SOUND_PATH, filename)
    if os.path.exists(path):
        playsound(path, block=block)

def show_image(filename):
    """Tampilkan gambar jika file ada"""
    path = os.path.join(IMAGE_PATH, filename)
    if os.path.exists(path):
        Image.open(path).show()

def narasi(teks, warna=Fore.WHITE, jeda=0.03):
    """Cetak teks seperti mesin ketik"""
    for huruf in teks:
        print(warna + huruf, end="", flush=True)
        time.sleep(jeda)
    print(Style.RESET_ALL)

# Intro
# forest
play_sound("awholenewworld.mp3", block=False)
show_image("download.jpeg")

narasi("🌲 Selamat datang di Hutan Ajaib...", Fore.GREEN)
time.sleep(1)
narasi("Kamu adalah petualang pemberani yang mencari rahasia Sang Penjaga Waktu.", Fore.YELLOW)
time.sleep(1)
narasi("Kabarnya, di hutan ini tersembunyi kekuatan kuno yang bisa mengubah masa depan... ⏳", Fore.CYAN)
time.sleep(1)

narasi("\nDi depanmu ada dua jalan:", Fore.WHITE)
print(Fore.MAGENTA + "1. Jalan ke kiri — terdengar suara air dan burung bernyanyi.")
print(Fore.MAGENTA + "2. Jalan ke kanan — ada cahaya misterius di balik pepohonan.")
pilihan = input(Fore.CYAN + "Pilih jalanmu (1/2): ")

if pilihan == "1":
    # river
    play_sound("awholenewworld.mp3", block=False)
    show_image("download.jpeg")
    narasi("\nKamu berjalan ke arah sungai. Airnya jernih, tapi arusnya deras.", Fore.GREEN)
    time.sleep(1)
    narasi("Kamu melihat batu besar di tengah sungai dan seekor buaya bersembunyi di bawahnya... 🐊", Fore.YELLOW)
    print(Fore.MAGENTA + "\n1. Melawan buaya dengan tongkat.")
    print(Fore.MAGENTA + "2. Menyelinap melewati batu.")
    aksi = input(Fore.CYAN + "Pilih tindakanmu (1/2): ")

    if aksi == "1":
        # fight
        play_sound("awholenewworld.mp3")
        narasi("\nKamu melawan buaya dengan berani!", Fore.RED)
        narasi("Tongkatmu patah, tapi buaya kabur. Kamu selamat! 😤", Fore.GREEN)
        narasi("Kamu menemukan pondok tua di tepi sungai...", Fore.YELLOW)
        show_image("download.jpeg")
        print(Fore.MAGENTA + "\n1. Masuk ke pondok.")
        print(Fore.MAGENTA + "2. Lewati saja dan lanjutkan perjalanan.")
        aksi2 = input(Fore.CYAN + "Pilih (1/2): ")

        if aksi2 == "1":
            # magic
            play_sound("awholenewworld.mp3")
            narasi("\nDi dalam pondok, kamu menemukan buku sihir kuno! 📖", Fore.YELLOW)
            narasi("Kamu belajar mantra penyembuh dan merasa kekuatan baru mengalir di tubuhmu.", Fore.CYAN)
            narasi("✨ Kamu mendapatkan kemampuan penyembuhan!", Fore.GREEN)
        else:
            narasi("\nKamu memilih lanjut berjalan. Setelah beberapa jam, kamu melihat patung naga emas. 🐉", Fore.YELLOW)
            play_sound("awholenewworld.mp3")
            narasi("Patung itu hidup! Tapi karena kamu tak punya buku sihir, naga itu hanya menatapmu... lalu menghilang. 😮", Fore.WHITE)

    else:
        narasi("\nKamu berhasil menyelinap melewati batu dan menemukan sesuatu yang berkilau.", Fore.CYAN)
        play_sound("awholenewworld.mp3")
        narasi("Sebuah permata biru tergeletak di air... kamu mengambilnya. 💎", Fore.BLUE)
        narasi("Kamu merasa energi misterius dari dalamnya...")

        print(Fore.MAGENTA + "\n1. Simpan permata.")
        print(Fore.MAGENTA + "2. Buang karena merasa takut.")
        aksi3 = input(Fore.CYAN + "Pilih (1/2): ")

        if aksi3 == "1":
            narasi("\nPermata itu bersinar terang! Kamu dipindahkan ke dunia lain! 🌌", Fore.CYAN)
            play_sound("awholenewworld.mp3")
            narasi("Kamu melihat istana kristal terapung di langit...", Fore.BLUE)
            narasi("Sebuah suara berkata: 'Kau telah dipilih menjadi penjaga waktu.' ⏳", Fore.YELLOW)
            narasi(Fore.GREEN + "\n✨ AKHIR BAIK: Kamu menjadi legenda yang menjaga keseimbangan masa depan. ✨")
        else:
            narasi("\nKamu membuang permata itu. Cahaya padam, dan hutan menjadi gelap.", Fore.RED)
            narasi("Kamu mendengar langkah berat mendekat... dan semuanya menghilang. 🌫️", Fore.RED)
            narasi(Fore.RED + "\n💀 AKHIR BURUK: Hutan menelammu selamanya.")

else:
    play_sound("awholenewworld.mp3", block=False)
    show_image("download.jpeg")
    narasi("\nKamu mengikuti cahaya dan menemukan kuil tua yang diterangi obor. 🕯️", Fore.YELLOW)
    narasi("Di dalamnya, kamu melihat altar dan bola kristal berputar perlahan.", Fore.CYAN)
    print(Fore.MAGENTA + "\n1. Sentuh bola kristal.")
    print(Fore.MAGENTA + "2. Cari jalan keluar terlebih dahulu.")
    aksi = input(Fore.CYAN + "Pilih (1/2): ")

    if aksi == "1":
        play_sound("awholenewworld.mp3")
        narasi("\nKamu menyentuh bola kristal... dan tersedot ke ruang waktu! ⏳", Fore.BLUE)
        narasi("Roh penjaga waktu muncul dan menatapmu dengan tatapan dalam.", Fore.YELLOW)
        print(Fore.MAGENTA + "\n1. Minta dikembalikan ke dunia nyata.")
        print(Fore.MAGENTA + "2. Terima takdirmu menjadi penjaga waktu.")
        aksi2 = input(Fore.CYAN + "Pilih (1/2): ")

        if aksi2 == "1":
            narasi("\nRoh itu tersenyum. 'Baiklah, waktu akan berputar untukmu sekali lagi.'", Fore.WHITE)
            play_sound("awholenewworld.mp3")
            narasi("Kamu terbangun di hutan... semua terasa seperti mimpi. 😶", Fore.GREEN)
            narasi(Fore.YELLOW + "\nAKHIR NETRAL: Kau kembali, tapi membawa kenangan yang takkan hilang.")
        else:
            narasi("\nKau menerima takdirmu.", Fore.BLUE)
            narasi("Cahaya memenuhi tubuhmu... dan kau menghilang dari dunia manusia.", Fore.CYAN)
            narasi(Fore.GREEN + "\nAKHIR LEGENDA: Kau menjadi penjaga waktu, pengawas masa depan dan masa lalu. ⏳✨")

    else:
        narasi("\nKamu menemukan jalan rahasia di dinding kuil!", Fore.CYAN)
        play_sound("awholenewworld.mp3")
        narasi("Kau keluar dari kuil dan menemukan peta kuno di tanah... 🗺️", Fore.YELLOW)
        print(Fore.MAGENTA + "\n1. Ikuti peta itu.")
        print(Fore.MAGENTA + "2. Abaikan dan kembali ke jalan awal.")
        aksi3 = input(Fore.CYAN + "Pilih (1/2): ")

        if aksi3 == "1":
            narasi("\nKau berjalan jauh hingga menemukan gua naga.", Fore.GREEN)
            play_sound("awholenewworld.mp3")
            narasi("Naga itu tidur di atas tumpukan emas. 🐉", Fore.YELLOW)
            print(Fore.MAGENTA + "\n1. Ambil harta diam-diam.")
            print(Fore.MAGENTA + "2. Bangunkan naga dan bicara.")
            aksi4 = input(Fore.CYAN + "Pilih (1/2): ")

            if aksi4 == "1":
                narasi("\nKau mengambil sebagian emas, tapi langkahmu membangunkan naga! 😱", Fore.RED)
                play_sound("awholenewworld.mp3")
                narasi("Kau kabur secepat mungkin dan berhasil keluar dari hutan.", Fore.GREEN)
                narasi(Fore.YELLOW + "\nAKHIR PETUALANG: Kau hidup bahagia dengan emas curianmu. 💰😂")
            else:
                narasi("\nNaga itu membuka matanya perlahan...", Fore.CYAN)
                narasi("'Manusia jujur sepertimu jarang ada,' katanya.", Fore.YELLOW)
                narasi("Ia memberimu setengah hartanya dan menganggapmu sahabat. 🐉❤️", Fore.GREEN)
                narasi(Fore.GREEN + "\nAKHIR HARMONI: Kau hidup damai berdampingan dengan naga penjaga harta.")

        else:
            narasi("\nKau kembali ke jalan awal dan melihat fajar mulai menyingsing. 🌅", Fore.YELLOW)
            narasi("Petualanganmu berakhir... tapi misteri hutan masih tersisa.", Fore.CYAN)
            narasi(Fore.WHITE + "\nAKHIR TENANG: Kau keluar dari hutan dengan hati penuh rasa syukur.")

narasi("\nTerima kasih sudah bermain! 🌿", Fore.WHITE)
