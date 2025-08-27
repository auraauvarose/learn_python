"""
Data splitting adalah langkah krusial dalam machine learning yang bertujuan untuk membagi dataset menjadi beberapa bagian agar model bisa belajar dengan baik, divalidasi dengan adil, dan diuji dengan akurat sebelum digunakan untuk prediksi nyata. Ada tiga bagian utama dalam data splitting: training set untuk melatih model, validation set untuk menyesuaikan hyperparameter, dan test set untuk mengevaluasi kinerja model dengan data baru.

Teknik yang digunakan dalam data splitting juga beragam, seperti Holdout Method yang paling sederhana, K-Fold Cross Validation untuk hasil evaluasi yang lebih akurat, Stratified Splitting yang memastikan proporsi kelas tetap seimbang, serta Time Series Splitting yang mempertimbangkan urutan waktu dalam data.

Selain itu, ada beberapa aspek penting yang perlu dipertimbangkan:

Menghindari Data Leakage, yaitu mencegah agar informasi dari test set tidak mempengaruhi pelatihan model.

Menjaga Randomness, agar pembagian data tidak bias dan tetap representatif.

Menyesuaikan Rasio Pembagian, di mana angka umum yang digunakan adalah 70:30 atau 80:20 untuk training dan testing, atau 60:20:20 jika ada validation set.

Ada juga perdebatan tentang apakah preprocessing sebaiknya dilakukan sebelum atau sesudah data splitting. Beberapa langkah seperti imputasi missing values dan encoding kategorikal sebaiknya dilakukan sebelum splitting agar tetap konsisten di seluruh dataset. Namun, standardisasi dan scaling lebih baik dilakukan setelah splitting agar tidak terjadi data leakage.

"""