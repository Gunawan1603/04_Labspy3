#Tampilkan n bilangan acak yang lebih kecil dari 0.5,menggunakan kombinasi while dan for, & fungsi random().
print ()
jumlah=int(input("Masukkan nilai N:  "))
import random
n = 0
for n in range(jumlah):
    a = random.uniform(.0,.5)
    n+=1
    print("data ke : " ,n, "==>", a )
print ("<<< Selesai >>>")
