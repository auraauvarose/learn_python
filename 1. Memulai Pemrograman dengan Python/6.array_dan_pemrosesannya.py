# Fundamental Array 
# Python tidak memiliki tipe data array yang sering digunakan dalam bahasa pemrograman lain. Sebaliknya, Python memiliki tipe data list yang dapat dikatakan mirip, tetapi tak sama dengan array. 

x = [1, 2, 3, 4, 5] # list ini bisa sama tapi tidak sama dengAN tipe data array
print(x)

# Library merupakan sekumpulan kode yang telah dibuat oleh developer atau programmer dan disediakan kepada pengguna lain agar dapat digunakan ulang dalam pengembangan program atau perangkat lunak. Adapun modul merupakan file yang berisikan kode Python dan dapat digunakan kembali oleh programmer lainnya.

import array # Mengakses liberary array
x = array.array('i', [1, 2, 3, 4, 5]) # array ini sama dengan tipe data array
print(x)
print(type(x)) # tipe data array

print("   ")

# Implementasi Array dengan Python
# Dalam materi ini, Anda akan mempelajari bentuk-bentuk penerapan Array dengan Python. Pertama, kita akan membahas deklarasi array. Kedua, kita akan membahas cara mengakses elemen array.

# Mendeklarasikan Array
var_list = [1,2,3]
for elemen in var_list:
    print(id(elemen))

# mndefinisikan nilai default
var_arr = [0 for i in range(10)]
print(var_arr) # Jika Anda merasa familier dengan struktur tersebut, Anda benar. Struktur tersebut merupakan struktur yang sama dengan list comprehension. Anda dapat menginisialisasi variabel array dengan menggunakan list comprehension dan mendefinisikan nilai default.

# mengakses elemen array
list_array = [1, 2, 3, 4, 5]
print(list_array[0]) # mengakses elemen pertama
print(list_array[1]) # mengakses elemen kedua

var_arr = [0, 5, 19, 60, 765]
left_pointer = var_arr[0] # pointer kiri

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i] # pointer kanan
    if right_pointer > left_pointer:
        left_pointer = right_pointer