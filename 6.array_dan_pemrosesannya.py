# Fundamental Array 
# Python tidak memiliki tipe data array yang sering digunakan dalam bahasa pemrograman lain. Sebaliknya, Python memiliki tipe data list yang dapat dikatakan mirip, tetapi tak sama dengan array. 

x = [1, 2, 3, 4, 5] # list ini bisa sama tapi tidak sama dengAN tipe data array
print(x)

# Library merupakan sekumpulan kode yang telah dibuat oleh developer atau programmer dan disediakan kepada pengguna lain agar dapat digunakan ulang dalam pengembangan program atau perangkat lunak. Adapun modul merupakan file yang berisikan kode Python dan dapat digunakan kembali oleh programmer lainnya.

import array
x = array.array('i', [1, 2, 3, 4, 5]) # array ini sama dengan tipe data array
print(x)
print(type(x)) # tipe data array