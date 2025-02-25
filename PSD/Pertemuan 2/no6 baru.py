data = []

while True:
    mahasiswa = {}
    nama = input('Masukkan nama: ')
    nim = int(input('Masukkan nim: '))
    daerah = input('Masukkan daerah: ')
    mahasiswa['nama'] = nama
    mahasiswa['nim'] = nim
    mahasiswa['daerah'] = daerah
    data.append(mahasiswa)
    opsi = input('Lanjut? (y/n) ')
    if opsi == 'n':
        print(data)
        break
    else:
        True


