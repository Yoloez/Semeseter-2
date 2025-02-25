kalimat = input('Masukkan sebuah kalimat: ')
vokal = ['a', 'i','u','e','o']
print(len(kalimat))
print(kalimat.upper())
for huruf in vokal:
    jumlah_vokal = kalimat.count(huruf)
    print(f'huruf {huruf} muncul sebanyak {jumlah_vokal}')