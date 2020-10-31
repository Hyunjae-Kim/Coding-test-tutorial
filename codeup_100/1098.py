###추측해서 풀긴했으나, 문제 정의 명확하지 않음

h, w = map(int, input().split())
n = int(input())

board = [[0 for i in range(w)] for j in range(h)]
for i in range(n):
    l, d, hh, ww = map(int, input().split())
    hh -= 1
    ww -= 1

    if d==0:
        for j in range(l):
            board[hh][ww+j] = 1
    else:
        for j in range(l):
            board[hh+j][ww] = 1

for k in range(h):
    print(*board[k])