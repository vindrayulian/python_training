# Mengubah detik ke menit

import time

def pengingat(jeda_menit, pesan):
    print(f"Pengingat akan muncul dalam {jeda_menit} menit...")
    time.sleep(jeda_menit * 60)  # Ubah menit ke detik
    print(f"\nPengingat: {pesan}")

# Meminta input dari pengguna
jeda_menit = float(input("Masukkan waktu pengingat (dalam menit): "))
pesan = input("Masukkan pesan pengingat: ")

# Memanggil fungsi pengingat
pengingat(jeda_menit, pesan)
