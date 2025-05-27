import pandas as pd
test = pd.read_csv("3. Belajar Machine Learning untuk Pemula/2.machine_learning workflow/test.csv") 
print(test.head())


test.info() # Menampilkan informasi tentang DataFrame, termasuk jumlah entri, tipe data, dan penggunaan memori.
test.describe(include='all') # Menampilkan statistik deskriptif dari DataFrame, termasuk nilai unik, frekuensi, dan statistik numerik.

# Memeriksa jumlah nilai yang hilang di setiap kolom
missing_values = test.isnull().sum()
missing_values[missing_values > 0]


"""
Mengatasi Missing Value
Perhatikan jumlah data yang hilang pada hasil kode sebelumnya, tentunya sangat banyak sekali data yang hilang ‘kan? Sebagai informasi jumlah data pada train.csv ini berjumlah 1460 baris sehingga jika salah satu fitur memiliki missing value lebih dari 1000, dapat kita asumsikan terlalu banyak data yang hilang. Lalu bagaimana solusinya? 

Pertama-tama, mari kita pisahkan kolom yang memiliki missing value lebih dari 75% dan kurang dari 75%.

"""
less = missing_values[missing_values > 0].index
over = missing_values[missing_values >= 1000].index
print("Kolom dengan missing value kurang dari 75%:")
print(less)
print("Kolom dengan missing value lebih dari 75%:")
print(over)