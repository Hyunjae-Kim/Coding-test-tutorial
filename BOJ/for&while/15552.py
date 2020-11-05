import sys

num = int(input())
for i in range(num):
    num1, num2 = map(int, sys.stdin.readline().rstrip().split())
    print(num1+num2)