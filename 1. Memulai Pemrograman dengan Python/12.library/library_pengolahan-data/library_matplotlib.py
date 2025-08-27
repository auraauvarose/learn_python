"""
Matplotlib
Selanjutnya adalah matplotlibyang merupakan library untuk melakukan visualisasi data. Matplotlib termasuk jenis library eksternal sehingga Anda perlu melakukan instalasi matplotlib terlebih dahulu. Silakan jalankan kode berikut.

python -m pip install -U matplotlib

Anda bisa juga jalankan kode berikut jika ingin menggunakan conda.

conda install matplotlib

"""

import matplotlib.pyplot as plt

# Data 
x = [1, 3, 5, 7, 9]
y = [2, 4, 6, 8, 10]

# Plot Garis
plt.plot(x, y)

# Menambahkan Judul dan label sumbu

plt.title("Contoh plot garis")
plt.xlabel("Sumbu x")
plt.ylabel("Sumbu y")

plt.show()

"""
Pada kode di atas, kita akan membuat visualisasi berdasarkan data dari variabel x dan y. Hal pertama yang dilakukan adalah mengimpor library dengan menggunakan sintaks “import matplotlib.pyplot as plt".

Selanjutnya, ini adalah contoh sehingga kita perlu membuat variabel sebagai data yang akan digunakan. Di sini kita membuat variabel x dan y sebagai data yang akan divisualisasi.

Untuk membuat visualisasinya, kita menggunakan sintaks “plt.plot(x, y)” dengan argumennya adalah variabel x dan y. Lalu, kita menambahkan informasi tambahan seperti title, xlabel, dan ylabel. Terakhir, kita menampilkan visualisasi tersebut dengan sintaks “plt.show()”.

"""