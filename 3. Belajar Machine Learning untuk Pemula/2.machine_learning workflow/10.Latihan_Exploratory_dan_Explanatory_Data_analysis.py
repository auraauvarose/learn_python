"""
Latihan: Exploratory dan Explanatory Data Analysis
Masih ingatkah Anda dengan tahapan data cleaning dan transformation pada materi sebelumnya? Selamat jika Anda mengikuti dan mengerjakan latihan tersebut karena pada tahapan ini, kita akan melanjutkan hasil dari proses sebelumnya. 


Karena pada tahapan data cleaning dan transformation Anda telah melakukan analisis deskriptif, pada tahapan ini kita memiliki asumsi bahwa data tersebut sudah bersih dan terdistribusi dengan baik. Bagaimana cara membuktikannya? Salah satu caranya adalah memeriksa kembali missing value pada dataset yang akan digunakan. 

"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt 

test = pd.read_csv("3. Belajar Machine Learning untuk Pemula/2.machine_learning workflow/test.csv")

print(test.head())
missing_values = test.isnull().sum()

print("\n")

"""
Bagian ini mengisi missing value pada kolom numerik dengan nilai median dari masing-masing kolom. Ini adalah cara yang umum dan aman untuk data numerik, terutama jika ada outlier.

"""
mumeric_features = test.select_dtypes(include=['number']).columns
test[mumeric_features] = test[mumeric_features].fillna(test[mumeric_features].median())


"""
Penjelasan:
Bagian ini mengisi missing value pada kolom bertipe kategori (object/string) dengan modus (nilai yang paling sering muncul) di kolom tersebut. Ini adalah cara yang umum untuk data kategori.

"""
kategoriie = test.select_dtypes(include=['object']).columns

for column in kategoriie:
    test[column] = test[column].fillna(test[column].mode()[0])

df_lencoder = test.copy()

le = LabelEncoder()
for col in df_lencoder.select_dtypes(include=['object']).columns:
    df_lencoder[col] = le.fit_transform(df_lencoder[col].astype(str))

missing_values = df_lencoder.isnull().sum()
missing_percentage = (missing_values / len(df_lencoder)) * 100


missing_data = pd.DataFrame({
    'Missing Values': missing_values,
    'Missing Percentage': missing_percentage
}).sort_values(by='Missing Values', ascending=False)


missing_data[missing_data['Missing Values'] > 0]

print("\nMissing Values and Percentages:")
print(missing_data)

"""
Seperti yang Anda lihat pada output di atas, tidak terdapat satu pun missing value karena kita sudah menangani permasalahan tersebut pada materi sebelumnya. Selanjutnya, lakukan analisis deskriptif menggunakan .describe() atau membuat histogram agar distribusi data lebih terlihat. Karena kita telah mempelajari fungsi .describe(), pada latihan ini akan menggunakan histogram untuk melihat sebaran data.

"""

# Menghitung jumlah variabel
num_vars = df_lencoder.shape[1]

# Menentukan jumlah baris dan kolom untuk grid subplots
n_cols = 4 # Jumlah kolom yang inginkan ditampilkan
n_rows = -(-num_vars // n_cols)  # Menghitung jumlah baris yang diperlukan

# Membuat subplot
fig, exes = plt.subplots(n_rows, n_cols, figsize=(20, n_rows * 4))

# flatten exes array untuk iterasi yang lebih mudah
axes = exes.flatten()

# Plot setiap variabel
for i, col in enumerate(df_lencoder.columns):
    df_lencoder[column].hist(ax=axes[i], bins=20, edgecolor='black')
    axes[i].set_title(column)
    axes[i].set_xlabel('Value')
    axes[i].set_ylabel('Frequency')
    
# Menghapus subplot yang tidak dipakai (jika ada)
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

# Menyesuikan layout agar lebih rapi
plt.tight_layout()
plt.show()
