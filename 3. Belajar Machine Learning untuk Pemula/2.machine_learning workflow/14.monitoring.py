# Memuat model dari file joblib
joblib_model = joblib.load('gbr_model.joblib')
 
# Memuat model dari file pickle
with open('gbr_model.pkl', 'rb') as file:
    pickle_model = pickle.load(file)
    
    
    
from flask import Flask, request, jsonify
import joblib
 
# Inisialisasi aplikasi Flask
app = Flask(__name__)
 
# Memuat model yang telah disimpan
joblib_model = joblib.load('gbr_model.joblib') # Pastikan path file sesuai dengan penyimpanan Anda
 
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']  # Mengambil data dari request JSON
    prediction = joblib_model.predict(data)  # Melakukan prediksi (harus dalam bentuk 2D array)
    return jsonify({'prediction': prediction.tolist()})
 
if __name__ == '__main__':
    app.run(debug=True)
    
"""
Setelah model di-deploy ke dalam produksi, monitoring menjadi sangat penting untuk memastikan bahwa model terus bekerja dengan baik dan tetap relevan seiring waktu. Walaupun pada tahapan ini kita masih melakukan deployment di local, materi tentang monitoring ini masih sangat relevan. Karena Anda akan mempelajari Machine Learning Operations di kelas-kelas berikutnya. Sampai pada kelas tersebut, silakan reviu kembali kelas ini sebagai bekal utama, ya.

Mungkin muncul sebuah pertanyaan, “Mengapa monitoring penting?” Model machine learning dapat mengalami penurunan kinerja dari waktu ke waktu karena perubahan dalam data yang masuk (concept drift) atau perubahan dalam distribusi data (data drift). Selain itu, monitoring membantu mendeteksi anomali atau bug yang mungkin muncul saat model digunakan di dunia nyata. Dan yang paling penting monitoring juga berperan untuk memastikan bahwa model mematuhi regulasi atau kebijakan internal terkait privasi, keamanan, atau fairness.

Biasanya model machine learning memiliki metrik dan alat untuk membantu monitoring. Berikut adalah metrik dan alat yang bisa digunakan ketika Anda memonitoring model machine learning di lingkungan produksi.

Metrik yang Dimonitor:

Accuracy, Precision, Recall, F1-Score: digunakan untuk memantau kinerja model klasifikasi.
Mean Squared Error (MSE), R-squared: digunakan untuk model regresi.
Data Drift Metrics: memantau perubahan distribusi data input dibandingkan dengan data yang digunakan saat pelatihan.
Model Latency: mengukur waktu yang diperlukan model untuk memberikan prediksi. Hal ini penting untuk aplikasi real-time.
Alat Monitoring:

Prometheus/Grafana: digunakan untuk memantau metrik dan membuat dashboard custom.
ELK Stack (Elasticsearch, Logstash, Kibana): digunakan untuk monitoring log dan menganalisis anomali.
Sentry: digunakan untuk mendeteksi dan melaporkan error di aplikasi yang mengintegrasikan model.
MLflow: alat khusus untuk tracking eksperimen dan monitoring model machine learning.
Sampai di sini Anda dapat memastikan bahwa model machine learning yang dibuat tidak hanya berguna pada saat dilatih, tetapi juga terus memberikan nilai saat digunakan di dunia nyata. 

Sebagai penutup, Anda telah mencapai akhir babak dari materi ini yaitu Deployment dan Monitoring. Dengan pemahaman ini, Anda mampu memastikan model yang dibangun tidak hanya bekerja di lingkungan pengembangan, tetapi juga mampu bertahan dan beradaptasi dalam skenario dunia nyata.

Namun, perjalanan Anda belum selesai di sini. Di modul berikutnya, kita akan membahas lebih dalam tentang berbagai macam machine learning yang ada. Mulai dari supervised learning, unsupervised learning, hingga optimasi machine learning yang memiliki keunikan dan objektif masing-masing. Penasaran bagaimana algoritma-algoritma ini bekerja dan kapan waktu terbaik untuk menggunakannya? Jangan lewatkan pembahasan berikutnya yang akan membuka lebih banyak wawasan dan kemungkinan di dunia machine learning. Sampai jumpa!
"""