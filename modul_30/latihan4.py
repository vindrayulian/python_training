# Menambahkan suara dari audio sendiri saat pengingat muncul

import time
from playsound import playsound

def pengingat(jeda_menit, pesan):
    print(f"Pengingat akan muncul dalam {jeda_menit} menit...")
    time.sleep(jeda_menit * 60)
    playsound(r"D:\Vindra\Robotic\Training\modul_30\awholenewworld.mp3")
    print(f"\n🎵 Pengingat: {pesan}")

jeda_menit = float(input("Masukkan waktu pengingat (dalam menit): "))
pesan = input("Masukkan pesan pengingat: ")

pengingat(jeda_menit, pesan)
