from sys import stdin
import copy

num = int(stdin.readline().rstrip())
new_num = copy.copy(num)
count = 0

while 1:
    num_var = '{:0>2}'.format(new_num)
    num1, num2 = num_var[0], num_var[1]

    num_sum = int(num1)+int(num2)
    num_sum_var = '{:0>2}'.format(num_sum)
    num1_, num2_ = num_sum_var[0], num_sum_var[1]

    new_num = int('{:0>2}'.format(num2+num2_))
    count += 1
    if new_num==num:
        break

print(count)

##더 심플하게 가능