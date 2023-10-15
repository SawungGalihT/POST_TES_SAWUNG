# Membuat percabangan untuk memilih satuan massa yang ingin dikonversikan (pounds (lb), ounce (ons), gram (g) )

nama = str(input("NAMA : "))
nim = int(input("NIM : "))
prodi = str(input("PRODI : "))
password = int(input("PASWORD : "))

if password == 2222:
    print("\nKonversi massa (kg), ke (lb), (ons), (gram)")

    massa = float(input("\nmasukan massa (kg) : "))
    massa_apa = massa
    print("\nsilahkan pilih satuan")
    print("1. lb")
    print("2. ons")
    print("3. gram")

    satuan = int(input("yang akan dikonversikan dari kg ke : "))

    if satuan == 1:
        satuan_apa = " lb "
        massa *= 2.205
    elif satuan == 2:
        satuan_apa = " ons "
        massa *= 35.274
    elif satuan == 3:
        satuan_apa = " gram "
        massa *= 1000

    print("\n", massa_apa, "kg =", massa, satuan_apa)
    print("\nNAMA", nama,"\nNIM",nim, "\nPRODI", prodi,)
    print("\nTERIMA KASIH TELAH MENGGUNAKAN")
    print("="*10, "PROGRAM SELESAI", "="*10)
else:
   print("Password anda tidak sesuai, silahkan coba lagi")
