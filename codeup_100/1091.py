a, m, d, n = list(map(int, input().split()))
result = a
for i in range(n-1):
    result *= m
    result += d
print(result)