"""
Melatih Model (Training)
Model akan "belajar" dari data training dengan menyesuaikan parameternya agar dapat memetakan input (fitur) ke output (target) dengan baik. Selama pelatihan, model akan menyesuaikan bobot atau koefisiennya untuk meminimalkan kesalahan antara prediksi dan nilai sebenarnya dalam training set. 

Ada dua hal yang perlu Anda perhatikan pada tahapan ini, yaitu fitur dan target. Fitur adalah data input yang digunakan untuk melatih model, sedangkan target adalah data output yang menjadi referensi model untuk belajar. 

Perlu Anda catat, pada latihan ini kita tidak akan melakukan hyperparameter tuning sehingga algoritma yang digunakan akan menghasilkan output berdasarkan konfigurasi dasarnya. Sebagai pemanasan, mari kita latih data yang sudah kita miliki dengan tiga algoritma yang berbeda.
"""

# Melatih model 1 dengan algoritma Least Angle Regression
from sklearn import linear_model
lars = linear_model.Lars(n_nonzero_coefs=1).fit(x_train, y_train)
 
# Melatih model 2 dengan algoritma Linear Regression
from sklearn.linear_model import LinearRegression
LR = LinearRegression().fit(x_train, y_train)
 
# Melatih model 3 dengan algoritma Gradient Boosting Regressor
from sklearn.ensemble import GradientBoostingRegressor
GBR = GradientBoostingRegressor(random_state=184)
GBR.fit(x_train, y_train)

"""
Evaluasi Model
Model yang telah dilatih perlu melalui tahapan evaluasi berdasarkan validation set untuk melihat seberapa baik ia mampu memprediksi output yang benar dari input yang belum pernah dilihat sebelumnya. Metrik umum untuk evaluasi adalah accuracy, precision, recall, F1-score (untuk klasifikasi), dan Mean Squared Error (MSE) atau R-squared (untuk regresi). 

Karena contoh kasus yang sedang kita hadapi merupakan regresi, evaluasi yang akan akan kita gunakan adalah MAE, MSE, dan R2. Untuk melakukan evaluasi ini kita membutuhkan validation set (x_test). Validation test merupakan bagian dari data yang tidak digunakan untuk pelatihan tetapi digunakan untuk mengevaluasi model (unseen data). Mari kita lakukan evaluasi satu per satu.
"""

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
 
# Evaluasi pada model LARS
pred_lars = lars.predict(x_test)
mae_lars = mean_absolute_error(y_test, pred_lars)
mse_lars = mean_squared_error(y_test, pred_lars)
r2_lars = r2_score(y_test, pred_lars)
 
# Membuat dictionary untuk menyimpan hasil evaluasi
data = {
    'MAE': [mae_lars],
    'MSE': [mse_lars],
    'R2': [r2_lars]
}

# Konversi dictionary menjadi DataFrame
df_results = pd.DataFrame(data, index=['Lars'])
df_results

# Evaluasi pada model Linear Regression
pred_LR = LR.predict(x_test)
mae_LR = mean_absolute_error(y_test, pred_LR)
mse_LR = mean_squared_error(y_test, pred_LR)
r2_LR = r2_score(y_test, pred_LR)
 
# Menambahkan hasil evaluasi LR ke DataFrame
df_results.loc['Linear Regression'] = [mae_LR, mse_LR, r2_LR]
df_results

# Evaluasi pada model Linear Regression
pred_GBR = GBR.predict(x_test)
mae_GBR = mean_absolute_error(y_test, pred_GBR)
mse_GBR = mean_squared_error(y_test, pred_GBR)
r2_GBR = r2_score(y_test, pred_GBR)
 
# Menambahkan hasil evaluasi LR ke DataFrame
df_results.loc['GradientBoostingRegressor'] = [mae_GBR, mse_GBR, r2_GBR]
df_results

"""
Menyimpan Model
Untuk menyimpan model yang telah dilatih, Anda dapat menggunakan modul joblib atau pickle pada Python. Kedua modul ini memungkinkan Anda untuk menyimpan model ke dalam sebuah file sehingga bisa digunakan kembali di masa mendatang tanpa perlu melatih ulang model. Mari kita bahas kedua cara tersebut secara saksama.


"""

# Joblib
# Joblib adalah pilihan yang disarankan untuk menyimpan model scikit-learn karena lebih efisien dalam menyimpan objek model yang besar.
import joblib
 
# Menyimpan model ke dalam file
joblib.dump(GBR, 'gbr_model.joblib')

# Pickle
# Pickle adalah modul standar Python yang dapat digunakan untuk menyimpan hampir semua objek Python termasuk model machine learning.
import pickle
 
# Menyimpan model ke dalam file
with open('gbr_model.pkl', 'wb') as file:
    pickle.dump(GBR, file)
    
"""
Kapan menggunakan joblib vs pickle? joblib lebih efisien dan cepat ketika bekerja dengan objek besar seperti model machine learning, sedangkan pickle lebih umum dan dapat digunakan untuk menyimpan berbagai jenis objek Python, tetapi kurang efisien dibandingkan joblib untuk model besar.

Memilih antara joblib dan pickle tergantung pada preferensi Anda, tetapi untuk menyimpan model scikit-learn, joblib sering kali merupakan pilihan yang lebih baik.
"""