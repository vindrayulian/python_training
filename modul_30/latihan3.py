# Menambahkan suara saat pengingat muncul

import time
import os
import platform

def bunyi():
    sistem = platform.system()
    if sistem == "Windows":
        import winsound
        winsound.Beep(1000, 700) 
    else:
        os.system('echo -e "\a"')

def pengingat(jeda_menit, pesan):
    print(f"Pengingat akan muncul dalam {jeda_menit} menit...")
    time.sleep(jeda_menit * 60)
    bunyi()
    print(f"\nPengingat: {pesan}")

# Input pengguna
jeda_menit = float(input("Masukkan waktu pengingat (dalam menit): "))
pesan = input("Masukkan pesan pengingat: ")

pengingat(jeda_menit, pesan)
