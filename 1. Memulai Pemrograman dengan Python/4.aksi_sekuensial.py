# aksi sekuensial dengan kata lain, program yang Anda bangun haruslah memiliki awal dan akhir. Jadi, ketika program tersebut dijalankan, bisa diketahui waktu berakhirnya. Simak kode di bawah ini untuk melihat implementasinya.

print("Selamat datang dalam program python\n")
print("silahkan masukan data diri anda\n")

nama = input("Nama :")
tahun_lahir = input("Tahun lahir :")
umur = 2025 - int(tahun_lahir)

print("Nama anda adalah", nama, "dan umur anda adalah", umur, "tahun")
print("Terima kasih telah menggunakan program ini")

a = 6
b = 9 

print(a**2)
print(b//3)

# Kode di atas merupakan program yang sama dengan kode sebelumnya. Namun, hasil yang didapat berbeda karena Anda mengubah urutan sintaks "print()". 


# block code
# Kode ini merupakan penerapan materi perulangan.
for i in range(10):
    print(i)

# Case-sensitive
text = "Indonesia"
Text = "dikoding"

print(text)
print(Text)

# Pada program di atas, Anda membuat dua variabel dengan nama "teks" dan "Teks". Python akan menganggap bahwa variabel tersebut berbeda, walaupun bagi kita sebagai manusia, mereka memiliki arti yang sama.

# One-Liner 
# Tujuan dari one-liner ini adalah membuat satu baris kode yang singkat dan jelas. Perlu diingat bahwa tidak semua kode blok dapat dijadikan one-liner, seperti deklarasi fungsi, modul, dan kelas

x = 1
y = 2

temp = x
x = y
y = temp 

print("Setelah Penukaran")
print("x =", x)
print("y =", y)
