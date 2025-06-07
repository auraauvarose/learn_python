import pandas as pd
import joblib

# Load model dan tools preprocessing
kmeans = joblib.load('best_model_clustering.pkl')
classifier = joblib.load('best_model_classifier.pkl')
scaler = joblib.load('scaler.pkl')
encoders = joblib.load('encoders.pkl')

# Load data test
test = pd.read_csv('3. Belajar Machine Learning untuk Pemula/2.machine_learning workflow/test.csv')

# Hapus kolom ID yang tidak relevan
id_columns = ['TransactionID', 'AccountID', 'DeviceID', 'IPAddress', 'MerchantID']
test_processed = test.drop(columns=id_columns, errors='ignore')

# Preprocessing numerik
numeric_features = test_processed.select_dtypes(include='number').columns.tolist()
test_processed[numeric_features] = scaler.transform(test_processed[numeric_features])

# Preprocessing kategorikal
categorical_features = test_processed.select_dtypes(include='object').columns.tolist()
for col in categorical_features:
    encoder = encoders[col]
    # Pastikan semua nilai sudah ada di encoder, jika tidak, ganti dengan -1 atau kategori lain
    test_processed[col] = test_processed[col].map(lambda x: encoder.transform([x])[0] if x in encoder.classes_ else -1)

# Prediksi cluster KMeans
test['Cluster'] = kmeans.predict(test_processed)

# Prediksi klasifikasi (jika ingin)
test['Cluster_Class'] = classifier.predict(test_processed)

# Simpan hasil prediksi
test.to_csv('test_with_cluster.csv', index=False)
print("Prediksi cluster dan klasifikasi pada test.csv selesai! Hasil disimpan di test_with_cluster.csv")