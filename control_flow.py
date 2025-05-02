# Prcabangan dan Ternary Operators
# Percabangan : Dalam pemrograman, sebuah kode program dapat berjalan berdasarkan kondisi tertentu. Maknanya, Anda dapat memberikan instruksi berdasarkan "Jika-maka" (if-else). 

ketersediaan = "Daging Ayam"
score = 100
tinggi_badan = 140

if ketersediaan == "Daging Ayam": # Nilai True  
    print("Daging Ayam Tersedia")
else:
    print("Daging Ayam Tidak Tersedia")

if score >= 100: print("Score Anda Memuaskan") # if statement memiliki versi one-liner-nya

if tinggi_badan >= 160: # Nilai False
    print("kamu bisa memakai wahana ini")
else:
    print("kamu tidak bisa memakai wahana ini")

# elif : Jika Anda memiliki lebih dari dua kondisi, Anda dapat menggunakan elif untuk menambahkan lebih banyak kondisi.

nilai = 77
if nilai >= 90:
    print("Selamat Anda Lulus")
    print("Dengan Sangat Memuaskan (Grade A)")
elif nilai >= 80:
    print("Selamat Anda Lul us")
    print("Dengan Memuaskan (Grade B)")
elif nilai >= 70:
    print("Selamat Anda Lulus") 
    print("Dengan Cukup Memuaskan (Grade C)")
else:
    print("Maaf Anda Tidak Lulus")
    print("Silakan coba lagi tahun depan")


# untuk informasi tambahan dapat menanmbahkan and dan or 
nilai = 81
perilaku = "tidak baik"

if nilai >= 80 and perilaku == "baik":
    print("Selamat Anda Lulus")
    print("Dengan Sangat Memuaskan (Grade A)")
elif nilai >= 80 and perilaku != "baik":
    print("Selamat Anda Lulus")
    print("Dengan Memuaskan (Grade B)")
else:
    print("Maaf Anda Tidak Lulus")
    print("Silakan coba lagi tahun depan")


# ternary operator
# Ternary operator adalah cara singkat untuk menulis if-else dalam satu baris.
lulus = True 
print("selamat") if lulus else print("maaf") # sama dengan

if lulus:
    print("selamat")
else:
    print("maaf")


# Perulangan dan Looping
# Perulangan adalah cara untuk mengeksekusi blok kode yang sama berulang kali. Anda dapat menggunakan perulangan untuk mengulangi blok kode dengan jumlah yang ditentukan atau sampai kondisi tertentu terpenuhi. 

# For 
# Perulangan for digunakan untuk mengulangi blok kode dengan jumlah yang ditentukan. Anda dapat menggunakan perulangan for untuk mengulangi elemen dalam list, tuple, string, atau range.

var_list = [1, 2, 3, 4, 5] # list
for i in var_list:
    print(i)

print("   ")

for i in range(5): # range
    print(i)

print("   ")

for i in range(1, 6): # range dengan batasan
    print(i)

print("   ")

# While
# While termasuk sintaks dalam Python yang bersifat indefinite iteration. Indefinite iteration adalah sebuah proses iterasi yang akan berhenti ketika memenuhi kondisi tertentu.

counter = 1
while counter <= 5:
    print(counter)
    counter += 1 # increment counter = counter + 1, jika tidak ditambahkan maka akan menjadi infinite loop

print("  ")

# For Bersarang 
for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)

print("  ")

# Kontrol Perulangan
# break, break digunakan untuk menghentikan perulangan saat kondisi tertentu terpenuhi.

for i in range(2):
    print("Perulangan", i)
    for j in range(10):
        print("Perulangan", j)
        if j == 2:
            break # untuk menghentikan perulangan kedua
print("  ")
# ini contoh kedua 
for name in 'Diko ding':
    if name == ' ':  
        break # untuk menghentikan perulangan kedua
    print('huruf saat ini adalah: {}'.format(name))

print("  ")

# Else setelah for 
# pada python juga dikenal else setelah for yang berfungsi untuk perulangan bersifat pencarian.

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 5:
        print("Angka ditemukan")
        break
else:
    print("angka tidak ditemukan")

print("  ")
