w, h, b = list(map(int, input().split()))
memory = w*h*b
memory_MB = (memory/8)/(1024**2)
print('{:.2f} MB'.format(memory_MB))