from sys import stdin

num = int(stdin.readline().rstrip())

for i in range(num):
    print(('{:>%d}'%num).format('*'*(i+1)))