"""
Library Parser
Library parser pada Python menyediakan fasilitas untuk menguraikan kode Python menjadi struktur data yang dapat diproses dan dianalisis. Anda dapat menggunakan Getopt atau ArgParse. 

Argument parser bermanfaat jika kita ingin membuat program atau skrip kecil yang langsung menerima parameter pada saat pemanggilan program. Hal ini biasa digunakan dalam pemanggilan aplikasi atau skrip di CLI/terminal *nix-based, misalnya Linux dan MacOS. Contoh perintah dimaksud adalah berikut.

run di terminal: python panggildicoding.py -o

"""

import argparse

persen = argparse.ArgumentParser()
persen.add_argument("-o", "--output", action='store_true', help="output file")
args = persen.parse_args()

if args.output:
    print("Ini adalah perintah output dari library_parser.py")
    
"""
1. Berkas panggildicoding.py dapat menerima parameter -o atau --output.
2. Jika kita memanggil berkas tanpa parameter -o, berkas tidak akan menampilkan apa pun.
3. Jika kita memanggil dengan -o atau --output, berkas akan menampilkan Halo, ini merupakan sebuah output dari panggildicoding.py.
4. Jika kita memanggil --help, tampil help dengan penjelasan "tampilkan output".

"""

