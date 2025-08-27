# ==============================================================================
# Tahap 0: Import Library yang Dibutuhkan
# ==============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

sns.set(style="whitegrid")

# ===================== 1. Memuat Data =====================
df = pd.read_csv("3. Belajar Machine Learning untuk Pemula/2.machine_learning workflow/train.csv")
df_original = df.copy()

print("===== 5 Data Teratas =====")
print(df.head())
print("\n" + "="*30 + "\n")

print("===== Informasi Dataset =====")
df.info()
print("\n" + "="*30 + "\n")

print("===== Deskripsi Statistik Fitur Numerik =====")
print(df.describe())
print("\n" + "="*30 + "\n")

# Visualisasi distribusi fitur numerik
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df['TransactionAmount'], kde=True)
plt.title('Distribusi Jumlah Transaksi')

plt.subplot(1, 2, 2)
sns.histplot(df['Age'], kde=True)
plt.title('Distribusi Umur')
plt.tight_layout()
plt.show()

# Visualisasi distribusi fitur kategorikal
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.countplot(y='PaymentMethod', data=df, order=df['PaymentMethod'].value_counts().index)
plt.title('Distribusi Metode Pembayaran')

plt.subplot(1, 2, 2)
sns.countplot(y='DeviceType', data=df, order=df['DeviceType'].value_counts().index)
plt.title('Distribusi Tipe Perangkat')
plt.tight_layout()
plt.show()

# ===================== 2. Pembersihan & Pra-Pemrosesan =====================
print(f"Jumlah nilai null:\n{df.isnull().sum()}\n")
print(f"Jumlah data duplikat: {df.duplicated().sum()}")

id_columns = ['TransactionID', 'AccountID', 'DeviceID', 'IPAddress', 'MerchantID']
df_processed = df.drop(columns=id_columns, errors='ignore')

# Imputasi missing value numerik
numeric_features = df_processed.select_dtypes(include=np.number).columns.tolist()
df_processed[numeric_features] = df_processed[numeric_features].fillna(df_processed[numeric_features].median())

# Imputasi missing value kategorikal
categorical_features = df_processed.select_dtypes(include=['object']).columns.tolist()
for col in categorical_features:
    df_processed[col] = df_processed[col].fillna(df_processed[col].mode()[0])

# Scaling numerik
scaler = MinMaxScaler()
df_processed[numeric_features] = scaler.fit_transform(df_processed[numeric_features])

# Encoding kategorikal
encoders = {}
for col in categorical_features:
    encoder = LabelEncoder()
    df_processed[col] = encoder.fit_transform(df_processed[col])
    encoders[col] = encoder

print("\nDataset setelah preprocessing (Scaling dan Encoding):")
print(df_processed.head())

# ===================== 3. Clustering (KMeans & Elbow) =====================
print("Mencari jumlah cluster optimal dengan Elbow Method...")
model = KMeans(random_state=42, n_init='auto')
visualizer = KElbowVisualizer(model, k=(2, 10))
visualizer.fit(df_processed)
visualizer.show()
best_k = visualizer.elbow_value_
print(f"\nJumlah cluster terbaik yang disarankan adalah: {best_k}\n")

kmeans = KMeans(n_clusters=best_k, random_state=42, n_init='auto')
kmeans.fit(df_processed)
joblib.dump(kmeans, 'best_model_clustering')
print("Model clustering terbaik telah disimpan dengan nama 'best_model_clustering'")

# ===================== 4. Interpretasi Hasil Clustering =====================
df_original['Cluster'] = kmeans.labels_

original_numeric_features = df_original.select_dtypes(include=np.number).columns.drop('Cluster').tolist()
original_categorical_features = df_original.select_dtypes(include=['object']).columns.drop(id_columns, errors='ignore').tolist()

agg_funcs = {col: ['mean', 'min', 'max'] for col in original_numeric_features}
for col in original_categorical_features:
    agg_funcs[col] = lambda x: x.mode()[0]

cluster_interpretation = df_original.groupby('Cluster').agg(agg_funcs)

print("\n" + "="*50)
print("             HASIL AGREGASI PER CLUSTER")
print("="*50)
print(cluster_interpretation)
print("="*50 + "\n")

print("===== Analisis Hasil Clustering =====")
for i in range(best_k):
    cluster_data = cluster_interpretation.loc[i]
    desc = (
        f"Klaster {i} didapatkan karena "
        f"TransactionAmount rata-rata {int(cluster_data[('TransactionAmount', 'mean')])}, "
        f"min {int(cluster_data[('TransactionAmount', 'min')])}, max {int(cluster_data[('TransactionAmount', 'max')])}; "
        f"Age rata-rata {int(cluster_data[('Age', 'mean')])}; "
    )
    for col in original_categorical_features:
        desc += f"Modus {col}: '{cluster_data[(col, '<lambda>')]}'. "
    print(desc)

# ===================== 5. Klasifikasi =====================
X = df_processed
y = df_original['Cluster']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)
print("Model klasifikasi berhasil dilatih.\n")

y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Akurasi model klasifikasi pada data uji: {accuracy:.4f}\n")
print("Laporan Klasifikasi:")
print(classification_report(y_test, y_pred))

# Simpan model, scaler, dan encoder
joblib.dump(classifier, 'best_model_classifier')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(encoders, 'encoders.pkl')
print("Model, scaler, dan encoder telah disimpan.")

# ==============================================================================
# Tahap 0: Import Library yang Dibutuhkan
# ==============================================================================
import pandas as pd

df = pd.read_csv("3. Belajar Machine Learning untuk Pemula/2.machine_learning workflow/train.csv")
print(df['label'].value_counts())
print(df['prompt_name'].value_counts())
print(df.head())