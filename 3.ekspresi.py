# Dibawah ini, penerapn ekspresi pada Python
x = 10
y = 5
result = x + y
print("Hasil dari x + y adalah:", result) 

# dengan list
angka = [1, 2, 3, 4, 5]
huruf = ['a', 'b', 'c', 'd', 'e']
gabung = angka + huruf
print("Hasil dari angka + huruf adalah:", gabung)

learn = ["P", "Y", "T", "H", "O", "N"]
replikasi = learn * 3
print("Hasil dari learn * 3 adalah:", replikasi)

# jenis-jenis ekspresi dalam python
# 1. Ekspresi menurut arity dari operator
a = True
a = not a # unary operator
print(a) # False

b = 10
b -= 2 # binary operator
print(b) # 8

d = 10
print(-d) # unary operator -10

# 2. Ekspresi menurut tipe data yang dihasilkan
print(10 + 5) # integer
print(10>2) # boolean True
print(True or False) # True

# Jenis Jenis Operator dalam Python
# 1. Operator Aritmatika
x = 11
y = 5

print(x + y) # Penjumlahan
print(x - y) # Pengurangan
print(x * y) # Perkalian
print(x / y) # Pembagian
print(x // y) # Pembagian bulat
print(x % y) # Sisa bagi
print(x ** y) # Pangkat

# 3. Operator relasional
x = 5
y = 10

print(x == y) # Sama dengan
print(x != y) # Tidak sama dengan
print(x > y) # Lebih besar dari
print(x < y) # Lebih kecil dari
print(x >= y) # Lebih besar sama dengan
print(x <= y) # Lebih kecil sama dengan

# 4. Operator Logika
x = True
y = False

print(x and y) # AND
print(x or y) # OR
print(not x) # NOT

# 5. Operator Assigment
# +=
x = 11
x += 5
print(x)

# -=
x = 11
x -= 5
print(x)

# *=
x = 11
x *= 5
print(x)

# /=
x = 11
x /= 5
print(x)

#%=
x = 11
x%= 5
print(x)

# Kuis Coding: Ekspresi
"""
TODO:
Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".

Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""
# Jangan ubah kode ini
dico = 750000

# TODO: Silakan buat kode Anda di bawah ini.
if dico > 500000:
    total_harga = dico - (dico * 0.1)
else:
    total_harga = dico

print("Total harga belanja Dico setelah diskon adalah:", total_harga)

