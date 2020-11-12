def solve(a):
    result = a
    for i in range(len(str(a))):
        result += int(str(a)[i])
    return result

count = 0
num_list = list(range(1,10000))
while count<len(num_list):
    check_num = num_list[count]
    
    while check_num<10000:
        check_num = solve(check_num)
        try:
            num_list.remove(check_num)
        except ValueError:
            break
    count += 1

print(*num_list, end='\n')