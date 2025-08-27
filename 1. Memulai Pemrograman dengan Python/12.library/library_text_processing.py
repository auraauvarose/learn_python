# Library Text Processing
# Pertama adalah sekumpulan library yang bertujuan untuk melakukan pemrosesan teks dan menyederhanakan serta mempercepat tugas-tugas pemrosesan teks.

import re # import modul regex

"""

1. String
String adalah salah satu modul bawaan Python yang tidak perlu dideklarasikan. Pada modul string ada fungsi-fungsi yang dapat dioperasikan pada variabel bertipe string seperti di bawah.
    1. upper(): Ubah setiap huruf dalam string menjadi huruf kapital. 
    2. lower(): Ubah setiap huruf dalam string menjadi huruf kecil.
    3. split(): Pisahkan teks berdasarkan delimiter (karakter pemisah).
    4. title(): Jadikan setiap awal kata kapital.
    5. zfill(): Tambahkan nol di awal string sebanyak nilai yang ada pada parameter.

"""

testing = "Pelajar"
print(testing.upper())
print(testing.lower())
print(testing.split())
print(testing.title())
print(testing.zfill(20))


"""

2. Regex
Regex atau regular expression adalah sebuah cara untuk mencari teks berdasarkan pola tertentu. Umpamanya, ketika ingin mencari sebuah kata dalam kamus, misalnya arti dari kata parsing, kita akan mencari kata tersebut di halaman yang memiliki kata dengan awalan p, lalu pa. Regex bekerja dengan konsep yang sama.

Pada regex, kita mencari sebuah kata atau kumpulan kata dengan memberikan pola yang diinginkan. Contoh umum regex adalah pada email. Kita dapat menggunakan regex untuk mengecek bahwa karakter @ ada pada email atau tidak.

Contoh di bawah menunjukkan penggunaan regex. Pada variabel pattern di bawah, ^a berarti kita ingin mencari teks dengan awalan 'a', dan s$ berarti kita ingin mencari string berakhiran 's'.

"""

pola = '^a....s$' 
string_test = 'acycss'
hasil = re.match(pola, string_test)

if hasil:
    print('Berhasil')
else:
    print('Pencarian Gagal')