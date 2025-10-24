import time

def pengingat(jeda, pesan):
    print(f"Pengingat akan muncul dalam {jeda} detik...")
    time.sleep(jeda) # Menunggu sesuai waktu yang di atur
    print(f"\n**Pengingat: {pesan}**")
    

# Meminta input dari pengguna
jeda = int(input("Masukkan waktu pengingat (dalam detik): "))
pesan = input("Masukan pesan pengingat: ")

# Memanggil fungsi pengingat
pengingat(jeda, pesan)