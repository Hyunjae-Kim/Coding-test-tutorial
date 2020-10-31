num = int(input())
check = list(map(int, input().split()))
check_arr = [0]*23
for i in (check):
    check_arr[i-1] += 1
print(*check_arr, sep=' ')