tugas = float(input("masukan nilai tugas"))
uas = float(input("masukan nilai tugas"))
uts = float(input("masukan nilai tugas"))

nilai = (0.15 * tugas) + (0.35 * uts) + (0.55 * uas)
#menentukan grade berdasarkan bilai akhir
if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'
elif nilai > 50:
    grade = 'D'
else:
    grade = 'E'
#menentukan status kelulusan berdasarkan nilai akhir
if nilai > 60:
    status = 'lulus'
else:
    status = 'Tidak lulus'


#menampilkan nilai akhir, grade, dan Status kelulusan
print('Nilai Akhir: %0.2f' % nilai)
print('grade: {}'.format(grade))
print('Status: {}'.format(status))