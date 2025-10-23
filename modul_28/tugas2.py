print("=== Program Pembagian Ceria ===")

try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    hasil = angka1 / angka2
    print(f"Hasilnya adalah: {hasil}")

except ZeroDivisionError:
    print("Ups! 😅 Kamu mencoba membagi dengan nol. Coba lagi ya, nggak bisa bagi dengan nol soalnya!")

except ValueError:
    print("Hehe... 🤭 Sepertinya yang kamu ketik bukan angka. Yuk, masukkan angka yang benar!")

except Exception as e:
    print(f"Waduh 😮 Ada kesalahan tak terduga: {e}. Tapi nggak apa-apa, kita coba lagi ya!")

print("Terima kasih sudah mencoba program ini! 🎉")
