num = int(input())
b_list = []
count = 0
for k in range(num):
    height=int(input())

    while 1:
        if len(b_list)==0:
            b_list.append(height)
            break
        if b_list[-1]<=height:
            b_list.pop()
        else:
            count += len(b_list)
            b_list.append(height)
            break
print(count)
