"""
JSON
Untuk serialization dengan bahasa lain, umumnya kita menggunakan JSON(JavaScript Object Notation) yang memiliki beberapa perbedaan karakteristik dengan pickle, yakni berikut.
    1. JSON adalah format text-serialization dan umumnya menggunakan Unicode atau UTF-8. Sementara pickle bersifat binary serialization.
    2. JSON dapat dibaca dengan mudah oleh manusia, sementara pickle tidak.
    3. JSON dapat dioperasikan dan digunakan di luar ekosistem Python. Pickle adalah Python-specific.
    4. JSON secara default hanya dapat merepresentasikan subset dari built-in type pada Python.
    5. Pickle dapat merepresentasikan hampir (jika tidak seluruh) tipe Python dan secara default melakukan kompresi data.

Sebagaimana yang telah disebutkan sebelumnya, JSON adalah format text yang ditujukan untuk serialization. Agar data dapat dengan mudah ditransmisikan antar berbagai sumber tanpa khawatir bentuknya kacau, menggunakan JSON adalah salah satu pilihan yang tepat.

JSON memiliki format yang hampir mirip dengan dictionary, yakni data disimpan dengan format key dan value pair. Namun, tentunya JSON jauh lebih kompleks dari dictionary. Dapat dilihat dari contoh JSON untuk data pembelian di bawah.

Dengan JSON kita dapat menyimpan data dengan lebih teratur. Sebuah key seperti children di bawah dapat memiliki sebuah dictionary baru yang berisi informasi terkait objek children tersebut.

"""

import json

# contoh json
x = '{"name": "John", "age": 30, "city": "New York"}'

# parsing json
y = json.loads(x)

print(y["age"])