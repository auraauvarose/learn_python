import seaborn as sns 
import matplotlib.pyplot as plt

# Data
tips = sns.load_dataset('tips') # memuat dataset tips dari seaborn

# contoh plot histogram 
sns.histplot(tips['total_bill'], kde=True) # kde = Kernel Density Estimation
plt.title("Contoh plot histogram")
plt.xlabel("Total bill")
plt.ylabel("Jumlah")
plt.show()

"""
Pada contoh di atas, kita menggunakan seaborn untuk melakukan visualisasi berdasarkan dataset tips. Dataset ini adalah bawaan dari library seaborn yang dapat Anda gunakan.

Hal pertama yang dilakukan adalah mengimpor modul seaborn. Selanjutnya, kita load dataset dan menyimpannya pada variabel tips.

Untuk membuat plot yang baik, di sini kita menggabungkan seaborn dan juga matplotlib. Library matplotlib digunakan untuk membuat title, xlabel, ylabel, dan menampilkannya ke layar.

Untuk membuat plot histogram pada seaborn, Anda dapat menggunakan sintaks “sns.histplot()” dengan sns adalah library seaborn dan histplot merupakan fungsinya. Jangan lupa untuk mengisikan value dalam fungsi tersebut. Pada contoh di atas kita menggunakan kolom total_bill yang ada dalam dataset tips.


"""