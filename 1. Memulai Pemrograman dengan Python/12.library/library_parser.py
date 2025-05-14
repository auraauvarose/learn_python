"""
Library Parser
Library parser pada Python menyediakan fasilitas untuk menguraikan kode Python menjadi struktur data yang dapat diproses dan dianalisis. Anda dapat menggunakan Getopt atau ArgParse. 

Argument parser bermanfaat jika kita ingin membuat program atau skrip kecil yang langsung menerima parameter pada saat pemanggilan program. Hal ini biasa digunakan dalam pemanggilan aplikasi atau skrip di CLI/terminal *nix-based, misalnya Linux dan MacOS. Contoh perintah dimaksud adalah berikut.

run di terminal: python panggildicoding.py -o

"""

import argparse
from datetime import datetime

"""
persen = argparse.ArgumentParser()
persen.add_argument("-o", "--output", action='store_true', help="output file")
args = persen.parse_args()

if args.output:
    print("Ini adalah perintah output dari library_parser.py")
    
1. Berkas dapat menerima parameter -o atau --output.
2. Jika kita memanggil berkas tanpa parameter -o, berkas tidak akan menampilkan apa pun.
3. Jika kita memanggil dengan -o atau --output, berkas akan menampilkan Halo, ini merupakan sebuah output dari panggildicoding.py.
4. Jika kita memanggil --help, tampil help dengan penjelasan "tampilkan output".

"""


# Setup argparse
data = argparse.ArgumentParser()
data.add_argument("-o", "--nama", required=True, help="Input nama anda")
data.add_argument("-a", "--alamat", required=True, help="Input alamat anda")
data.add_argument("-t", "--tanggal_lahir", required=True, help="Input tanggal lahir anda (format: DD-MM-YYYY)")
args = data.parse_args()

# Secara default, ketika kamu menggunakan argparse dan menetapkan argumen sebagai required=True, maka semua argumen wajib diisi. 

# Output data
print("Terima kasih sudah memperkenalkan diri anda:", args.nama)
print("Alamat anda:", args.alamat)

# Validasi tanggal
try:
    tgl = datetime.strptime(args.tanggal_lahir, "%d-%m-%Y")
    print("Tanggal lahir anda:", args.tanggal_lahir)
except ValueError:
    print("⚠️ Format tanggal tidak sesuai! Harus DD-MM-YYYY")


"""
1. Berkas harus dipanggil dengan parameter -n atau --nama.
2. Jika kita memanggil berkas tanpa parameter -n, berkas akan meminta parameter n atau nama.
3. Jika kita memanggil dengan -n NAMAKITA atau --nama NAMAKITA, berkas akan menampilkan Terima kasih telah menggunakan panggildicoding.py NAMAKITA.
4. Jika kita memanggil --help, tampil help dengan penjelasan "Masukkan Nama Anda".

"""
