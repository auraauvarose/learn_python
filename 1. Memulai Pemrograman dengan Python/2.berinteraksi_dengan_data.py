# Dekelarasi dan Inisialisasi
age = 17
salary = 1000000.0

print(type(age))
print(type(salary))

# Tipe data pada python
# 1. Integer (int) : bilangan bulat - 
# 2. Float (float) : bilangan pecahan
# 3. String (str) : teks
# 4. Boolean (bool) : True/False
# 5. List (list) : kumpulan data yang terurut

# implementasi tipe data Numbers ke python
X = 10 # integer
Y = 10.5 # float
Z = 10 + 5j # complex number
print(type(X)) # <class 'int'>
print(type(Y)) # <class 'float'>
print(type(Z)) # <class 'complex'>

# implementasi tipe data Boolean ke python
x = True # Bernilai benar
y = False # Bernilai salah
print(type(x)) # <class 'bool'>
print(type(y)) # <class 'bool'>

# implementasi tipe data String ke python
x = "Nama saya aura dan saya tinggal di jakarta"
print(type(x)) # <class 'str'>
# Formatted String
name = "aura"
print(f"nama saya adalah {name}") # nama saya adalah aura

# implemetasi tipe data List ke python
variabel_list = [1, "Umur saya 17", 3.14, True] # list dengan berbagai tipe data
print(type(variabel_list)) # <class 'list'>
print(variabel_list[2]) # 3.14 index ke 2, index dimulai dari 0
# ini adalah konsep indexing dalam list
x = ["laptop", "handphone", "tablet", "smartwatch", "earphone", "mouse"]
print(x[0]) # laptop
print(x[1]) # handphone
print(x[2]) # tablet
print(x[3]) # smartwatch
print(x[4]) # earphone
print(x[5]) # mouse
print(x[-1]) # mouse index -1, index dimulai dari -1

#tipe data dictionary
name = {' name': 'aura', 'age': 17, 'address': 'boyolali', 'menikah' : False }
print(type(name)) # <class 'dict'>

name = { # data disimpan dalam bentuk key-value pair
    'nama': 'Aura',
    'kelas': 20,
    'jurusan': 'Teknik Informatika',
    'vavorite': ['makan', 'tidur', 'bermain'],
}

#Operasi pada list, set, dan string
# List
contoh_list = [11, 22, 312, 411, 52]
print(contoh_list) # [1, 2, 3, 4, 5]
print(len(contoh_list)) # 5

#set
contoh_set = set([1, 2, 3, 4, 4, 4, 4, 5])
print(contoh_set) # {1, 2, 3, 4, 5}
print(len(contoh_set)) # 5

#string 
contoh_string = "Halo apa kabar kalian semuanya?"
print(contoh_string) # Halo apa kabar kalian semuanya?
print(len(contoh_string)) # 31 menghitung jumlah karakter

#min() dan max()
print(min(contoh_list)) # 11
print(max(contoh_list)) # 411

#in dan Not in 
kalimat = "Saya adalah manusia yang mempunyai akal dan pikiran"
#in
print("manusia" in kalimat) # True
print("makanan" in kalimat) # False
#not in
print("manusia" not in kalimat) # False
print("makanan" not in kalimat) # True 



