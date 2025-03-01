n = int(input())
N = list(map(int, input().split()))
def insertion (N):
    for i in range (1, len(N)):
        x = N[i]
        j = i-1
        while j >= 0 and N[j] > x:
            N[j+1] = N[j]
            j -= 1
        N[j+1] = x
        for i in  N:
            print(i, end=" ")
        print("")
insertion(N)