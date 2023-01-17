#menghitung angka
angka = int(input("Masukan angka: "))

#jika habis dibagi nol,maka genap
if(angka % 2) == 0:
    print("{0} adakah bilangan genap".format(angka))

#jika tidal habis di bagi nol,maka ganjil
else:
    print("{0} adakah bilangan ganjil".format(angka))