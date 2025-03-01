n = int(input())
N = list(map(int, input().split()))

def selection(N):
    panjang = len(N)
    for i in range(panjang):
        terkecil = i
        for j in range(i + 1,n):
            if N[j] < N[terkecil]:
                terkecil = j
        N[i], N[terkecil] = N[terkecil], N[i]
        for angka in N:
            print(angka, end=" ")
        print('')

selection(N)
