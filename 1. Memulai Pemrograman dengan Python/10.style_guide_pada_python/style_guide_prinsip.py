"""
Style Guide Prinsip Penamaan pada Python
Saat membuat variabel, fungsi, hingga kelas, Anda dapat memberikan nama-nama yang beragam. Terkadang, keberagaman tersebut menghasilkan tidak adanya standar dalam kode yang Anda bangun.

Pada materi ini, kita akan belajar beberapa prinsip penamaan saat Anda membangun kode Python. Harapannya, Anda bisa membuat standar nama saat membangun variabel, fungsi, hingga kelas. 

Namun, perlu diperhatikan juga bahwa Anda dapat memilih mempertahankan styling yang sudah digunakan sebelumnya untuk menjaga konsistensi internal tim atau perusahaan. Ini karena konsistensi internal lebih diutamakan.

Catatan: Pada materi-materi sebelumnya, style guide Python belum diterapkan secara menyeluruh. Sangat disarankan jika Anda mempelajari ulang kode pada materi-materi sebelumnya dengan menerapkan style guide Python.

"""


# Prinsip Overriding
# Nama yang dilihat oleh user publik sebaiknya merefleksikan penggunaan/fungsinya dan bukan implementasinya. Misalnya nama fungsi berikut.


cariJalan() 
# Itu akan lebih mudah dipahami dibanding berikut.

jalan()
# Algoritma yang digunakan hingga informasi lainnya dari fungsi yang dibangun dapat dijelaskan dalam docstring ataupun komentar.


"""
Penamaan Deskriptif
Penamaan deskriptif adalah cara untuk memberikan nama yang informatif, jelas, dan sesuai dengan tujuan dari elemen kode. Penamaan deskriptif ini meliputi variabel, fungsi, kelas, hingga konstanta.

Ada berbagai cara penamaan yang umum digunakan dalam Python. Pemilihan cara penamaan ini penting untuk menjaga konsistensi dan kejelasan kode. Penamaan ini juga merujuk pada PEP8 mengenai Naming Conventions dan Naming Styles.

Berikut adalah beberapa cara penamaan yang umum.

    1. Satu karakter huruf kecil: b
    2. Satu karakter huruf besar: B
    3. Huruf kecil: hurufkecil
    4. Huruf kecil dengan pemisah kata garis bawah: huruf_kecil_dengan_pemisah_kata_garis_bawah
    5. Huruf Besar: HURUFBESAR
    6. Huruf Besar dengan pemisah garis bawah: HURUF_BESAR_DENGAN_PEMISAH_GARIS_BAWAH
    7. Huruf Besar di Awal Kata (CapWords, PascalCase): HurufBesarDiAwalKata (pastikan semua singkatan/akronim dituliskan dengan huruf besar, misalnya HTTPServerError, bukan HttpServerError)
    8. Huruf Campuran: hurufCampuran (mirip dengan CapWords, hanya berbeda di karakter paling awal)
    9. Huruf Besar di Awal Kata dengan Garis Bawah: Huruf_Besar_Di_Awal_Kata_Dengan_Garis_Bawah

Satu hal yang perlu diingat ketika Anda membuat sebuah fungsi, sangat tidak disarankan untuk menggunakan frasa atau huruf sebagai awalan fungsi. Awalan fungsi mengacu pada nama fungsi di bagian awal, seperti 'get' pada "get_name()" atau 'konversi' pada "konversi_ke_integer()". 

Python tidak menyarankan atau lebih tepatnya tidak dibutuhkan jika Anda membuat sebuah fungsi yang diawali huruf atau frasa, seperti 'f' jika fungsinya 'f_mean()',  'r' jika fungsinya 'r_name()', dan sebagainya. Python memiliki prinsip yang berlaku dalam penamaan fungsi atau method sebagai berikut.

    1. Atribut dan method name bersifat pre-fixed dengan objek.
    2. Function name selalu diawali dengan module name.

Selain penggunaan huruf atau frase yang tidak direkomendasikan, berikut adalah beberapa bentuk penamaan khusus yang umum ditemukan dalam penamaan fungsi. Ini juga bisa Anda terapkan pada penamaan variabel dan kelas.

    1. _diawali_sebuah_garis_bawah: penamaan ini dapat digunakan untuk penggunaan internal lemah yang merujuk pada penggunaannya dengan lingkup tertentu.
    2. _diakhiri_sebuah_garis bawah_: penamaan ini digunakan untuk mengatasi redundan dengan keyword/reserved words di Python.
    3. __diawali_dua_garis bawah: menegaskan bahwa sebuah objek adalah bagian dari kelas tertentu.
    4. __diawali_dan_diakhiri_dua_garis bawah__: Objek atau atribut tertentu yang diciptakan Python untuk digunakan dalam program. Contohnya adalah  __init__, __import__ or __file__.

Ingat, penamaan ini disebut juga sebagai dunder atau double underscore oleh programmer Python. Anda sangat tidak disarankan membuat penamaan menggunakan dunder. Misalnya Anda membuat penamaan "__special_method__", itu sangat tidak disarankan oleh Python karena bisa ada kemungkinan penamaan tersebut telah digunakan oleh Python dan secara tidak sengaja menimpa kode yang sudah ada. Terkecuali penamaan tersebut sudah terdokumentasikan oleh Python seperti '__init__' yang digunakan untuk membuat class constructor.
"""

"""
Hal-hal yang Harus Dipertimbangkan dalam Penamaan
Sebelumnya kita membahas detail terkait penamaan sebuah fungsi, method, kelas, hingga hal yang tidak dianjurkan dalam penamaannya. Pembahasan selanjutnya adalah petunjuk untuk mempertimbangkan nama yang tepat. Sekali lagi, penamaan di sini merujuk ke banyak hal, seperti penamaan variabel, fungsi, hingga kelas.

Nama yang Dihindari
Hindari karakter l (huruf L kecil), O (huruf o besar), atau I (huruf i besar) sebagai nama variabel satu karakter karena mereka sulit dibedakan dengan angka satu dan nol. Daripada menggunakan l (huruf l kecil), menggunakan L besar akan sangat membantu.



ASCII Compatibility
Merujuk pada PEP 3131,  suatu identifiers yang digunakan dalam Python Standard Library harus kompatibel dengan kode ASCII. ASCII adalah sebuah kode karakter yang memetakan set karakter dan umum digunakan dalam angka. Sederhananya, ASCII memetakan karakter-karakter beserta angka yang mewakilinya.

Identifiers merujuk pada nama-nama yang digunakan untuk menyebut variabel, fungsi, kelas, dan kode lainnya dalam Python. Contoh identifiers adalah nama variabel "x", nama fungsi "penjumlahan()", atau nama method "get_nama()".



Nama Paket dan Nama Modul
Masih ingat dengan modul dan package (paket) dalam Python? Modul pada Python adalah file yang berisi kode Python, seperti fungsi, kelas, dan sebagainya. Ketika Anda membuat script atau file Python, hal itu bisa dianggap sebagai modul. Di sisi lain, paket adalah sebuah direktori yang berisi satu atau lebih modul yang terkait dan saling berhubungan.

Penamaan modul sebaiknya pendek atau singkat, menggunakan huruf kecil, dan opsional garis bawah (_) untuk meningkatkan keterbacaan. Contohnya '__init__.py' atau modul 'math_operations.py' dengan seluruh kode di dalamnya merupakan fungsi, kelas, method yang berhubungan dengan operasi matematika, seperti penjumlahan, pengurangan, dan sebagainya.

Nama paket juga sebaiknya singkat, menggunakan huruf kecil, dan hindari garis bawah(_). Contohnya, jika kita membuat paket bernama "math" yang di dalamnya ada modul 'math_operations.py", pengguna akan memahami bahwa paketnya bernama math yang memiliki banyak modul, seperti salah satunya operasi matematika.
"""


# Nama Kelas
# Saat menamai kelas, gunakan CamelCase atau CapWords. Pastikan semua akronim (misal HTTP) ditulis keseluruhan dengan huruf besar.



# Penulisan Tipe Variabel
# Untuk penamaan variabel, umumnya menggunakan CamelCase atau CapWords, lebih pendek lebih baik.

# T, AnyStr, Num

# Jika terdapat covariant atau contravariant dari sebuah variabel, tambahkan di akhir variabel untuk mempermudah pembacaan. Covariant memungkinkan Anda menggunakan tipe turunan (lebih spesifik) dari yang telah ditentukan sebelumnya. Adapun, contravariant adalah istilah yang merujuk pada kemampuan untuk menggunakan tipe yang lebih umum dari sebelumnya.

from typing import TypeVar
VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)


# Nama Exception
# Untuk pengecualian (exception), Anda juga menerapkan konvensi penamaan kelas pada exception karena ia seharusnya bertipe kelas. Bedanya, tambahkan "Error" atau nama deskriptif lain pada nama exception Anda. Contoh kodenya sebagai berikut.

class DivideByZeroError(Exception):
    def __init__(self, message="Division by zero is not allowed"):
        super().__init__(message)

def divide_numbers(a, b):
    if b == 0:
        raise DivideByZeroError("Cannot divide by zero")
    return a / b

try:
    result = divide_numbers(10, 0)
except DivideByZeroError as e:
    print(f"Error: {e}")

"""
Output:
Error: Cannot divide by zero
"""
        
"""
Pada contoh di atas, kita membuat sebuah pengecualian berasal dari kelas yang dibuat. Kita membuat kelas bernama "DivideByZeroError" yang menginduk pada kelas Exception dari Python. Perhatikan bahwa kita menempatkan kata error di akhir penamaannya.

Nama Variabel Global
Dalam variabel global, penamaannya bisa mengikuti fungsi/modul yang bersifat publik. Anda bisa menggunakan garis bawah untuk menghindari variabel tersebut diimpor jika ia termasuk modul non-publik.



Nama Fungsi, Parameter, dan Variabel
Nama fungsi, parameter, dan variabel sebaiknya menggunakan huruf kecil dengan pemisahan menggunakan garis bawah untuk meningkatkan keterbacaan. mixedCase dapat digunakan jika ada dependensi dengan pustaka menggunakan style tertentu.



Argumen Fungsi dan Method
Dalam pembuatan fungsi dan method pada suatu kelas, ada beberapa hal yang perlu dipertimbangkan.

    1. Gunakan self sebagai argumen pertama jika Anda membuat instance method.
    2. Gunakan cls sebagai argumen pertama ketika Anda membuat class method.

Jika nama argumen fungsi adalah reserved keyword, tambahkan garis bawah di akhir nama argumen. Jangan mengorbankan keterbacaan nama dengan menyingkatnya. Mengganti argumen bernama class dengan class_ atau kelas, lebih baik daripada clss.



Nama Method dan Variabel Instance
Saat membuat method dan variabel dalam suatu kelas, gunakan standar penamaan fungsi, yaitu gunakan huruf kecil dengan pemisah kata garis bawah untuk meningkatkan keterbacaan. Tambahkan garis bawah sebagai awalan untuk method non-publik dan variabel internal pada fungsi.

Untuk menghindari kesamaan dengan subkelas, gunakan __dimulai_dua_garis_nama_method untuk memanggil proses yang tepat. Python menggabungkan nama modul dengan nama kelas. Misal ada suatu kelas bernama Foo, jika kelas Foo memiliki atribut __a, kita tidak dapat mengaksesnya melalui Foo.__a, tetapi Foo._Foo__a. Mulai dengan dua garis bawah hanya digunakan jika terjadi konflik dengan atribut di kelas atau subkelas lainnya.


Konstanta
Dalam memberikan nama variabel bertipe konstanta, umumnya didefinisikan pada bagian atas modul dengan huruf besar semuanya, misalnya 'PI = 3,14'  atau  'TOTAL = 4.14213'.

"""

# Selalu Persiapkan untuk Inheritance
# Saat membangun metode dan variabel dalam sebuah kelas, sebaiknya Anda dapat langsung mengetahui atribut pada metode dan variabel tersebut, entah publik atau non-publik. Jika Anda ragu, jadikan atributnya non-publik. Sebab, lebih mudah menjadikan sebuah variabel/method bersifat non-publik menjadi publik, dibandingkan sebaliknya.

# Variabel atau method bersifat non-publik adalah suatu variabel atau method yang hanya digunakan untuk lingkup tertentu dan tidak diakses secara langsung di luar. Contohnya berikut.

class MyClass:
    def __init__(self):
        self._private_var = 42   # Variabel non publik dengan awalan satu garis bawah
        self._secret_list = [1, 2, 3]  # Variabel non publik lainnya

    def _private_method(self):
        print("Ini adalah method non publik")

    def public_method(self):
        print("Ini adalah method publik")
        self._private_method()  # Method publik dapat memanggil method non publik

"""      
Pada contoh di atas, method '_private_method' merupakan jenis fungsi yang tidak diakses secara langsung. Anda bisa melihat pada method 'public_method', tempat kita menggunakan method private di sana. Selain itu, variabel seperti '_private_var' atau '_secret_list' merupakan variabel non_publik yang tidak digunakan secara langsung ketika kelas dipanggil.

Method/Variabel publik dipersiapkan untuk pihak eksternal menggunakan kelas Anda. Anda juga otomatis berkomitmen untuk menghindari adanya incompatible backward changes atau suatu kode yang tidak dapat berjalan kembali setelah adanya perubahan. 

Sebaliknya, method/variabel dengan atribut non-publik hanya digunakan oleh Anda sebagai developer. Itu juga tidak memberikan garansi kepada siapa pun bahwa Anda takkan mengubah atau menghapusnya. Di sini kita tidak menggunakan atribut private karena dalam Python tidak ada atribut yang benar-benar private.

Kategori lain dari atribut adalah "subclass API", umumnya disebut protected pada bahasa lain. Sebuah kelas dapat didesain untuk diwariskan (inherited-from), misalnya untuk memodifikasi atau menjadi ekstensi dari perilaku (behavior) kelas. Dalam mendesain kelas-kelas sejenis, pastikan untuk membuat keputusan eksplisit, variabel/method yang memiliki atribut publik, bagian dari subclass API, dan yang hanya anda gunakan secara internal.

Saat mendeklarasikan variabel/method tersebut, ikuti panduan Pythonic berikut.

    1. Atribut publik tidak menggunakan awalan garis bawah.
    2. Jika nama sebuah method/variabel publik sama dengan reserved keyword, tambahkan akhiran garis bawah. Hindari menyingkat atau mengurangi huruf.
    3. Pada data publik yang bersifat simpel, hindari nama yang terlalu panjang. Cukup dengan nama atribut sependek mungkin. Ingatlah bahwa pada masa depan Anda akan mungkin mengembangkan skema atau data ini sehingga nama sependek apa pun mungkin akan menguntungkan Anda.
    4. Jika Anda berniat untuk mewariskan atau membuat subclass dari kelas dan menginginkan sebuah variabel hanya digunakan di kelas utama saja, tambahkan awalan dua garis bawah. Ini akan memudahkan Anda karena Python mengenalinya sebagai konvensi kelas, untuk menghindari kemungkinan kesamaan nama atau implementasi.
    
Sekali lagi, semua materi style guide kali ini mengacu pada PEP8 yang dapat Anda baca lebih lanjut dalam link berikut.

"""