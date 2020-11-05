from sys import stdin

N, X = map(int, stdin.readline().split())
A_list = list(map(int stdin.readline().split()))

for i in range(N):
    if A_list[i]<X:
        print(A_list[i], end=' ')
    else:
        continue