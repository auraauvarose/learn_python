import sklearn # Import library sklearn

# Memisahkan fitur (X) dan target (y)
X = df_lencoder.drop(columns=['SalePrice'])  
y = df_lencoder['SalePrice'] 

from sklearn.model_selection import train_test_split
 
 
"""
Ketika Anda menjalankan train_test_split, fungsi ini akan mengembalikan empat bagian data seperti berikut.

X_train: fitur untuk train set.
X_test: fitur untuk test set.
y_train: target untuk train set.
y_test: target untuk test set.
Ini berarti setelah pemanggilan fungsi, Anda memiliki dua bagian data: satu untuk melatih model (train set) dan satu lagi untuk menguji model (test set).
"""
# membagi dataset menjadi training dan testing 
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# menghitung panjang/jumlah data 
print("Jumlah data: ",len(X))
# menghitung panjang/jumlah data pada x_test
print("Jumlah data latih: ",len(x_train))
# menghitung panjang/jumlah data pada x_test
print("Jumlah data test: ",len(x_test))