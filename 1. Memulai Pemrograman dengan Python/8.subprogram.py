import subprogram_modul # Menggunakan fungsi dari modul subprogram_modul.py

# Definisi Subprogram
# Sejauh ini, Anda telah membuat program yang beragam. Setiap program yang Anda bangun, pada akhirnya akan semakin besar seiring dengan kompleksitas masalah yang perlu diselesaikan. Semakin besar sebuah program, bagian kode yang berulang akan bertambah sehingga tidak efisien jika Anda perlu mengetik ulang atau bahkan melakukan copy-paste.

# ini contoh kode yang tidak efisien
# Menghitung Luas Persegi Panjang
panjang = 5
lebar = 10

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

# Luas kedua
panjang = 4
lebar = 15

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

print("   ")

# Lalu, apakah ada cara untuk menghindari kode yang perlu diketik berulang, dan sebaliknya, dapat digunakan berkali-kali? Jawabannya adalah ada, inilah yang disebut sebagai subprogram dan salah satu jenisnya adalah fungsi.

# Definisi Fungsi
# Fungsi adalah sekumpulan instruksi yang dapat digunakan berkali-kali. Fungsi dapat menerima input, melakukan pemrosesan, dan mengembalikan hasil. Fungsi juga dapat memiliki parameter yang memungkinkan Anda untuk memberikan nilai saat memanggil fungsi tersebut.
# Fungsi dapat didefinisikan dengan menggunakan kata kunci def diikuti dengan nama fungsi, tanda kurung, dan titik dua. Di dalam
def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4, 15)
print(persegi_panjang_kedua)

def perkalian(a, b):
    return a * b

angka_pertama = int(input("Masukkan angka pertama: "))
angka_kedua = int(input("Masukkan angka kedua: "))

print("Hasil dari", angka_pertama, "*", angka_kedua, "adalah", perkalian(angka_pertama, angka_kedua))

print("   ")

# Fungsi Anonim (Lambda Expression)
# Terakhir, mari kita pelajari cara membuat fungsi tanpa mendeklarasikan def. Cara ini dikenal dengan ekspresi lambda yang digunakan untuk membuat fungsi tanpa perlu menyebutkan def ketika membuatnya. Anda bisa mengasumsikan fungsi anonim ini sebagai fungsi one-liner. Secara umum, struktur fungsi anonim sebagai berikut.

mencari_luas = lambda panjang, lebar: panjang * lebar
print(mencari_luas(5, 10))


# Argumen dan Parameter
# Definisi fungsi: x dan y adalah parameter

angka1 = 80
angka2 = 15

def bandingkan(x, y):
    if x < y:
        return x
    else:
        return y

# Pemanggilan fungsi: 10 dan 20 adalah argumen
hasil1 = bandingkan(10, 20)     # argumen = 10, 20
hasil2 = bandingkan(angka1, angka2)  # argumen = nilai variabel angka1 dan angka2



# Menulis Modul pada Python
# Pembahasan terakhir terkait fungsi adalah kita akan mempelajari cara memanggil sebuah fungsi dari berkas lain. Masih ingat dengan modul? Ia adalah sebuah file berisi kode Python dan di dalamnya terdapat fungsi, kelas, dan sebagainya.

# Sebab setiap file berekstensi .py dapat direferensikan sebagai modul, Anda bisa melakukan impor file dari satu file ke yang lainnya. Layaknya ketika Anda menggunakan library, modul, dan sebagainya.
# contoh penerapan fungsi dari modul lain diatas 

persegi_panjang = subprogram_modul.mencari_luas(5, 10)
print(persegi_panjang)

# contoh lain
print(subprogram_modul.nama) # memanggil variabel dari modul lain

# Prosedur 
# Dalam KBBI, kata prosedur memiliki makna sebagai tahap kegiatan untuk menyelesaikan suatu aktivitas. Hal ini sama seperti prosedur sebagai subprogram yang merupakan pengelompokan instruksi-instruksi yang sering dipakai dalam program. 

def greeting(name):
    print("Halo " + name + ", Selamat Datang!")

greeting("Dicoding Indonesia") # memanggil prosedur greeting dengan parameter Dicoding Indonesia
