import pandas as pd

"""
Pandas adalah library populer yang digunakan untuk pengelolaan dan analisis data. Library ini menyediakan struktur data dan alat untuk membantu pengguna dalam melakukan manipulasi, pembersihan, transformasi, dan analisis data dengan mudah dan efisien.

Meskipun pandas sudah terinstal secara otomatis pada beberapa IDE dan versi Python, perlu diingat bahwa pandas bukan merupakan library bawaan Python. Oleh karena itu, Anda harus menginstal library ini terlebih dahulu sebelum dapat menggunakannya. Silakan buka command prompt dan jalankan kode berikut.

"""

data = {
    'nama': ['Budi', 'Andi', 'Cindy', 'Dian'],
    'umur': [20, 25, 30, 35],
    'gaji': [5000000, 6000000, 7000000, 8000000]
}

df = pd.DataFrame(data)

print(df)