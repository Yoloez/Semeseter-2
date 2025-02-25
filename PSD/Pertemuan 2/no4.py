mahasiswa = {
    "2351345TK22456": "Fahim",
    "2467890KG25467": "Edelweis",
    "2245644SV23478": "Muhammad Hardiyanto"
}

nim = input('Masukkan NIM: ')
if nim in mahasiswa.keys():
    print(mahasiswa[nim])
else:
    print('Mahasiswa tidak ada dalam daftar')