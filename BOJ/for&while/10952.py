from sys import stdin

while 1:
    A, B = map(int, stdin.readline().split())

    if A+B==0:
        break
    else:
        print(A+B)
    