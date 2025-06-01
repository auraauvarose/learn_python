import pandas as pd
test = pd.read_csv("3. Belajar Machine Learning untuk Pemula/2.machine_learning workflow/test.csv") 
print(test.head())

print("\n")

test.info() # Menampilkan informasi tentang DataFrame, termasuk jumlah entri, tipe data, dan penggunaan memori.
test.describe(include='all') # Menampilkan statistik deskriptif dari DataFrame, termasuk nilai unik, frekuensi, dan statistik numerik.

print("\n")

"""
Anda perlu melakukan pemeriksaan terhadap data yang hilang (missing value). Tujuannya untuk mencegah kesalahan ketika melakukan analisis, mencegah error pada model, dan meningkatkan performa model. Dengan melakukan pemeriksaan missing value, Anda dapat memastikan bahwa proses analisis data dan pelatihan model machine learning berjalan dengan baik sehingga hasil yang diperoleh lebih valid dan akurat. Berikut salah satu contoh kode untuk melakukan pemeriksaan missing value.

"""
# Memeriksa jumlah nilai yang hilang di setiap kolom
missing_values = test.isnull().sum()
missing_values[missing_values > 0]

print(missing_values)

print("\n")

"""
Mengatasi Missing Value
Perhatikan jumlah data yang hilang pada hasil kode sebelumnya, tentunya sangat banyak sekali data yang hilang ‘kan? Sebagai informasi jumlah data pada train.csv ini berjumlah 1460 baris sehingga jika salah satu fitur memiliki missing value lebih dari 1000, dapat kita asumsikan terlalu banyak data yang hilang. Lalu bagaimana solusinya? 

Pertama-tama, mari kita pisahkan kolom yang memiliki missing value lebih dari 75% dan kurang dari 75%.

"""

less = missing_values[missing_values > 0].index
over = missing_values[missing_values >= 1000].index


print("Kolom dengan missing value kurang dari 75%:")
print(less)
print("\n")
print("Kolom dengan missing value lebih dari 75%:")
print(over)

print("\n")

"""
Berdasarkan hasil dari langkah sebelumnya, kita akan memutuskan bagaimana menangani nilai yang hilang dengan dua cara.

Mengisi Nilai yang Hilang: data di atas terdapat beberapa fitur yang memiliki missing value kurang dari 75% dari jumlah skala pada data. Namun, perlu Anda catat bahwa seluruh fitur tersebut memiliki tipe data yang berbeda. Sehingga penanganan missing value-nya pun perlu dibedakan.

Mari kita mulai dengan mengatasi missing value untuk tipe data numerik.

"""
numeric_features = test[less].select_dtypes(include=['number']).columns
test[numeric_features] = test[numeric_features].fillna(test[numeric_features].median())

print(numeric_features)

print("\n")
"""
Selanjutnya, kita perlu menangani permasalahan yang serupa pada data yang bertipe object atau string. Sedikit berbeda dengan kasus data numerik, pada kasus ini kita tidak bisa menggunakan median, mean, atau fungsi agregasi lainnya. Biasanya ada dua cara yang sering dilakukan untuk mengatasi permasalahan missing value pada data kategori.

    1. Mengisi Missing Value dengan Modus (Nilai yang Paling Sering Muncul): pendekatan ini cukup umum karena nilai modus sering kali merupakan representasi yang baik untuk data yang hilang dalam konteks kategorikal.
    2. Mengisi dengan Kategori Baru (Misalnya "Unknown" atau "Missing"): ini adalah cara lain untuk menangani missing value dengan menandai data yang hilang sebagai kategori baru.
    
Pada contoh kasus ini, mari kita atasi dengan mengisi missing value dengan modus atau nilai yang paling sering muncul pada masing-masing fitur.


"""

kategoriie = test[less].select_dtypes(include=['object']).columns

for column in kategoriie:
    test[column] = test[column].fillna(test[column].mode()[0])
    
print(kategoriie)

"""
Menghapus Kolom dengan Banyak Nilai yang Hilang:jika ada kolom dengan terlalu banyak nilai yang hilang, kita bisa mempertimbangkan untuk menghapusnya (pada kasus ini kita mengambil batasan 75%). Untuk mengatasi kasus ini sangatlah mudah, pertama Anda perlu mengambil index atau nama kolom dari fitur yang memiliki missing value lebih dari batasan yang sudah ditentukan (Anda dapat lihat kode ketika memisahkan kolom di atas). Kemudian hal yang perlu dilakukan adalah menghapus kolom tersebut sesuai dengan nama fitur yang sudah ditentukan sebelumnya

"""

# Menghapus kolom dengan terlalu banyak nilai yang hilang
df = test.drop(columns=over)

