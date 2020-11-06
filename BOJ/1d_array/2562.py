from sys import stdin

num_list = [int(input()) for i in range(9)]
f = lambda i: num_list[i]

print(max(num_list))
print(max(range(len(num_list)), key=f)+1)