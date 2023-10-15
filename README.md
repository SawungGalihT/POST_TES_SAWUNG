# POST_TES_PRAKTIKUM_KELAS_B
# NAMA : SAWUNG GALIH TRIATMOJO
# NIM : 2309116058
# SOURCECODE PYTHON : 
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
   print("Password and tidak sesuai, silahkan coba lagi")

   ![WhatsApp Image 2023-09-26 at 01 05 55](https://github.com/SawungGalihT/POST_TES_SAWUNG/assets/144757389/5279d75c-93ad-4c26-bcd8-4d4550e9c0a1)
![flowchart konversi drawio (4)](https://github.com/SawungGalihT/POST_TES_SAWUNG/assets/144757389/ace6bcf9-df2c-4c90-aa22-a628174fb6c3)
![Screenshot 2023-09-26 012048](https://github.com/SawungGalihT/POST_TES_SAWUNG/assets/144757389/3545985e-962a-4a87-890f-bf947d4dcf5f)
![Screenshot 2023-09-26 012415](https://github.com/SawungGalihT/POST_TES_SAWUNG/assets/144757389/a6960c21-91cc-406f-b539-d1138916242a)
![Screenshot 2023-09-26 012247](https://github.com/SawungGalihT/POST_TES_SAWUNG/assets/144757389/fac7dd0f-705d-4882-82d7-fcea421aa6b1)


