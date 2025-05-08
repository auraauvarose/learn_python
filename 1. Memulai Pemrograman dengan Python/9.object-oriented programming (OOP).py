# Duck Typing 

"""
Jika diterjemahkan ke dalam bahasa Indonesia, kalimat di atas mengandung arti "Jika sesuatu berjalan seperti bebek dan bersuara seperti bebek, kemungkinan besar ia adalah bebek".

Konsep duck typing tidak berkaitan langsung dengan dynamic typing atau loosely typed, ini merupakan konsep yang lebih erat dengan materi kita kali ini, yaitu pemrograman berorientasi objek (object-oriented programming). Duck typing menjelaskan bahwa sebuah tipe atau class dari sebuah object tidak lebih penting daripada method yang menjadi perilakunya. 

Class, object, dan method akan kita bahas secara mendalam pada materi kali ini. Kita hanya akan berkenalan terlebih dahulu secara umum sebelum spesifik membahasnya. Sebenarnya, Python ingin memberikan keleluasaan terhadap para developernya untuk tidak perlu mencemaskan tentang tipe atau kelas (class) dari sebuah objek (object), yang lebih penting adalah kemampuan melakukan operasinya (method). 

"""

# Class, Object, dan Method

""" 
Secara umum, konsep OOP dalam pemrograman sangat mirip seperti ilustrasi-ilustrasi di atas. Object-oriented programming adalah paradigma pemrograman berorientasi pada pengorganisasian kode menjadi objek-objek yang memiliki atribut dan perilaku (method). Objek merupakan perwujudan dari class dengan anggapan bahwa kelas adalah cetakan yang memungkinkan kita dapat membuat banyak objek berdasarkan cetakan tersebut.

"""

# Class
# Pembuatan class dalam Python mirip seperti fungsi, yakni perlu menggunakan keyword untuk bisa membuatnya. Keyword atau kata kunci untuk membuat kelas dalam Python adalah "class".
class Mobil: 
    warna = "merah" # atribut

# Object (Objek)
# Objek adalah perwujudan dari class. Kita bisa membuat objek dari class yang sudah kita buat sebelumnya. Untuk membuat objek, kita cukup memanggil nama class tersebut layaknya kita memanggil fungsi.

mobil_1 = Mobil() # objek dari class Mobil
mobil_1.warna = "biru" # mengubah atribut warna dari objek mobil_1
print(mobil_1.warna) # output: merah ke biru, nama objek dan atributnya


# Atribut
# Dalam Python, ada dua jenis atribut kelas yang dapat dibagi, yaitu atribut kelas dan atribut objek atau instance. Atribut kelas adalah jenis atribut yang secara otomatis terdefinisi dan menjadi bawaan kelas ketika instance dibuat berdasarkan kelas tersebut. Anda dapat menganggapnya sebagai nilai default atau bawaan dari kelas. Jika Anda membuat beberapa objek berdasarkan kelas yang memiliki jenis atribut ini, setiap objek akan memiliki atribut yang sama dengan nilai yang sama. 

mobil_1 = Mobil()
print(mobil_1.warna) # output: merah
mobil_2 = Mobil() 
print(mobil_2.warna) # output: merah

Mobil.warna = "hitam" # mengubah atribut warna dari class Mobil

print(mobil_1.warna) # output: hitam
print(mobil_2.warna) # output: hitam