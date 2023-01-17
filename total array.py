array =[]
#membuat variabel total

total = 0

#membuat variabel n untuk menampung jumlah array
# n = jumlah elemen

n = int(input("Masukan Jumlah Elemen Array : "))
for x in range(n):
    #menginputkan nilai yang akan bertambah 1
    nilai = float(input("Masukan Nilai Ke-  {} : "))
    array.append(nilai)
    #menampilkan jualan dari nilai
    print('\nhasil nilai total adalah : {}'.format(sum(array)))
    #menampilkan rata rata
    print('hasil rata rata adalah : {}'.format(sum(array)/n))

