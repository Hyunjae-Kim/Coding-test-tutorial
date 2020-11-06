from sys import stdin
num = int(stdin.readline().rstrip())

num_list = list(map(int, stdin.readline().split()))
print(min(num_list), max(num_list))


## short coding
# input()
# *list, = map(int, input().split())
# print(min(list), max(list))