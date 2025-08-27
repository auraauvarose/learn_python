"""
Latihan: Exploratory dan Explanatory Data Analysis
Masih ingatkah Anda dengan tahapan data cleaning dan transformation pada materi sebelumnya? Selamat jika Anda mengikuti dan mengerjakan latihan tersebut karena pada tahapan ini, kita akan melanjutkan hasil dari proses sebelumnya. 


Karena pada tahapan data cleaning dan transformation Anda telah melakukan analisis deskriptif, pada tahapan ini kita memiliki asumsi bahwa data tersebut sudah bersih dan terdistribusi dengan baik. Bagaimana cara membuktikannya? Salah satu caranya adalah memeriksa kembali missing value pada dataset yang akan digunakan. 

"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt 
import seaborn as sns

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
fig, exes = plt.subplots(n_rows, n_cols, figsize=(10, n_rows * 4))

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
# plt.tight_layout()
# plt.show() 

"""
Selanjutnya, mari kita visualisasikan distribusi beberapa kolom serta melihat korelasi antara variabel numerik. 

"""

# Visualisasi distribusi beberapa kolom
# Visualisasi distribusi data untuk beberapa kolom
columns_to_plot = ['OverallQual', 'YearBuilt', 'LotArea', 'SaleType', 'SaleCondition']
 
plt.figure(figsize=(15, 10))
for i, column in enumerate(columns_to_plot, 1):
    plt.subplot(2, 3, i)
    sns.histplot(df_lencoder[column], kde=True, bins=30)
    plt.title(f'Distribution of {column}')
 
plt.tight_layout()
plt.show()

"""
Berikutnya, kita perlu melakukan analisis korelasi dengan membuat matriks korelasi. Matriks korelasi menunjukkan beberapa hubungan penting antara variabel-variabel yang ada dalam dataset. Biasanya warna yang lebih terang atau lebih gelap mengindikasikan korelasi yang lebih kuat (positif atau negatif). Untuk melakukan analisis korelasi Anda dapat menggunakan kode berikut sebagai panduan awal.

"""

# Visualisasi korelasi antar variabel numerik
plt.figure(figsize=(12, 10))
correlation_matrix = df_lencoder.corr()
 
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()


"""
Pada tahapan ini, sebetulnya Anda bisa saja mengurangi fitur atau variabel yang tidak memiliki hubungan linier dengan variabel target (pada kasus ini SalePrice). Untuk mempermudah proses analisis tersebut, mari kita buat matriks korelasi hanya terhadap variabel atau fitur SalePrice saja sebagai variabel dependen pada studi kasus ini.
 
"""

# Menghitung korelasi antara variabel target dan semua variabel lainnya
target_corr = df_lencoder.corr()['SalePrice']
 
# (Opsional) Mengurutkan hasil korelasi berdasarkan korelasi
target_corr_sorted = target_corr.abs().sort_values(ascending=False)
 
plt.figure(figsize=(10, 6))
target_corr_sorted.plot(kind='bar')
plt.title(f'Correlation with SalePrice')
plt.xlabel('Variables')
plt.ylabel('Correlation Coefficient')
plt.show()


"""
Kesimpulannya exploratory data analysis (EDA) dan explanatory data analysis (ExDA) adalah dua langkah penting dalam analisis data yang saling melengkapi. EDA bertujuan untuk memahami pola, anomali, dan struktur dalam data secara mendalam melalui visualisasi dan teknik statistik tanpa asumsi awal, sehingga membuka wawasan baru dan membantu membentuk hipotesis. Sebaliknya, ExDA fokus pada komunikasi temuan yang jelas dan meyakinkan, menggunakan visualisasi dan narasi yang efektif untuk menjelaskan dan mendukung argumen berdasarkan hasil analisis. Keduanya esensial untuk menghasilkan analisis yang valid dan dapat dimengerti oleh berbagai pemangku kepentingan (stakeholder).

"""