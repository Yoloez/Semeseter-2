
angka = list(map(int, input().split()))
total = 0 
print(angka)
for i in angka:
    total += i
print(total)
angka.sort()
print(angka)
angka.pop()
print(angka)