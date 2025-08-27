import shutil
terminal_center = shutil.get_terminal_size().columns

print("hello word")

addlish = 1 + 2 # ini adalah variabel
result = addlish - 1
print(result)

nama = input("nama kamu: ")

judul_1 = "Tipe data pada python"  
print("\n" + judul_1.center(terminal_center, '-') + "\n")

# Tipe data pada python 
x = 6 # Tipe data integer
print(type(x)) 
x = 6.0 # Tipe data float
print(type(x))
x = 1+2j # Tipe data complex
print(type(x))
m = True  # Tipe data boolean
print(type(m))
m = False 
print(type(m))
s = "Hello" # Tipe data string
print(type(s))

# Tipe data multi line string
multi_line = """        nama : Aura
        kelas : 3
        umur : 20"""

print(multi_line)

i = 'Dikoding'
print(i[2:]) # Mengambil karakter pertama

#Tipe data 
#tipe data primitif 
x = 5
print(type(x)) #integer
x = 5.0
print(type(x)) #float
x = 1+2j
print(type(x)) #complex
x = True
print(type(x)) #boolean
x = "hello"
print(type(x)) #string
print(f"hello {nama}") # formated string

judul_1 = "Tipe Data Collection dan disctionary"
print("\n" + judul_1.center(terminal_center, '-') + "\n")

# tipe data collection
variable_list = [1, "Aura", True, 5.0] # list
print(variable_list[3]) # list mulai dihitung dari 0
variable_list[3] = "Indonesia" # mengubah nilai list
print(variable_list)

x = { 'name ': 'Aura', 'age': 20} # dictionary
print(type(x))
data_diri = {
    'name': "Aura", 
    'umur': 20,
    'kelas': 3,
    'alamat': "sadon dawahan"
}
print(data_diri) # mengambil nilai dictionary

judul_1 = "Transformasi Angka, Karakter, dan String"
print("\n" + judul_1.center(terminal_center, '-') + "\n")

# Mengubah huruf besar e kecil atau kecil ke besar
kata = "Dicoding"
kata = kata.upper() # mengubah huruf kecil ke besar
print(kata)
kata = kata.lower() # mengubah huruf besar ke kecil
print(kata)

print('Dicoding'.rjust(50)) # rjust() untuk rata kanan
print('Dicoding'.ljust(100)) # ljust() untuk rata kiri
print('Dicoding'.center(10, '-')) # center() untuk rata tengah

judul_1 = "Operasi pada list, set, dan string"
print("\n" + judul_1.center(terminal_center, '-') + "\n")

umur = 17
umur_float = 50000.0
umur_bool = True

print(type(umur))
print(type(umur_float))
print(type(umur_bool))


judul_1 = "Mencoba penggunaan if else"
print("\n" + judul_1.center(terminal_center, '-') + "\n")

sandi = 20
password = input("masukan angka kamu")
hasil = int(password)

if hasil > sandi:
    print("Password benar sekali cuy")
elif hasil == sandi:
    print("Password tepat")
else:    
    print("Password anda salah")
