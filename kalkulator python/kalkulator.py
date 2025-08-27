print("=" * 20)
print("Operasi Matematika")
print("1. Penjumlahan \t [+]")
print("2. Pengurangan \t [-]")
print("3. Perkalian \t [*]")
print("4. Pembagian \t [/]")
print("=" * 20)

operasi = input("Pilih operasi (1/2/3/4):  ")
angka1 = eval(input("Masukkan angka pertama: "))
angka2 = eval(input("Masukkan angka kedua: "))

print("=" * 20)
if operasi == "1":
    hasil = angka1 + angka2
    print(f"Hasil Penjumlahan: {hasil}")
elif operasi == "2":
    hasil = angka1 - angka2
    print(f"Hasil Pengurangan: {hasil}")
elif operasi == "3":
    hasil = angka1 * angka2
    print(f"Hasil Perkalian: {hasil}")
elif operasi == "4":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil Pembagian: {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
else:
    print("Operasi tidak valid. Silakan pilih 1, 2, 3, atau 4.")
    
