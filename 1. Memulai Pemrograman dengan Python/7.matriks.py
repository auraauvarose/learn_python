import numpy # Library NumPy sering dipakai oleh programmer Python untuk melakukan tugas-tugas dalam ranah science dan engineering karena dianggap memiliki penggunaan penyimpanan memori yang efisien.
import numpy as np # NumPy adalah library Python yang digunakan untuk melakukan komputasi numerik. NumPy menyediakan objek array multidimensi yang efisien dan fungsi-fungsi untuk memanipulasi array tersebut.

# Pada materi sebelumnya, kita telah mempelajari cara menyimpan data yang sama menggunakan array dalam Python dengan list. Untuk pengingat, array merupakan salah satu jenis struktur data linear dan terdiri dari kumpulan elemen bertipe data sama dengan indeks yang berurutan atau linear. 

# Sebenarnya, array adalah jenis struktur data 1 dimensi yang menyimpan semua datanya secara linear. Pada materi ini, kita akan mempelajari jenis array 2 dimensi, yakni matriks.

""" Sementara itu dalam pemrograman, matriks adalah kumpulan data yang diatur dalam bentuk tabel dua dimensi dengan setiap elemennya terdefinisi berdasarkan baris dan kolom. Matriks dalam pemrograman diimplementasikan menggunakan array dua dimensi. Bahkan dalam Python, matriks dapat diimplementasikan menggunakan nested list atau list di dalam list. """
matriks = [[1,2,3,4,5],
           [1,2,3,4,5],
           [1,2,3,4,5]]

matriks2 = numpy.array([[1,2,3,4,5],
                       [1,2,3,4,5],
                       [1,2,3,4,5]])
print(matriks2)

print("   ")

# Deklarasi Matriks ada 2
# 1. Deklarasi sekaligus inisialisasi nilai matrikss
matriks = [[1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 2, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]]
     
print(matriks)
print(matriks[2][3]) # Dalam pemrograman, nilai tersebut bisa diasumsikan dengan "[2][2]" dengan nilai 2 adalah indeks atau nomor baris dan nilai 3 adalah indeks atau nomor kolom. indeks dimulai dari 0

print("   ")

# 2. Deklarasi dengan nilai default.
matriks = [[0 for i in range(4)] for j in range(5)]
print(matriks)

# Operasi Matriks pada Python
var_mat = np.array([[5, 0,],
                   [1, -2]])

result = var_mat * 2 # Perkalian matriks dengan bilangan bulat
print(result)