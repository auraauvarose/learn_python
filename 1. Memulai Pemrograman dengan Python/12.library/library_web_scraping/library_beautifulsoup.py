"""
Library Web Scraping
Library web scraping adalah jenis library untuk membantu pengguna mengumpulkan data dari halaman web. Proses ini disebut sebagai “web scraping” atau “web crawling”. Anda bisa menggunakan fungsi dan metode pada library ini untuk mengekstraksi informasi dari situs web dan menyimpannya dalam format yang dapat diakses dan digunakan dalam analisis atau aplikasi lainnya. 

"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


# Pengambilan konten
url = "https://python.org"
page = urlopen(url)
html = page.read().decode("utf-8")

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")


print(soup.prettify())

"""
Pada contoh di atas, kita melakukan web scraping untuk mengambil judul dari laman web “http://python.org/”. Hal pertama yang dilakukan adalah mengimpor Beautifulsoup sebagai library yang akan kita gunakan. Selanjutnya kita mengambil konten dari url dengan menggunakan fungsi dari modul “urlopen”. Setelah konten diambil, kita membuat objek BeautifulSoup dan dari objek ini kita bisa memunculkan beberapa konten berdasarkan tag html. Pada contoh di atas, kita mengambil judul halaman dengan menggunakan method “title”.

"""