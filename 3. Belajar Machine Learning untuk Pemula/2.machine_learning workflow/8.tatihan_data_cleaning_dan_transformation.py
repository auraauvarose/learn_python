import pandas as pd
test = pd.read_csv("3. Belajar Machine Learning untuk Pemula/2.machine_learning workflow/test.csv")
print(test.head())


test.info() # Menampilkan informasi tentang DataFrame, termasuk jumlah entri, tipe data, dan penggunaan memori.
test.describe(include='all') # Menampilkan statistik deskriptif dari DataFrame, termasuk nilai unik, frekuensi, dan statistik numerik.

test = test.isnull().sum() # Menghitung jumlah nilai yang hilang (NaN) dalam setiap kolom dari DataFrame.
test[test > 0]  