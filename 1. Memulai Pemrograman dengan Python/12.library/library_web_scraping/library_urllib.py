"""
Urllib
Urllib adalah library bawaan dari Python yang bertujuan untuk scraping konten dari sebuah website. Penggunaan urllib berbeda dengan beautifulsoup. Bisa dikatakan bahwa cara penggunaan urllib sedikit kompleks dibandingkan beautifulsoup. Kode di bawah adalah contoh untuk memulai proses scraping pada situs dengan domain python.org dan menampilkan isi dari tag title dari situs tersebut.

"""

from urllib.request import urlopen
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
 
# Mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]
print(title)


"""
Pada kode di atas, kita melakukan scraping terhadap url yang sama seperti contoh sebelumnya. Namun, kali ini kita menggunakan urlopen untuk mengambil title dari laman “http://python/org/”

Hal pertama yang dilakukan adalah mengimpor urlopen dengan menggunakan “from urllib.request import urlopen”. Selanjutnya, kita mengambil konten dari url yang telah ditentukan.

Tahapan ketiga adalah kita mencari indeks awal dan akhir. Tujuan kita adalah mengambil title sehingga indeksnya ditentukan dari tag “<title>” dan “</title>”. Terakhir, kita mengekstrak dan mencetak judul halaman tersebut.

"""