"""
Halaman ini membahas **data cleaning dan transformation** dalam machine learning, yang merupakan langkah krusial sebelum data digunakan untuk melatih model. Berikut adalah poin-poin utama dari halaman tersebut:

### **Pentingnya Data Cleaning**
- **Menghabiskan banyak waktu** dalam pekerjaan seorang data scientist.
- **Meningkatkan kualitas data**, yang berpengaruh langsung terhadap akurasi dan performa model.
- **Konsep “Garbage In - Garbage Out”** berlaku—data buruk menghasilkan prediksi buruk.

### **Manfaat Data Cleaning**
1. **Meningkatkan Akurasi Model** – Data bersih memungkinkan model belajar pola yang sebenarnya.
2. **Mencegah Overfitting** – Data yang tidak akurat atau penuh noise bisa menyebabkan model terlalu menyesuaikan diri dengan data latih.
3. **Meningkatkan Efisiensi** – Data yang bersih mempermudah proses analisis dan pemodelan.
4. **Memastikan Keandalan** – Data yang tidak bersih dapat memperkenalkan bias atau kesalahan dalam pengambilan keputusan.

### **Tahapan Utama dalam Data Cleaning**
1. **Mengidentifikasi dan Menangani Nilai Hilang (Missing Values)**  
   - Menghapus atau mengganti nilai dengan **mean, median, atau modus**.  
   - Menggunakan metode lebih canggih seperti **KNN atau regresi** jika data yang hilang berpengaruh besar.

2. **Mengidentifikasi dan Menangani Outliers**  
   - Menghapus outliers jika disebabkan oleh **kesalahan pengukuran**.  
   - Menggunakan **transformasi log** jika outliers adalah bagian dari distribusi normal.

3. **Normalisasi dan Standardisasi Data**  
   - Memastikan fitur-fitur memiliki **skala yang sama**, penting untuk algoritma tertentu seperti KNN atau SVM.

4. **Menangani Duplikasi Data**  
   - Duplikasi bisa terjadi akibat **kesalahan input atau penggabungan dataset**, harus dihapus agar model tidak bias.

5. **Mengonversi Tipe Data dan Menangani Inkonsistensi**  
   - **Menyamakan format data**, seperti penulisan tanggal atau mata uang.  
   - **Konversi tipe data**, misalnya variabel kategorikal ke format numerik melalui **one-hot encoding**.  
   - **Menyesuaikan skala data**, memastikan nilai dalam rentang yang benar.

Data cleaning adalah **langkah vital** dalam membangun model machine learning agar lebih akurat dan andal. Tahapan-tahapan ini **tidak selalu harus dilakukan semua**—tergantung karakteristik dataset yang digunakan.  

Semoga rangkuman ini membantu! 😊 Ada bagian yang ingin dijelaskan lebih detail?

"""