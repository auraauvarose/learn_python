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

print("  ")

# Atribut
# Dalam Python, ada dua jenis atribut kelas yang dapat dibagi, yaitu atribut kelas dan atribut objek atau instance. Atribut kelas adalah jenis atribut yang secara otomatis terdefinisi dan menjadi bawaan kelas ketika instance dibuat berdasarkan kelas tersebut. Anda dapat menganggapnya sebagai nilai default atau bawaan dari kelas. Jika Anda membuat beberapa objek berdasarkan kelas yang memiliki jenis atribut ini, setiap objek akan memiliki atribut yang sama dengan nilai yang sama. 

# atribut objek atau instance
mobil_1 = Mobil()
print(mobil_1.warna) # output: merah
mobil_2 = Mobil() 
print(mobil_2.warna) # output: merah

Mobil.warna = "hitam" # mengubah atribut warna dari class Mobil

print(mobil_1.warna) # output: hitam
print(mobil_2.warna) # output: hitam

# Class Constructor
class Warna:
    def __init__(self):
        self.color = "hijau"


color_1 = Warna()
color_2 = Warna()

print(color_1.color) # output: hijau
print(color_2.color) # output: hijau

color_1.color = "biru"

color_1 = Warna() # membuat objek baru
color_2 = Warna() # membuat objek baru

print(color_1.color) # output: biru
print(color_2.color) # output: hijau


print("  ")

# Constructor adalah method khusus yang dipanggil ketika kita membuat objek dari class. Constructor ini digunakan untuk menginisialisasi atribut-atribut dari objek tersebut. Dalam Python, constructor didefinisikan dengan nama method __init__ (double underscore) dan diikuti dengan parameter self yang merujuk pada objek itu sendiri.

# contoh lain

class Sepeda:
    def __init__(self, warna, kecepatan, merek):
        self.warna = warna
        self.kecepatan = kecepatan
        self.merek = merek

sepeda_1 = Sepeda("Biru", 20, "Polygon")
print(sepeda_1.warna) # output: Biru
print(sepeda_1.kecepatan) # output: 20
print(sepeda_1.merek) # output: Polygon



# Method
"""
Setelah atribut, saatnya membahas method sebagai perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas. Pada pembuatan metode , sebenarnya kita membuat fungsi di dalam kelas itu sendiri. Dengan kata lain, kita menggunakan kata kunci "def" atau membuat fungsi sebagai suatu metode. Python membagi method menjadi tiga jenis.

1. Metode dari object (object method).
2. Metode secara statis (static method).
3. Metode dari class (class method).

Dua metode terakhir sangat erat kaitannya dengan konsep dekorator. Kita tidak akan membahasnya lebih detail mengenai dekorator, tetapi secara umum saja. 
"""

# Dekorator adalah fungsi dalam Python yang mengembalikan fungsi lain, biasanya diawali dengan sintaks "@" di awal.  Contoh sederhana dekorator sebagai berikut.

def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dipanggil")
        func()
        print("Setelah fungsi dipanggil")
    return wrapper

# dekorasi fungsi dengan decoorator
@my_decorator
def say_hello():
    print("Hello, World!")

# Memanggil fungsi yang sudah didekorasi
say_hello()

print("  ")

"""
Metode dari Objek (Object Method)
Jenis pertama adalah method yang melekat terhadap objek. Ciri dari jenis metode ini adalah adanya parameter self yang merujuk pada objek saat ini. Perhatikan contoh di bawah ini, asumsikan bahwa kita membuat kelas mobil yang sama seperti sebelumnya. Namun, kita menambahkan metode bernama "tambah_kecepatan" dan setiap metode ini dipanggil maka kecepatan mobil akan bertambah 10.

"""

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan


    def tambah_kecepatan(self):
            self.kecepatan += 10

mobil_1 = Mobil("Biru", "Toyota", 50)
print("Sebelum ditambahkan :")
print(mobil_1.kecepatan) # output: 50

mobil_1.tambah_kecepatan() # memanggil method tambah_kecepatan

print("Setelah ditambahkan :")
print(mobil_1.kecepatan) # output: 60

print("   ")

"""
Metode secara Statis (Static Method)
Static method adalah fungsi atau method pada sebuah kelas yang bersifat statis. Artinya, metode atau fungsi ini bersifat independen dan tidak terikat pada instance kelas. Metode ini dapat dianggap seperti kita membuat fungsi seperti biasa, tetapi didefinisikan dalam kelas sehingga ini menjadi perilaku untuk kelas tersebut. Untuk membuat static method, Anda bisa menambahkan dekorator @staticmethod tepat sebelum mendefinisikan fungsi atau metode.

"""

class Mobil:
    def __init__(self, merek):
        self.merek = merek

    
    @staticmethod
    def intro_mobil():
        print("Mobil adalah kendaraan yang memiliki empat roda dan digunakan untuk transportasi.")

Mobil.intro_mobil() # output: Mobil adalah kendaraan yang memiliki empat roda dan digunakan untuk transportasi.
mobil_1 = Mobil("Toyota")
mobil_1.intro_mobil() # output: Mobil adalah kendaraan yang memiliki empat roda dan digunakan untuk transportasi.

print("  ")

"""
Metode dari Kelas (Class Method)
Metode terakhir adalah class method yang termasuk jenis metode cukup spesial dalam Python. Jika object method identik dengan parameter self yang merujuk pada objek, class method juga memerlukan sebuah parameter yang merujuk pada kelas. Mari buat contoh yang sama dengan sebelumnya, tetapi kali ini menggunakan class method.

"""

class Mobil:
    def __init__(self, merek):
        self.merek = merek

# Pada bagian fungsi intro_mobil, kita menambahkan parameter cls. Ini adalah parameter wajib dalam menggunakan dekorator @classmethod.
    @classmethod 
    def intro_mobil(cls): 
        print("Ini adalah metode dari kelas Mobil")
# Catatan:
# Penamaan cls merupakan kesepakatan bersama dari programmer Python untuk memudahkan pembacaan kode. Anda dapat mengganti namanya, tidak harus cls.
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()



"""
Inheritance (Pewarisan)
Sebagaimana ilustrasi awal, kita dapat membuat sebuah kelas baru dengan menggunakan kelas induk yang sudah ada. Konsep ini disebut dengan 'inheritance' atau dalam bahasa Indonesia artinya pewarisan.

"""

class Kendaraan:
    def  __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def kecepatan_mobil(self):
        self.kecepatan += 10

class Mobilsport(Kendaraan): # Mobilsport adalah turunan dari class Kendaraan
    def turbo(self):
        self.kecepatan += 50

# Mobil dasar
mobil_1 = Kendaraan("Biru", "Toyota", 150)
print(mobil_1.kecepatan) # output: 150

# Mobil menengah 
mobil_1.kecepatan_mobil() # Memanggil method untuk menambah kecepatan
print(mobil_1.kecepatan) # output: 160

# mobil sport
mobil_sport_1 = Mobilsport("Merah", "Ferrari", 200)
print(mobil_sport_1.kecepatan) # output: 200
mobil_sport_1.turbo() # Menambah kecepatan dengan turbo
print(mobil_sport_1.kecepatan) # output: 250


"""
Override
Selanjutnya, seperti yang dijelaskan di awal, ketika kita membuat metode baru di kelas turunan (kelas baru) dengan nama yang sama seperti metode di kelas induk, itu akan menyebabkan metode baru menimpa (override) metode dari kelas induk.

"""


class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self): # tambah_kecepatan
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self): # tambah_kecepatan
        self.kecepatan += 20

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)



"""
Super
Lantas, bagaimana cara untuk kita ingin menggunakan metode atau atribut dari kelas induk, tetapi tidak ingin menuliskan ulang semua kode? Ini adalah tujuan dari adanya super dalam konsep OOP. Nama super sebenarnya merujuk pada kelas induk yang disebut juga sebagai super class. Kita bisa memanfaatkan konsep ini untuk menghindari kode berulang dan memanfaatkan fungsi yang sudah ada pada kelas induk (super class).

"""

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "DicodingSportCar", 160)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

"""
TODO:
1. Buatlah class bernama Animal dengan ketentuan:
    - Memiliki properti:
      - name: string
      - age: int
      - species: string
    - Memiliki constructor untuk menginisialisasi properti:
      - name
      - age
      - species
2. Buatlah class bernama Cat dengan ketentuan:
    - Merupakan turunan dari class Animal
    - Memiliki method:
      - bernama "deskripsi" yang mengembalikan nilai string berikut ini.
        "{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
      - bernama "suara" yang akan mengembalikan nilai string "meow!"
 3. Buatlah instance dari kelas Cat bernama "myCat" dengan ketentuan:
    - Atribut name bernilai: "Neko"
    - Atribut age bernilai: 3
    - Atribut species bernilai: "Persian".
    
"""

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

class Cat(Animal):
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    
    def suara(self):
        return "meow!"
    
myCat = Cat("Neko", 3, "Persian")
print(myCat.deskripsi()) # output: Neko adalah kucing berjenis Persian yang sudah berumur 3 tahun
