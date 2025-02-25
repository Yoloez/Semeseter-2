setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
set_gabung = setA.union(setB)
print(set_gabung)
set_irisan = setA.intersection(setB)
print(set_irisan)
set_selisihab = setA.difference(setB)
print(set_selisihab)
set_selisihba = setB.difference(setA)
print(set_selisihba)
selisih = set_selisihab.difference(set_selisihba)
print(selisih)