#Buat program untuk menampilkan bilangan terbesar dari n buah data yang diinputkan.
#Masukkan angka 0 untuk berhenti
x=0
while True:
    a=int(input("Masukkan Bilangan : "))
    if x<a:
        x=a
    if a==0:
        break
print("Bilangan terbesar adalah =",x)
