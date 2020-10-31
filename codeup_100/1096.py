num = int(input())
N = 19
board =[[0 for i in range(N)] for j in range(N)]

for k in range(num):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

for n in range(len(board)):
    print(*board[n])