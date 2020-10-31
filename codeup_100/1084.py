num1, num2, num3 = list(map(int, input().split()))
count = 0
for i in range(num1):
    for j in range(num2):
        for k in range(num3):
            print('{} {} {}'.format(i,j,k))
            count += 1
print(count)