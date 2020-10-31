day1, day2, day3 = list(map(int, input().split()))
count = 1
while (count%day1!=0) or (count%day2!=0) or (count%day3!=0):
    count += 1
print(count)