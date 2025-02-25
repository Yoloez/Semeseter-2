hari = ('senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu')
angka = [1,2,3,4,5,6,7]
masuk = int(input('Masukkan angka (1-7): '))
if masuk not in angka:
    print('Masukkan angka 1-7')
else:
    print(hari[masuk-1])
