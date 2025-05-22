"""
mengapa data ecollecting itu penting?
Data collecting adalah langkah awal yang sangat penting dalam machine learning karena kualitas dan kuantitas data yang dikumpulkan akan mempengaruhi performa model yang dibangun. Berikut adalah beberapa alasan mengapa data collecting itu penting:

1. Menentukan akurasi model: Data yang berkualitas tinggi dan relevan akan membantu model belajar dengan baik, sedangkan data yang buruk dapat menyebabkan model tidak akurat atau bias.

2. Mencegaj Bias: Pengumpulan data yang beragam dan representatif dapat membantu mengurangi bias dalam model, sehingga model dapat bekerja dengan baik pada berbagai kondisi dan populasi.

3. Mengkomodasikan data: Data yang dikumpulkan harus sesuai dengan tujuan analisis. Misalnya, jika kita ingin membangun model prediksi harga rumah, kita perlu mengumpulkan data tentang harga rumah, lokasi, ukuran, dan faktor-faktor lain yang mempengaruhi harga.

Lantas, bagaimana cara kita mengumpulkan data? Berikut adalah beberapa metode umum untuk mengumpulkan data:

1. Data Internal: Menggunakan data yang sudah ada di dalam organisasi, seperti database, laporan, atau sistem informasi.

2. Data Eksternal: Mengumpulkan data dari sumber eksternal seperti API, web scraping, atau dataset publik yang tersedia di internet.

3. Data sintetis: Menghasilkan data buatan menggunakan algoritma atau simulasi untuk melengkapi data yang kurang.

4. Data yang dihasilkan oleh pengguna: Mengumpulkan data dari interaksi pengguna dengan aplikasi atau sistem, seperti umpan balik, survei, atau perilaku pengguna.

Mari sekarang kita bisa lakukan untuk mengumpulkan data: 

1. mengextrak data (misal dari interent, riset, survai, dll)

2. Mengumpulkan data dan membuat dataset anda sendiri dari nol

3. Menggunakan dataset yang sudah ada (misal dari Kaggle, UCI ML Repository, dll)


Setelah memiliki bekal terkait pengumpulan alangkah lebih baiknya Anda juga mempelajari langkah-langkah yang umum dilakukan untuk melakukan pengumpulan data. Berangkat dari pengetahuan yang sudah dipelajari pada materi ini, mari kita bahas langkah-langkah dalam proses pengumpulan data.

1. Menentukan Kebutuhan Data.
Sebelum mengumpulkan data, Anda harus memperjelas objektif tentang apa yang ingin Anda prediksi atau analisis. Ini akan membantu Anda menentukan jenis data apa yang perlu dikumpulkan dan dalam jumlah berapa.

2. Memilih Sumber Data.
Setelah mengetahui kebutuhan Anda, langkah selanjutnya adalah memilih sumber data yang sesuai. Apakah Anda akan menggunakan data internal, mengunduh data publik, atau melakukan survei sendiri?

3. Mengumpulkan dan Menyimpan Data.
Setelah sumber data dipilih, Anda mulai mengumpulkan data. Ini bisa melalui API, survei, scraping web, atau impor data dari file. Pastikan data disimpan dengan baik dan aman, serta dalam format yang mudah diakses untuk analisis lebih lanjut.

4. Validasi dan Pembersihan Data.
Data yang terkumpul mungkin mengandung kesalahan atau data yang hilang. Oleh karena itu, proses validasi dan pembersihan data penting untuk memastikan data yang Anda gunakan berkualitas tinggi.

Sampai pada tahap ini Anda sudah mengetahui secara utuh tahapan pengumpulan data, tetapi untuk mempermudah pemahaman mari kita bayangkan beberapa studi kasus.

Bayangkan Anda ingin membangun model machine learning untuk memprediksi harga rumah. Langkah pertama yang Anda lakukan adalah mengumpulkan data. Anda bisa mengumpulkan data dari beberapa sumber berikut.

1. Website properti untuk mendapatkan informasi harga, lokasi, ukuran rumah, dan tahun bangunan.

2. Data ekonomi dari pemerintah yang memberikan informasi mengenai tingkat bunga hipotek dan tren pasar properti.

3. Data survei pelanggan untuk mendapatkan preferensi dan kebutuhan dari calon pembeli rumah.


Setelah data terkumpul, Anda membersihkannya, memastikan tidak ada data yang hilang, dan mulai menggunakannya untuk melatih model prediksi harga rumah. Dengan data yang tepat, model Anda akan mampu memberikan estimasi harga rumah yang akurat.

"""