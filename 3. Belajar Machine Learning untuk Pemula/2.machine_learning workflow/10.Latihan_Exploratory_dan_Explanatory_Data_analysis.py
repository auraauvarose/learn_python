"""
Latihan: Exploratory dan Explanatory Data Analysis
Masih ingatkah Anda dengan tahapan data cleaning dan transformation pada materi sebelumnya? Selamat jika Anda mengikuti dan mengerjakan latihan tersebut karena pada tahapan ini, kita akan melanjutkan hasil dari proses sebelumnya. 


Karena pada tahapan data cleaning dan transformation Anda telah melakukan analisis deskriptif, pada tahapan ini kita memiliki asumsi bahwa data tersebut sudah bersih dan terdistribusi dengan baik. Bagaimana cara membuktikannya? Salah satu caranya adalah memeriksa kembali missing value pada dataset yang akan digunakan. 

"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

test = pd.read_csv("3. Belajar Machine Learning untuk Pemula/2.machine_learning workflow/test.csv")

print(test.head())
missing_values = test.isnull().sum()

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