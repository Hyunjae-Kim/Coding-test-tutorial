from sys import stdin

num = int(stdin.readline().rstrip())
for i in range(num):
    A, B = map(int, stdin.readline().split())
    print('Case #{}: {} + {} = {}'.format(i+1, 
          A, B, A+B))