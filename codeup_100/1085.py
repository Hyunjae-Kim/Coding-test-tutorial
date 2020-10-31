h, b, c, s = list(map(int, input().split()))
memory = h*b*c*s
memory_mb = (memory/8)/(1024**2)
print('{:.1f} MB'.format(memory_mb))