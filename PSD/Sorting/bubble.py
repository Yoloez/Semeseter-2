n = int(input())
N = list(map(int,input().split()))

def bubble(N):
    panjang = len(N)
    iterasi = 0
    for i in range (panjang-1):
        for j in range(panjang-1-i):
            iterasi += 1
            if N[j] > N[j+1]:
                N[j], N[j+1] = N[j+1], N[j]
    for angka in N:
        print(angka, end=" ")
    print('')
    print("Iterasi:",iterasi)
    
bubble(N)
