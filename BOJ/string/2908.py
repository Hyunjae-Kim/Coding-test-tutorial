f = lambda i : int(i[::-1])
two_num = map(f, input().split())
print(max(two_num))
